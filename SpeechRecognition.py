import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()      #creating engine variable
rate = engine.getProperty("rate")
engine.setProperty("rate", 120) #setting the rate of speech

r = sr.Recognizer()           #creating object of recognizer class
with sr.Microphone() as source:  #using microphone as source for the speech
    print("Listening...")
    r.pause_threshold = 1      #setting a pause in speech to 1 sec
    audio = r.listen(source)   #obtaining audio file from source speech

try:
    print("recognizing..")
    text = r.recognize_google(audio) #using google api to convert audio file in text format
    engine.say(text)                 #using same text to listen what was in the text  
    print(f"you said : {text} ")
    engine.runAndWait()

except:
    print("sorry could not recognize")