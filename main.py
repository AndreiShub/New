def lucky(x):
	summ1 = 0
	summ2 = 0
	x = str(x)
	if len(x) < 6 or len(x) > 6:
		raise ValueError
	for i in x[:3]:
		summ1 += int(i)
	for i in x[3:]:
		summ2 += int(i)
	if summ1 == summ2:
		return True
	else:
		return False


print(lucky(611125))
