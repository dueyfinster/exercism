def is_armstrong_number(number):
	length = len(str(number))
	if number == number**length:
		return True
	elif length > 1:
		res = 0
		for c in list(str(number)):
			res += int(c) ** length
		if res == number:
			return True
			
	return False
