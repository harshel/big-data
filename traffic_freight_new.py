import sys
import string

while True:
	line = sys.stdin.readline()
	if not line:
		break
	
	row = string.strip(line, "\n")
	print row
	year, cp, aj, bj, length, cycles, bikes, cars, buses, vans, trucks = string.split(row, "\t")
	print year
	total_freight = float(cycles) + float(bikes) + float(cars) + float(buses) + float(vans) + float(trucks)
	print total_freight
	print "\t".join([year,cp,aj,bj,length,str(total_freight)])
