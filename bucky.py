import speech_recognition as sr
#import wolframalpha
from reply import * 
 

r = sr.Recognizer()
m = sr.Microphone()
s=""
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        play_wav('ready.wav')
        print("I'm Listening!")

        with m as source: audio = r.listen(source)
        play_wav('gotit.wav')
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            #print value   #added by abhi

            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))




            s+=value+'.'
            print(s)
            #voice("You said {}".format(value))
            reply(value)


            # we need some special handling here to correctly print unicode characters to standard output
            
        except sr.UnknownValueError:
            voice("Sorry! I couldn't understand")
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            voice("Sorry! Some error occured. Please check the internet connection!")
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        except KeyError:
            pass    
            
except KeyboardInterrupt:
    pass