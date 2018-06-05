def verify_pin(pin):
	if pin == '2222':
		return True	
	else:
		return False
def log_in():
	tries = 0
	while tries < 4:
		pin=input('enter your 4 digit pin: ')
		if verify_pin(pin):
			print("pin accepted!")
			return True
		else:
			print("invalid pin")
			tries  += 1
	print("to many incorrect tries. could not log in")
	return False
def start_menu():
	print("welcome to the atm!")
	if log_in():
		# you will need to make this one yourself!
		main_menu()
	print("exiting program")
stsrt_menu()		
