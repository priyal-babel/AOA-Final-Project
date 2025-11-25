#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: sh run.sh <input_file>"
    exit 1
fi

python3 string_gen.py "$1"
echo "Output written to actual_input.txt"
