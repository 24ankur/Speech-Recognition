import pyttsx3

engine = pyttsx3.init()      #engine variable for function to run it

rate = engine.getProperty('rate')  #setting the rate of pronunciation
engine.setProperty("rate", 120)

engine.say("hello world")
engine.runAndWait()