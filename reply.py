from utilities import *  
from questions import * 
from jokes_and_quotes import * 
import re

def reply(str):
    if (str in ask_time):
        voice(tell_time())
    elif (str in who_are_you):
        voice("I am Bucky, the new age personal assistant")
    elif (str in greetings):
        voice("hello, nice to meet you")
    elif (str in about_creators):
        voice("i was created by those 4 people standing next to you")
    elif (str in how_are_you):
        voice("i'm doing fine, thanks how are you ")
    elif (str in where_are_you):
        voice("I am probably inside someone's computer")    
    elif (str in about_skills):
        voice("i can recognize and carry out basic voice commands, monitor your expenses, search internet for you, and much more!")
    elif (str in ask_date):
    	voice(tell_date())
    elif (str in ask_jokes):
        voice(tell_jokes())
    elif (str in ask_quotes):
        voice(tell_quotes())  
    elif (str in write_diary):
        diary_entry()          
    else:

        
		#to call calculator
        try:

            searchObj=re.search( r'(.*) of (.*) and (.*)', str, re.M|re.I)
            if searchObj:

                if(searchObj.group(1) in['sum','add']):
                    voice(float(searchObj.group(2))+float(searchObj.group(3)))

                elif(searchObj.group(1) in['subtract','difference']):
                    voice(float(searchObj.group(2))-float(searchObj.group(3)))

                elif(searchObj.group(1) in['product','multiplication']):
                    voice(float(searchObj.group(2))*float(searchObj.group(3)))

                elif(searchObj.group(1) in['quotient','division','ratio']):
                    voice(float(searchObj.group(2))/float(searchObj.group(3)))

            searchObj = re.search( r'(.*) (.*) of (.*) and (.*)', str, re.M|re.I)
            if searchObj:

                if(searchObj.group(2) in['sum','add']):
				    voice(float(searchObj.group(3))+float(searchObj.group(4)))

                elif(searchObj.group(2) in['subtract','difference']):
				    voice(float(searchObj.group(3))-float(searchObj.group(4)))

                elif(searchObj.group(2) in['product','multiplication']):
				    voice(float(searchObj.group(3))*float(searchObj.group(4)))

                elif(searchObj.group(2) in['quotient','division','ratio']):
                    voice(float(searchObj.group(3))/float(searchObj.group(4)))
		
		# to call countdown timer
				
            searchObj = re.search( r'(countdown|countdown timer|timer|countdown for|timer for|countdown timer for) (.*) (.*)', str, re.M|re.I)
            if searchObj:
                
                countdown(searchObj.group(2),searchObj.group(3))
            searchObj = re.search( r'(countdown|countdown timer|timer|countdown for|timer for|countdown timer for) (.*)', str, re.M|re.I)	
            if searchObj:
                
                countdown(searchObj.group(2))

		    #to call tell day or yesterday or tomorrow
            searchObj = re.search( r'(what day is|what day was|what is the day|what was the day) (.*)', str, re.M|re.I)
            if searchObj:
				if(searchObj.group(2)=="today"):
					tell_day()
				elif (searchObj.group(2)=="yesterday"):
					tell_day(int(time.strftime('%d'))-1)	
				elif (searchObj.group(2)=="tomorrow"):
					tell_day(int(time.strftime('%d'))+1)
                   		
				
		#make code for custom dates

        #to call dictionary
            searchObj = re.search( r'(define|what is the meaning of|meaning of|what is meaning of|who is|google) (.*)', str, re.M|re.I)

            if searchObj:
                dictionary(searchObj.group(2))
            searchObj = re.search( r'(what does the word|what does) (.*) (means|mean)', str, re.M|re.I)
            if searchObj:
                dictionary(searchObj.group(2))  

        #to play diary
            searchObj = re.search( r'(play diary|read diary) (on|of) (.*) (.*) (.*)', str, re.M|re.I)

            if searchObj:
                play_diary(searchObj.group(3),searchObj.group(4),searchObj.group(5))
              
        #add code to play more general dates

        except AttributeError:
            voice("Sorry. something error, has occured!")
        except ValueError:
			voice("Sorry. something went wrong!")

            
'''

     (str=="i love you"):
        voice("I love you too handsome")
    elif (str=="go to hell"):
        voice("perhaps i have already been there")
    
    elif (str=="search *"):
        voice("okay what do you want to search")
    elif (str=="check notifications"):
        voice("you have no new notelifications")
    elif (str=="music"):
        voice("A husband and wife stepped up to view the body of his mother-in-law. As he began to cry, his wife punched him and said: Why are you crying, you never liked my mother anyway. I know he replied, I thought I saw her move!")
    elif (str=="who am i"):
        voice("i'm sorry, what is your name")
    elif (str=="what is my name"):
        voice("i'm sorry, what is your name")
    elif (str=="how is the weather"):
        voice("32 degree celcius with chances of rain")
    elif (str=="set a reminder"):
        voice("ok, what should i remind you of")
    elif (str=="count to 10"):
        voice("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    elif (str=="toss a coin"):
        import random
        x = random.randint(0,1)
        if (x==0):
            voice "Head"
        else:
            voice "Tail"
    elif (str=="im confused"):
        voice("lets toss a coin")
    elif (str=="i am sad"):
        voice("hi sad, my name is Bucky ha ha ha")
    elif (str==""):
        voice("I am Bucky, the new age personal assitant")
    else:
        voice("Nothing to say")
        voice("Nothing  ")
        #client = wolframalpha.Client("K9RLXP-GKPWYPR92J")
        #res = client.str(str)
        #voice(next(res.results).text)
'''

