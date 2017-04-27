import time
import pyttsx
import pyaudio  
import wave 

def speak(arg):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-5)
    engine.say(arg)
    engine.say("   ")
    engine.runAndWait()

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        secs=mins*60+secs
        if(secs >= 50 and secs %10==0):
            speak(secs)
        elif secs<10:
            speak(secs)
            time.sleep(.4)
                
        elif secs < 50:
            speak(secs)

        
        else:
            time.sleep(1)
        t -= 1
    chunk = 1024 
    f = wave.open(r"alarm.wav","rb")
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
    speak("Time up")      
countdown(5) 


