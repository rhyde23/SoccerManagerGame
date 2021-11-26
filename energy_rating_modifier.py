def adjust_for_energy(rating, significance_percentage, energy) :
	return int(((rating*(significance_percentage/100))*(energy/100))+(rating*((100-significance_percentage)/100)))
