def leap_year(year):
	y=int(year)
	if ((y%400==0) or ((y%4==0) and (y%100!=0))):
		return "%s is Leap year"%y
	else:
		return "%s is not a Leap year"%y

print(leap_year(input("Enter a Year : ")))