#Michael Esposito
#Computer Network Defense
#CSCI 6542
#1/26/17
#Temperature Converter.py

print "Temperature Converter"
while True:
	temp = raw_input("Enter a temperature: ")
	try:
		temp = float(temp)
	except ValueError:
		print "Invalid input, please try again"
		continue
	tempScale = raw_input("Convert to (F)ahrenheit or (C)elsius? ")
	if tempScale is "F" or tempScale is "f" or tempScale is "C" or tempScale is "c":
		pass
	else:
		print "Invalid input, please try again"
		continue
	#Convert to Fahrenheit
	if tempScale is "F" or tempScale is "f":
		frac = float(9)/5
		tF = frac * temp + 32
		print temp, " C = ", tF, " F"
		break
	#Convert to Celsius
	else:
		frac = float(5)/9
		tC = frac * (temp - 32)
		print temp, " F = ", tC, " C"
		break