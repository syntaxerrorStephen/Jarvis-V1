import webbrowser
import string
import speech_recognition as sr

# obtain audio 
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hi I'm Jarvis a simple virtual assitant made by Stephen Flynn")
    audio = r.listen(source)
    

if "weather" in r.recognize_google(audio): 
    # obtain audio from the microphone
    r3 = sr.Recognizer()
    url3 = 'https://www.timeanddate.com/weather/ireland/'
    with sr.Microphone() as source:
        print("What County?")
        audio3 = r3.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r3.recognize_google(audio3))
            webbrowser.open_new(url3+r3.recognize_google(audio3))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e))


if "directions" in r.recognize_google(audio):
    # obtain audio from the microphone
    r4 = sr.Recognizer()
    url4 = 'https://www.google.ie/maps/place/'
    with sr.Microphone() as source:
        print("Where would you like to go today?")
        audio4 = r4.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r4.recognize_google(audio4))
            webbrowser.open_new(url4+r4.recognize_google(audio4))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e))

if "search" in r.recognize_google(audio):
    # obtain audio from the microphone
    r5 = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("what website would you like me to search for you? ")
        audio5 = r5.listen(source)
        url5= r5.recognize_google(audio5)

        try:
            print("Google Speech Recognition thinks you said " + r5.recognize_google(audio5))
            webbrowser.open_new('https://'+url5+'.com')
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

if "food" in r.recognize_google(audio): 
    # obtain audio from the microphone
    r6 = sr.Recognizer()
    url6 = 'https://www.just-eat.ie/area/rush-co-dublin/'
    with sr.Microphone() as source:
        print("What'd you like to eat?")
        audio6 = r6.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r6.recognize_google(audio6))
            webbrowser.open_new(url6+r6.recognize_google(audio6))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e))
