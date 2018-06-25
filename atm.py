atmpin=4444
bal=5000
name=input("\nEnter Your name : ")
print("Hello ",name," !")
pin=int(input("Enter your pin : "))
if atmpin == pin :
	print('Login Successful! \n\n\t  **** welcome **** \n')
	while 1:
			print('\t----------------------')
			print('\t|       MENU         |')
			print('\t----------------------')
			print('\t|     1) ENQUIRY     |')
			print('\t----------------------')
			print('\t|     2) WITHDRAWAL  |')
			print('\t----------------------')
			print('\t|     3) DEPOSIT     |')
			print('\t----------------------')
			print('\t|     4) EXIT        |')
			print('\t----------------------')
			x=int(input(''))
			if x==1:
				print('Your Current Balance is :',bal,'\n\n')
			elif x==2:
				print('Enter the amount you want to withdraw :')
				y=int(input(''))
				if y>bal:
							print("Sorry, Insufficient Funds !")
				else:
						bal=bal-y
						print('Your Current Balance is : ',bal,'\n\n')
			elif x==3:
					print('Enter the amount you want to deposit :')
					y=int(input(''))
					bal=bal+y;	
					print('Your Current Balance is : ',bal,'\n\n')		
			elif x==4:
					print('Thanks for visiting....!\n\n')
					break
			else:
					print("Oops..! Wrong Input \n\n")
					break
else:
	print("Oops..! Wrong Pin \n\n")



