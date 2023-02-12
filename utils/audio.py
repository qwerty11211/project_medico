import speech_recognition as sr

r = sr.Recognizer()
print("initiating")
with sr.Microphone() as source:
    print("listening")
    audio = r.listen(source)


text = r.recognize_google(audio)
print(text)
symptom=text.split("symptom")[1:]
