import re

def calculate(operator,op1,op2):
	if operator=='+':
		return float(op1)+float(op2)
	elif operator=='-':
		return float(op1)-float(op2)
	elif operator=='*':
		return float(op1)*float(op2)
	elif operator=='/':
		return float(op1)/float(op2)
	elif operator=='**':
		return	float(op1)**float(op2)

str="calculate 2 raised to the power 8"
# calculate|what is|compute 2 to the power|to the power of 8
searchObj=re.search( r'(.*) (.*) (to the power of|to the power) (.*)', str, re.M|re.I)
print ("searchObj.group(1) : ", searchObj.group(1))
print ("searchObj.group(2) : ", searchObj.group(2))
print ("searchObj.group(3) : ", searchObj.group(3))

if searchObj:
	print calculate('**',searchObj.group(2),searchObj.group(4))
else:
	# calculate|what is|compute 2 to the power|to the power of 8
	searchObj=re.search( r'(.*) (.*) (raised to the power of|raised to the power) (.*)', str, re.M|re.I)
	print ("searchObj.group(1) : ", searchObj.group(1))
	print ("searchObj.group(2) : ", searchObj.group(2))
	print ("searchObj.group(3) : ", searchObj.group(3))
	if searchObj:
		print calculate('**',searchObj.group(1),searchObj.group(3))	
	else:
		searchObj=re.search( r'(.*) (power) (.*)', str, re.M|re.I)
		if searchObj:
			print calculate('**',searchObj.group(1),searchObj.group(3))
		else:
			pass
					

		