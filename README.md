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

* --help
* --version
* --output
* --inventory
* --host
* --list-hosts
* --parse
* --detect
* --collect
    * --content
* --benchmark
    * --content
