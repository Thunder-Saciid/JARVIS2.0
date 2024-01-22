import pyttsx3  #package to convert text to speech
import datetime
import speech_recognition as sr
import smtplib
from secrets_1 import senderEmail,emailPassword,emailTo
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
from nltk.tokenize import word_tokenize
from voices import speak
from openai import OpenAI




client = OpenAI(
    api_key = "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"
)




# engine = pyttsx3.init()

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def gpt(prompt):
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


def time():
    Time = datetime.datetime.now().strftime("%I:%M")# hour = I, minutes = M, seconds = S.
    speak("The time is")
    speak(Time)

def date():
    date = int(datetime.datetime.now().day)
    month = datetime.datetime.now().month
    year = int(datetime.datetime.now().year)
    speak(date)
    speak(month)
    speak(year)

def sendEmail(reciever,subject,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail,emailPassword)
    email = EmailMessage()
    email['From'] = senderEmail
    email['To'] = reciever
    email['subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendWhatsapp (phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
    sleep(10)
    pyautogui.press('Enter')

def searchOnGoogle():
    speak("What should i sourch for you my love")
    search = takeCommandMic()
    wb.open("https://www.google.com/search?q="+search)

def news():
    newsapi= NewsApiClient(api_key='e18cd1eb978840efacab7d41a57874fd')

    speak("What topic do you wanna search")

    topic = takeCommandMic()
    data=newsapi.get_top_headlines(q=topic,
                                   language='en',
                                   page_size=5)
    
    newsdata= data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))


    speak("That is it for today my belovely darling, til next time")

def textToSpeach():
    text = clipboard.paste()
    print(text)
    speak(text)

def open_application(app_name):
    try:
        os.startfile(app_name)
    except FileNotFoundError:
        print(f"Application {app_name} not found.")

def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("good morning Sir!")
    elif hour >=12 and hour <18:
        speak("good afternoon Sir! ")
    
    elif hour >=18 and hour <24:
        speak("Good evening sir! ")
    else:
        speak("Good night Sir! ")

def wishme():
    greeting()
    speak("How can i assist you my beloved master")


def takemCMDcommand():
    query = input("How can i assist you sir? ")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
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

if __name__ == "__main__":
    
    wishme()

    wakeupWord = "Nora"

    while True:

        query = takeCommandMic().lower()
        query1 = query

        if wakeupWord in query:
  
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'email' in query:
                email_list = {
                    'mail':'saciid4867@gmail.com'
                }
                try:
                    speak("Who you want to send")
                    name= takeCommandMic()
                    reciever = email_list[name]

                    speak("what is the subject you want to send")
                    subject= takeCommandMic()
                    
                    speak('What should i write in the email?')
                    content = takeCommandMic()

                    sendEmail(reciever,subject,content)

                    speak('Email has been succesfully send my beloved master')

                except Exception as e:
                    print(e)
                    speak('Sorry my beloved master, could not sendt the email')
            elif 'message' in query:
                user_name = {
                    'to my friend':'+4748428061'
                }

                try:
                    speak("Who you want to send the message")
                    name= takeCommandMic()
                    phone_no = user_name[name]

                    speak("what is the message you want to send")
                    message= takeCommandMic()
                    
                    sendWhatsapp(phone_no,message)

                    speak('message has been succesfully send my beloved master')

                except Exception as e:
                    print(e)
                    speak('Sorry my beloved master, could not sendt the message')


            elif 'wikipedia' in query:
                speak('Searching on wikipedia...')
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences= 2)
                print(result)
                speak(result)

            elif 'google' in query:
                searchOnGoogle()
            

            elif 'youtube' in query:
                speak("Searching on youtube...")
                query =query.replace("youtube","")
                pywhatkit.playonyt(query)
            
            elif 'weather' in query:
                url = "https://api.openweathermap.org/data/2.5/weather?q=oslo&units=imperial&appid=4f668cb5c06c87529e4b50578d950fc1"
                res = requests.get(url)
                data = res.json()

                weather = data['weather'][0] ['main']
                temperature = data['main'] ['temp']
                temperature = round((temperature-32)*5/9)
                description = data['weather'][0]['description']
                print(weather)
                print(temperature)
                speak('Temperature is : {} degree celcius'.format(temperature))
                speak('Weather is : {} '.format(description))
            

            elif 'news' in query:
                news()

            elif 'read' in query:
                textToSpeach()

            elif 'open' in query:
                app_name = query.replace('open ', '').strip()
                open_application(app_name)
            
            elif 'remember' in query:
                speak('What do you want me to remember darling')
                data = takeCommandMic()
                
                speak('You told me to remember'+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            

            elif 'what do you know' in query:
                remember = open('data.txt','r')
                speak('you told me to remember that '+remember.read())
            
            

            elif 'terminate' in query:
                speak("okay my darling")
                quit()

            else:
                gpt(query1)


