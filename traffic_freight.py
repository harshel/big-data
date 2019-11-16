import sys
import string

while True:
	line = sys.stdin.readline()
	if not line:
		break
	
	row = string.strip(line, "\n")
	year, cp, aj, bj, length, cycles, bikes, cars, buses, vans, trucks = string.split(row, ",")
	total_freight = float(cycles) + float(bikes) + float(cars) + float(buses) + float(vans) + float(trucks)
	print ",".join([year,cp,aj,bj,length,str(total_freight)])
