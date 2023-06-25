#!/usr/bin/env python3
import re
import csv

per_user = {}
per_test = []
error = {}
file = "x_syslog.log"
reg = r"ERROR ([\w. ']*)\(([\w. ]*)\)"
with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        result = re.search(reg, line)
        if result != None and result not in per_test:
            per_test[]
