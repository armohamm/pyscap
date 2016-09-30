#!/usr/bin/env python

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

import socket
import os
import datetime

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509, utils
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID


ca_hostname = socket.gethostbyaddr(socket.gethostname())[0]
agent_hostname = socket.gethostbyaddr(socket.gethostname())[0]
scanner_hostname = socket.gethostbyaddr(socket.gethostname())[0]

# Generate our ca key
ca_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Write our key to disk for safe keeping
with open("ca_key.pem", "wb") as f:
    f.write(ca_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

def random_serial_number():
    return utils.int_from_bytes(os.urandom(20), "big") >> 1

# Various details about who we are. For a self-signed certificate the
# subject and issuer are always the same.
issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, ca_hostname),
])
subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, ca_hostname),
])

ca_cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    ca_key.public_key()
).serial_number(
    # x509.random_serial_number()
    random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.utcnow() + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(ca_hostname)]),
    critical=False,
).add_extension(
    x509.BasicConstraints(ca=True, path_length=None),
    critical=True,
).add_extension(
    x509.KeyUsage(
        False, # digital_signature
        False, # content_commitment
        False, # key_encipherment
        False, # data_encipherment
        False, # key_agreement
        True, # key_cert_sign
        False, # crl_sign
        False, # encipher_only
        False, # decipher_only
    ),
    critical=False,
# Sign our certificate with our private key
).sign(ca_key, hashes.SHA256(), default_backend())

# Write our certificate out to disk.
with open("ca_cert.pem", "wb") as f:
    f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

# Generate our agent key
agent_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Write our key to disk for safe keeping
with open("agent_key.pem", "wb") as f:
    f.write(agent_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, agent_hostname),
])

agent_cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    agent_key.public_key()
).serial_number(
    # x509.random_serial_number()
    random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.utcnow() + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(agent_hostname)]),
    critical=False,
).add_extension(
    x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]),
    critical=False,
# Sign our certificate with our private key
).sign(ca_key, hashes.SHA256(), default_backend())

with open("agent_cert.pem", "wb") as f:
    f.write(agent_cert.public_bytes(serialization.Encoding.PEM))
    f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

# Generate our scanner key
scanner_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Write our key to disk for safe keeping
with open("scanner_key.pem", "wb") as f:
    f.write(scanner_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, scanner_hostname),
])

scanner_cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    scanner_key.public_key()
).serial_number(
    # x509.random_serial_number()
    random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.utcnow() + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(scanner_hostname)]),
    critical=False,
).add_extension(
    x509.ExtendedKeyUsage([ExtendedKeyUsageOID.CLIENT_AUTH]),
    critical=False,
# Sign our certificate with our private key
).sign(ca_key, hashes.SHA256(), default_backend())

with open("scanner_cert.pem", "wb") as f:
    f.write(scanner_cert.public_bytes(serialization.Encoding.PEM))
    f.write(ca_cert.public_bytes(serialization.Encoding.PEM))
