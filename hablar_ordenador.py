import re
import pyttsx3
import speech_recognition as sr

def identify_name(text):
  name = None
  Patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)"]
  for pattern in patterns:  
    try:
      name = re.findall (pattern, text) [0]
    except IndexError:
      print ("No me ha dicho su nombre...")
  return name

engine= pyttsx3.init()
engine.setProperty ("rate",120)
engine.setProperty ("voice", "spanish")

engine.say ("Hola, Soy Atila, como te llamas?")
engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
  print("Puedes hablar")
  audio = r.listen(source)
  text = r.recognize_google(audio, lenguage = "es -ES")
  name = identify_name (text)
  if name:
    engine.say ("Encantado de conocerte {}" .format (name))
  else:
    engine.say ("Puedes pronunciar ms despacio, gracias")
  engine.rundAndWait()