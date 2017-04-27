from utilities import *

def read_diary(day=time.strftime('%d'),month=time.strftime('%m'),year=time.strftime('%Y')):
	try:
		filename="diary/"+day+"_"+month+"_"+year+".wav1"
		play_wav(filename)
	except IOError:
		voice("Oops! Couldnot find, a diary entry, for,this date!")

read_diary('22','07','2017')	
