import os
import pyttsx3 
from openai import OpenAI
import speech_recognition as sr

from voices import speak


client = OpenAI(
    api_key = "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"
)

start_sequence = "\nAI:"
restart_sequence ="\nHuman: "

prompt = "The following is a conversation with an AI assistant"

engine = pyttsx3.init()

speak("Hi")

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        speak("can you please repeat if you dont mind")
        return "None"
    return query

def gpt (prompt):
    chat_completion = client.chat.completions.create(

        messages=[
            {
                "role":"user",
                "content": prompt
            }
        ],
        model = "gpt-3.5-turbo",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    data = chat_completion.choices[0].message.content
    print(data)
    speak(data)

while True:
    query = takeCommandMic()
    gpt(query)
