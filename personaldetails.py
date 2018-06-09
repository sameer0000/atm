class urdetails():
	def __init__(self,name,age,gender):
		self.name=name
		self.age=age
		self.gender=gender
		print("Your Details Are")
		print("Name:",self.name,"\n","Age:",self.age,"\n","Gender:",self.gender)	
	def bmical(self):
        	height=float(input("Input your height in metes: "))
        	weight=float(input("Input your weight in kilograms: "))
        	print("your body mass index is: ",round(weight/(height * height), 2))
print("HELLO!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("WELCOME THIS IS YOUR HEALTH CARE ASSISTANT")
print("Can I ask you some personal details")
a=raw_input("Tell me ur Name: ")
b=input("Tell me ur Age: ")
c=raw_input("Are u a male or a female:")
if c=="male" or c=="female":
	x=urdetails(a,b,c)
	x.bmical()
else:
	print ("Enter ur correct gender")
