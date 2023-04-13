import pyttsx3 as pi
engine=pi.init()

voice=engine.getProperty('rate')

voice=voice-125

engine.setProperty('volume',0.4)
engine.setProperty('rate',50)


engine.say("i love you")
engine.runAndWait()
'''print(voice)
volume=engine.getProperty('volume')
volume=volume-60
engine.setProperty('volume',volume)
engine.runAndWait()'''