#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("New file created\n")
    print(f"The file {filename} has been created!")
else:
    print(f"Error, the file {filename} already exists!")
    sys.exit(1)
