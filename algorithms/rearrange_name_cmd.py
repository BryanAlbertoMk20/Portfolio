#!/usr/bin/env python3

import re
import sys

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)", name)
    return "{} {}".format(result[2], result[1])

name1 = sys.argv[1]

print(rearrange_name(name1))