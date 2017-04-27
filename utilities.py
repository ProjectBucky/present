import random
import pyttsx
import pyaudio  
import wave
import time
from jokes_and_quotes import *
        
def voice (str):
    engine = pyttsx.init()
    engine.say(str)
    engine.runAndWait()

def play_wav(filename):
	try:

		chunk = 1024 
		f = wave.open(filename,"rb")
		p = pyaudio.PyAudio()
		stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)
		data = f.readframes(chunk) 
		while data:  
			stream.write(data)  
			data = f.readframes(chunk)
		stream.stop_stream()  
		stream.close()
		p.terminate()
	except IOError:
		voice("Sorry. I could not find that file!")	

def roll_dice():
	dice_val = random.randint(1,7)
	voice(dice_val) 

def toss_coin():
	toss_val=random.randint(0,2)
	if toss_val==1:
		voice("Heads")
	else:
		voice("Tails")
		
def tell_jokes():
	joke_val=random.randint(0,6)
	voice(jokes[joke_val])

def tell_quotes():
	quote_val=random.randint(0,10)
	voice(quotes[quote_val])
	
def tell_time():
	return time.strftime('%I, %M , %p !')

def tell_date():
	return time.strftime('%B, %e. %Y, %A')

def tell_day(day=time.strftime('%d'),month=time.strftime('%m'),year=time.strftime('%Y')):
	import calendar
	day_names={0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
	x=calendar.weekday(int(year),int(month),int(day))
	voice(day_names[x])

'''
def speak(arg):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-5)
    engine.say(arg)
    engine.say("   ")
    engine.runAndWait()
'''
def countdown(t,unit="second"):
	t=int(t)
	if (unit in['minutes','mins','min']):
		t=t*60
	while t:
        
		if(t >= 50 and t %10==0):
			voice(t)
		elif t<10:
			voice(t)
			time.sleep(.4)
                
		elif t < 50:
			voice(t)
			time.sleep(.2)        
		else:
			time.sleep(1)
		t -= 1
	play_wav('alarm.wav')    
	voice("Time up")         

def calculate(operator,op1,op2):
	if operator=='+':
		return float(op1)+float(op2)
	elif operator=='-':
		return float(op1)-float(op2)
	elif operator=='*':
		return float(op1)*float(op2)
	elif operator=='/':
		return float(op1)/float(op2)	

def dictionary(word):
	import urllib2
	import re
	word='+'.join(word.split(" "))
	url = "https://www.google.co.in/search?q=define+"+word
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

	req = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(req)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'html.parser')
	definitions= re.sub(r'\\[^\\]*\\ [0-9][a-z] :','',(re.sub(r'\([^)]*\)', '', soup.find("span",class_='st').text)))
	voice(definitions) 


def diary_entry():
	import speech_recognition as sr
	day=time.strftime('%d')
	month=time.strftime('%m')
	year=time.strftime('%Y')
	filename="diary/"+day+"_"+month+"_"+year+".wav"
	r = sr.Recognizer()
	m = sr.Microphone()
	r.pause_threshold = 3

	try:
    
		with m as source: r.adjust_for_ambient_noise(source)
		print("Set minimum energy threshold to {}".format(r.energy_threshold))

		while True:
			voice("I,m all set to write your diary. Please start talking!")
			with m as source: audio = r.listen(source)
			print("Got it! Now to saving it...")
			voice("Got it!.. I'm saving it...")
			try:
            # recognize speech using Google Speech Recognition
            
				with open(filename, "wb") as f:

					f.write(audio.get_wav_data())
            
            # we need some special handling here to correctly print unicode characters to standard output
				r.pause_threshold = .8
				voice("Your diary is. successfully, saved!")
				return
			except ValueError:
				voice("Sorry! some error has occured.")
				return
	except ValueError:
		voice("Sorry! some error has occured.")	
		return

def play_diary(day,month,year):
	month_names={'january':'01','february':'02','march':'03','april':'04','may':'05','june':'06','july':'07','august':'08','september':'09','october':'10','november':'11','december':'12'}
	month=month_names[month.lower()]
	
	filename="diary/"+day+"_"+month+"_"+year+".wav"
	play_wav(filename)