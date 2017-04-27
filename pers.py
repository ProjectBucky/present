#!/usr/bin/python
import re
import csv

likes={}
dislikes={}
user={}
line = ""
for key, val in csv.reader(open("likes.csv")):
    likes[key] = val
for key, val in csv.reader(open("dislikes.csv")):
    dislikes[key] = val
for key, val in csv.reader(open("user.csv")):
    user[key] = val

while True:

	line = input()

	if (line=="stop"):
		break
	
	searchObj = re.search( r'(.*) is my (best|favourite) (.*)', line, re.M|re.I)
	if searchObj:	
		print ("searchObj.group() : ", searchObj.group())
		print ("searchObj.group(1) : ", searchObj.group(1))
		print ("searchObj.group(2) : ", searchObj.group(2))
		print ("searchObj.group(3) : ", searchObj.group(3))
		likes[searchObj.group(3)]=searchObj.group(1)
		continue

	searchObj= re.search( r'my (best|favourite) (.*) is (.*)', line, re.M|re.I)
	
	if searchObj:	
		print ("searchObj.group() : ", searchObj.group())
		print ("searchObj.group(1) : ", searchObj.group(1))
		print ("searchObj.group(2) : ", searchObj.group(2))
		print ("searchObj.group(3) : ", searchObj.group(3))
		likes[searchObj.group(2)]=searchObj.group(3)
		continue

	searchObj= re.search( r'i (like|love) (.*) (.*)', line, re.M|re.I)
	
	if searchObj:	
		print ("searchObj.group() : ", searchObj.group())
		print ("searchObj.group(1) : ", searchObj.group(1))
		print ("searchObj.group(2) : ", searchObj.group(2))
		print ("searchObj.group(3) : ", searchObj.group(3))
		likes[searchObj.group(3)]=searchObj.group(2)
		continue	
		
	searchObj = re.search( r'i (hate|donot like| don\'t like|dont like) (.*) (.*)', line, re.M|re.I)

	if searchObj:
		print ("searchObj.group() : ", searchObj.group())
		print ("searchObj.group(1) : ", searchObj.group(1))
		print ("searchObj.group(2) : ", searchObj.group(2))
		print ("searchObj.group(3) : ", searchObj.group(3))
		dislikes[searchObj.group(3)]=searchObj.group(2)
		continue

	searchObj = re.search( r'my (name) is (.*)', line, re.M|re.I)
	if searchObj:	
		print ("searchObj.group() : ", searchObj.group())
		print ("searchObj.group(1) : ", searchObj.group(1))
		print ("searchObj.group(2) : ", searchObj.group(2))
		user[searchObj.group(1)]=searchObj.group(2)
		continue


	searchObj = re.search( r'my (.*)\'s name is (.*)', line, re.M|re.I)
	if searchObj:	
		print ("searchObj.group() : ", searchObj.group())
		print ("searchObj.group(1) : ", searchObj.group(1))
		print ("searchObj.group(2) : ", searchObj.group(2))
		user[searchObj.group(1)]=searchObj.group(2)
		continue		

	searchObj = re.search( r'my (.*) is (.*)', line, re.M|re.I)
	if searchObj:	
		print ("searchObj.group() : ", searchObj.group())
		print ("searchObj.group(1) : ", searchObj.group(1))
		print ("searchObj.group(2) : ", searchObj.group(2))
		user[searchObj.group(1)]=searchObj.group(2)
		continue	


w = csv.writer(open("likes.csv", "w"))
for key, val in likes.items():
    w.writerow([key, val])	

w = csv.writer(open("dislikes.csv", "w"))
for key, val in dislikes.items():
    w.writerow([key, val])

w = csv.writer(open("user.csv", "w"))
for key, val in user.items():
    w.writerow([key, val])    	    
 
print (likes)
print (dislikes)
print (user)