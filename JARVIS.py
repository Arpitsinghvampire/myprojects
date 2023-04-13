from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
engine=pyttsx3.init()
#voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[0].id)
activationWord='jarvis'
chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
def search_wikipedia(query=' '):
    search_results=wikipedia.search(query)
    if not search_results:
        speak("not found master")
    try:
        wikipage=wikipedia.page(search_results[0])
    except wikipedia.DisambiguationError as error:
        wikipage=wikipedia.page(error.options[0])
    print(wikipage.title)
    wikisummary=str(wikipage.summary)
    return wikisummary
def speak(text,rate=100):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener=sr.Recognizer()
    print("LISTENING FOR COMMAND")
    with sr.Microphone() as source:
        listener.pause_threshold=1
        input_speech=listener.listen(source)
    try:
        print("RECOGNIZING SPEECH .......")
        query=listener.recognize_google(input_speech,language='en_ind')
        print(f'the input speech was :{query}')
    except Exception as exception:
        speak("SORRY COULD NOT CATCH THAT")
        print(exception)
        return 'NONE'

    return query

if __name__=='__main__':
    speak("enter the activation code")
    while(True):
        query=parseCommand().lower().split()
        if query[0]==activationWord:
            query.pop(0)
            speak(" hello ARPIT WHAT'S FOR TODAY")
        if(query[0]=='say'):
            if 'hello' in query:
                speak('GREETINGS MASTER')
            else:
                query.pop(0)
                speech=''.join(query)
                speak(speech)
        if query[0]=='go' and query[1]=='to':
            speak('OPENING.....')
            query=' '.join(query[2:])
            webbrowser.get('chrome').open_new(query)
        if query[0]=='wikipedia':
            query=''.join(query[1:])
            speak("quering the universe")
            result=search_wikipedia(query)
            speak(result)
        if query[0]=='log':
            speak('ready to record your note')
            newNote=parseCommand().lower()
            now=datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            with open('note_%s.txt' % now, 'w' ) as newFile:
                newFile.write(newNote)
                speak('NOTE WRITTEN')
        if query[0]=='exit':
            speak('GOODBYE')
            break
'''import pyttsx3
engine=pyttsx3.init()
engine.say('sally sells seashells by the shore')
engine.runAndWait()'''
    
        
