atmpin=2000
bal=50000
pin=input("enter a pin")
if atmpin == 2000:
	print('select 1 for eng\n')
	print('select 2 for withdrawl\n')
	print('select 3 for deposit\n')
	print('select 4 for exit\n')
	x=input('')
	if x==1:
		print('Your balance')
		print(bal)
	elif x==2:
		print('enter the amount you want to withdrawl')
		y=input('')
		if y>bal:
			print('wrong input')
		else:
			bal=bal-y
			print('your balance is')
			print(bal)
	elif x==3:
		print('enter the amount you want to deposit')
		y=input('')
		if y<0:
			print('wrong input')
		else:
			bal=bal+y
			print('your balance is')
			print(bal)
	elif x==4:
		print('')
	else:
		print('wrong input')
else:
	print('wrongpin try later')

