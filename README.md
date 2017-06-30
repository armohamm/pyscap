# pyscap
Python implementation of a Security Content Automation Protocol compatible Configuration, Vulnerability, Patch and Inventory Scanner

Requires Python 3.5 or greater. See the requirements.txt file for addition required packages that can be installed using pip -r

Usage
=====

    pyscap.py
        [--help or -h]
        [--version or -V]
        [--verbose or -v]
        [--output [OUTPUT] or -o [OUTPUT]]
        [--inventory INVENTORY [INVENTORY ...]]
        [--host HOST [HOST ...]]
        --list-hosts
        | --parse CONTENT [CONTENT ...]
        | --detect
        | --collect --content CONTENT [--content CONTENT [...]]
        | --benchmark
            --content CONTENT [--content CONTENT [...]]
            [--data_stream DATA_STREAM]
            [--checklist CHECKLIST]
            [--profile PROFILE]
            [--pretty]

Options
-------

* --help

    Prints a help message
    
* --version

    Prints the version of pyscap

* --output

    Configures the location where output is sent for the various operations

* --inventory

    Specifies the location of an (ini formatted) inventory file.

* --host

    Specifies a host to target

Operations
----------

* --list-hosts

    List the hosts that would be targeted

* --parse
    Parse the specified file

* --detect
    Do basic detection on the specified host(s)

* --collect
    Collect system characteristics about the specified host(s)

    * --content
        Specifies the content to use for system characteristic collection

* --benchmark

    Benchmarks a host against a checklist (unless there's only one).

    * --content

        Specifies the content to use for benchmarking.

    * --data_stream

        If a data stream collection is used, the data_stream must also be specified (required unless there's only one).

    * --checklist

        Used to specify checklist (required unless there's only one).

    * --profile

        Used to specify profile (required unless there's only one).

    * --pretty

        Beautify the output generated to make it easier to read by human eyes.
