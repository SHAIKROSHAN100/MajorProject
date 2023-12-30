import speech_recognition as sr
import pywhatkit

from gtts import gTTS
from playsound import playsound
import os

listener = sr.Recognizer()

def Text_to_speech(data):
    Message =  data
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
    os.remove('DataFlair.mp3')



a = "hi I'm alexa"
Text_to_speech(a)

b = "what can i do for you"
Text_to_speech(b)


def take_command():
	try:
		with sr.Microphone() as source:
			print("listening....")
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			command.lower()
			command = command.replace("alexa", " ")
			print(command)
	except:
		pass
	return command

def task():
	command = take_command()
	if "play" in command:
		song = command.replace('play', ' ')
		Text_to_speech("playing"+song)
		print(song)
		pywhatkit.playonyt(song)

		

while(True):
	task()
	inp = int(input("Enter the 0 to exit:"))
	if( inp == 0 ):
  		break



