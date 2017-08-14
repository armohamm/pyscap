#!/bin/bash

find src -name '*.pyc' -delete
find tests -name '*.pyc' -delete
rm -f *.pem
(
    cd src/agent
    bash clean.sh
)
