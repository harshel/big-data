#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
	line = line.strip()
	year, cp, aj, bj, length, cycle, bike, car, bus, van, truck = line.split(",")
	print year
