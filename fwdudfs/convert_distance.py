@outputSchema("m_traffic: {(year:int, miles:float, vans:float, trucks:float)}")

def to_miles(km_traffic):

	year, kms, vans, trucks = km_traffic.split(' ')

	miles = float(kms)*0.62

	return int(year), miles, float(vans), float(trucks)


@outputSchema("k_traffic: {(year:int, kms:float, vans:float, trucks:float)}")
def to_kms(mile_traffic):

	year, miles, vans, trucks = km_traffic.split(' ')

	kms = float(kms)*1.6

	return int(year), kms, float(vans), float(trucks)
