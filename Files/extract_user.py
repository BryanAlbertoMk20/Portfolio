#!/usr/bin/env python3

import sys
import re

logfile = "sample.txt"
with open(logfile) as file:
    for line in file:
        pattern = r"\((\w+)\)$"
        result = re.search(pattern, line)
        if "INFO" in line:
            print(line)



