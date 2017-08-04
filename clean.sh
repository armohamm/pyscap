#!/bin/bash

find scap -name '*.pyc' -delete
find test -name '*.pyc' -delete
rm -f *.pem
(
    cd agent
    bash clean.sh
)
