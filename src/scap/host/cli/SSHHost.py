# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import binascii
import getpass
import logging
import os
import paramiko.client
import paramiko.pkey
from paramiko.ssh_exception import PasswordRequiredException
import socket
import sys

from scap.host.CLIHost import CLIHost
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class SSHHost(CLIHost):
    SSH_TIMEOUT = 3

    class AskHostKeyPolicy(paramiko.client.MissingHostKeyPolicy):
        def missing_host_key(self, client, hostname, key):
            fpt = key.get_fingerprint()
            logger.debug('Fingerprint: ' + str(fpt))
            hex_fpt = str(binascii.hexlify(fpt), encoding='utf-8')
            logger.debug('Hex Fingerprint: ' + hex_fpt)
            response = input('Accept key ' + hex_fpt + ' for host ' + hostname + ' (Y/n)? ')
            if response == '' or response.lower()[0] == 'y':
                logger.debug('Adding key for host ' + hostname)
                host_keys = client.get_host_keys()
                host_keys.add(hostname, key.get_name(), key)
                if not os.path.exists(os.path.expanduser('~/.pyscap')):
                    try:
                        os.mkdir(os.path.expanduser('~/.pyscap'))
                        logger.debug('Created ~/.pyscap')
                    except:
                        logger.warning('Could not create directory ~/.pyscap')
                        return
                try:
                    host_keys.save(os.path.expanduser('~/.pyscap/ssh_host_keys'))
                    logger.debug('Saved ~/.pyscap/ssh_host_keys')
                except:
                    logger.warning("Couldn't save ssh host keys")
                return
            else:
                raise RuntimeError('Key for ' + hostname + ' not accepted')

    def connect(self):
        self.client = paramiko.client.SSHClient()
        self.client.load_system_host_keys()
        try:
            # TODO windows/linux home instead of ~
            logger.debug('Read ssh host keys from ~/.pyscap/ssh_host_keys')
            self.client.load_host_keys(os.path.expanduser('~/.pyscap/ssh_host_keys'))
        except:
            logger.warning("Couldn't read ssh host keys")
        self.client.set_missing_host_key_policy(self.AskHostKeyPolicy())

        inventory = Inventory()

        if inventory.has_option(self.hostname, 'ssh_port'):
            port = inventory.get(self.hostname, 'ssh_port')
        else:
            port = 22

        if inventory.has_option(self.hostname, 'ssh_username') and inventory.has_option(self.hostname, 'ssh_password'):
            self.client.connect(self.hostname, port=port,
                username=inventory.get(self.hostname, 'ssh_username'),
                password=inventory.get(self.hostname, 'ssh_password'))
        elif inventory.has_option(self.hostname, 'ssh_private_key_filename'):
            if inventory.has_option(self.hostname, 'ssh_private_key_file_password'):
                self.client.connect(self.hostname, port=port,
                    key_filename=inventory.get(self.hostname, 'ssh_private_key_filename'),
                    password=inventory.get(self.hostname, 'ssh_private_key_file_password'))
            else:
                try:
                    self.client.connect(self.hostname, port=port,
                        key_filename=inventory.get(self.hostname, 'ssh_private_key_filename'))
                except PasswordRequiredException:
                    # retry with password
                    ssh_private_key_file_password = getpass.getpass('Password for private key file ' +
                        inventory.get(self.hostname, 'ssh_private_key_filename') + ': ')
                    self.client.connect(self.hostname, port=port,
                        key_filename=inventory.get(self.hostname, 'ssh_private_key_filename'),
                        password=ssh_private_key_file_password)
        else:
            ssh_username = input('Username for host ' + self.hostname + ': ')
            if ssh_username.strip() == '':
                raise RuntimeError('No method of authenticating with host ' + self.hostname + ' found')
            ssh_password = getpass.getpass('Password for host ' + self.hostname + ': ')
            self.client.connect(self.hostname, port=port, username=ssh_username, password=ssh_password)

        from scap.collector.UNameCollector import UNameCollector
        UNameCollector(self, {}).collect()

        if self.facts['uname']['kernel_name'] == 'Linux':
            self.facts['oval_family'] = 'linux'
        # elif uname.startswith('Darwin'):
        #     TODO
        elif self.facts['uname']['kernel_name'] == 'Windows NT':
            self.facts['oval_family'] = 'windows'
        else:
            raise NotImplementedError('Host detection has not been implemented for uname: ' + self.facts['uname'] + ' on ' + self.hostname)

    def _send_stdin(self, chan, data):
        try:
            chan.send(self.sudo_password + "\n")
        except socket.timeout:
            pass

    def exec_command(self, cmd):
        inventory = Inventory()
        cmd = 'sh -c "' + cmd.replace('"', r'\"') + '"'

        logger.debug("Sending command: " + cmd)
        chan = self.client.get_transport().open_session()
        chan.exec_command(cmd)
        chan.settimeout(self.SSH_TIMEOUT)

        self._cmd_out_buf = ''
        self._cmd_err_buf = ''
        while True:
            if chan.recv_ready():
                try:
                    self._recv_stdout(chan.recv(1024).decode())
                except socket.timeout:
                    pass

            if chan.recv_stderr_ready():
                try:
                    self._recv_stderr(chan.recv_stderr(1024).decode())
                except socket.timeout:
                    pass

            if chan.exit_status_ready():
                try:
                    self._recv_stdout(chan.recv(1024).decode())
                except socket.timeout:
                    pass
                try:
                    self._recv_stderr(chan.recv_stderr(1024).decode())
                except socket.timeout:
                    pass
                break

        status = chan.recv_exit_status()

        chan.close()

        out_lines = str.splitlines(self._cmd_out_buf)
        out_lines = [line.strip('\x0A\x0D') for line in out_lines]

        err_lines = [line.strip('\x0A\x0D') for line in str.splitlines(self._cmd_err_buf)]
        err_lines = [line.strip('\x0A\x0D') for line in err_lines]

        return (status, out_lines,err_lines)

    def disconnect(self):
        self.client.close()
