#i will use the pyttsx3 
#now here we will use the class to take in the input

import speech_recognition
import pyttsx3

class ToDoList:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the TTS engine
        self.work = []

    def get_text(self):
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)  # Adjust for ambient noise
            try:
                audio = recognizer.listen(mic, timeout=2)  # Listen for 2 seconds
                text = recognizer.recognize_google(audio).lower()
                print(f"You said: {text}")
                return text
            except speech_recognition.UnknownValueError:
                print("Sorry, could not understand audio.")
                return ""
            except speech_recognition.RequestError as e:
                print("Error:", e)
                return ""
            except speech_recognition.WaitTimeoutError:
                print("Timeout: No speech detected.")
                return ""

    def add_task(self):
        text = self.get_text()
        if text:
            self.work.append(text)

    def show_tasks(self):
        for task in self.work:
            print(task)

# Create an instance of ToDoList
work = ToDoList()

while True:
    print("Enter 1 to input a task")
    print("Enter 2 to show all tasks")
    print("Enter 3 to quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        work.add_task()
    elif choice == 2:
        work.show_tasks()
    elif choice == 3:
        break
