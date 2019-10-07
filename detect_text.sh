#!/bin/bash

# This generates a file every 5 minutes

while true; do
time ./detect_text.py >> ./detect_text.log
sleep 10
done
