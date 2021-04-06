# -*- coding: <utf-8> -*-
import smtplib
from email.mime.multipart import MIMEMultipart
import os.path

from googletts import Translator
from pynput.keyboard import Key, Controller
import requests
import pyttsx3
import speech_recognition as sr
import datetime
import os
import time
import subprocess
import wikipedia
import webbrowser
import random
import googletrans
from PIL import Image
import pyautogui
import urllib.request
import re

def urls():
    inputs("say the song title")
    print("say the song title :")
    out8 = str(get_inputs()).replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+out8)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = ('https://www.youtube.com/watch?v='+video_ids[0])
    try:
        webbrowser.open(url)
    except:
        print("Invalid input")

def rands(list):
    abc = random.choice(list)
    return abc
emails = "jchandlerbing123@gmail.com"
pwds = "owrtnewsadjzdckg"
girl = 1
boy = 0

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[girl].id)
def loops(char , count,t):
    for i in range(1,count):
        print(char,end=" ")

        time.sleep(t)
def inputs(text):
    pyttsx3.speak(text)
def helps():
    print("Opening help documentation..........")
    subprocess.Popen(["notepad.exe","help.txt"])
    time.sleep(3)
def translates():
    print("Say the sentence :")
    inputs("Say the sentence ")
    out4 = get_inputs()
    try:
        trans = Translator()
        t = trans.translate(out4, src="en", dest="si")
        print(t.pronunciation)
        inputs(t.pronunciation)
    except:
        print("Error")

def menu():
    os.system("cls")

    loops("*",60,0.025)
    print()

    print("                                   WELCOME TO BASIC VOICE ASSISTANT PROJECT")
    print("                                        Created by Ashen Ranaweera\n\n")

    global a
    global name
    inputs("welcome to basic voice assistant project.. please fill the following details")
    loops("=",60,0.025)
    print()
    name = input("What is your name :")


    global boy
    a = input("Give me a name :")
    boy = int(input("1-Girl\n0-Boy\nAm i girl or a Boy :"))
    loops("=", 60, 0.025)
    print()
menu()


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[(boy)].id)
#global said

def searching():
    print("Tell me what to search :")
    out3 = get_inputs()
    print("Searching "+out3+" on the internet")
    try:
        os.system("start chrome https://www.google.com/search?q="+str(out3))
    except:
        os.system("start iexplore https://www.google.com/search?q="+str(out3))

def notes():
    print("Say what you want me to write")
    inputs("say what you want me to write")

    date =datetime.datetime.now()
    fname = str(date).replace(":","-")+"-note.txt"
    with open(fname,"w") as f:
        out1 = get_inputs()
        f.write(out1)

def get_inputs():
    r = sr.Recognizer()
    print("Listening")
    with sr.Microphone()as source:
        audio = r.listen(source)

        said = ""

        try:
            said = r.recognize_google(audio,language="en-in")
            print(said)
            endwords = ["stop","bye","bhai","good bye","see you","see you later","turn off","off","goodbye","Goodbye"]
            welcome = {"hello","hi","hai"}
            whatname = ["what is your name","what is name","your name","whats your name"]
            case2 = "notes", "remember this","write note","open notepad","notepad",""
            for i in endwords:
                if i in said:
                    return False
            for i in welcome:
                if i in said:
                    return 'a'
            for i in whatname:
                if i in said:
                    return 'b'
            if said in case2:
                notes()

            if "Wikipedia" in said:
                print(said)
                result = wikipedia.summary(said,sentences=3)
                print("According to Wikipedia :\n"+result)
                inputs(result)


        except Exception as e:
            list4 = ["sorry what did you say?","Can you please tell it again","Can you speak a little bit louder?","didn't hear you","there are difficuties in hearing","CAn't hear you"]
            a4 = rands(list4)
            inputs(a4)
    #inputs(said)
    return said
def weather ():

    inputs("tell me the city you want to know the weather of?")

    out6 = get_inputs()
    city = out6
    try:

        url = "https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02".format(city)
        res = requests.get(url)
        o = res.json()
        weather_status = o['weather'][0]['description']
        temperatue = o['main']['temp']
        humidity = o['main']['humidity']
        print("According to my database Weather status is "+str(weather_status)+" and current temperature is "+str(temperatue)+" in "+city)
        inputs("According to my database Weather status is "+str(weather_status)+" and current temperature is "+str(temperatue)+" in "+city)

    except Exception:
        inputs("Sorry i didnt hear you..enter the city you want to know the weather of?")

        out6 = input("Enter the City Name :")

        url = "https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02".format(out6)
        res = requests.get(url)
        o= res.json()
        weather_status = o['weather'][0]['description']
        temperatue = o['main']['temp']
        humidity = o['main']['humidity']
        print("According to my database Weather status is " + str(weather_status) + " and current temperature is " + str(temperatue) + " in " + out6)

        inputs("According to my database Weather status is " + str(weather_status) + " and current temperature is " + str(temperatue) + " in " + out6)

    except:
        print("Invalid City")


def steel1():
    send_to_email = input("Enter your email address: ")
    print("subject of the email :")
    inputs("subject of the email")
    subject = get_inputs()
    print("Subject :" + subject)
    print("please tell what is the content of the email")
    inputs("please tell what is the content of the email")
    message = get_inputs()
    print("Content :" + message)
    try:
        email = emails
        password = pwds
        print("Trying to send the email......")

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        print("Email sent........")

    except Exception as e:
        print("done", e)


def editor():
    out7 = get_inputs()
    inputs("Please tell me what to do")
    time.sleep(3)
    while True:
        print("say 'close' to escape from edit mode")

        out7 = get_inputs()
        if "select" in out7:
            inputs("All selected")
            keyboard = Controller()
            with keyboard.pressed(Key.ctrl):
                keyboard.press('a')
                keyboard.release('a')

        elif "copy" in out7:
            inputs("All Copied")
            keyboard = Controller()
            with keyboard.pressed(Key.ctrl):
                keyboard.press('c')
                keyboard.release('c')
        elif "cut" in out7:
            inputs("All copied and cleared")
            keyboard = Controller()
            with keyboard.pressed(Key.ctrl):
                keyboard.press('x')
                keyboard.release('x')
        elif "copy" in out7:
            inputs("All Copied")
            keyboard = Controller()
            with keyboard.pressed(Key.ctrl):
                keyboard.press('c')
                keyboard.release('c')
        elif "maximize" in out7:
            inputs("Maximized the window")
            keyboard = Controller()
            with keyboard.pressed(Key.cmd_l):
                keyboard.press(Key.up)
                keyboard.release(Key.up)
        elif "minimize" in out7 or "minimise" in out7:
            inputs("Minimized the window")
            keyboard = Controller()
            with keyboard.pressed(Key.cmd_l):
                keyboard.press(Key.down)
                keyboard.release(Key.down)
        elif "paste" in out7:
            inputs("All pasted")
            keyboard = Controller()
            with keyboard.pressed(Key.ctrl):
                keyboard.press('v')
                keyboard.release('v')

        elif "open" in out7:
            inputs("Notepad Opened")
            os.system("start notepad.exe")

        elif "close" in out7:
            inputs("Editor mode closed")
            break


while True:
    case = "age","old","how old are you","old are you","old you","what is your age","your age"
    change = "change name","go back","menu","stop"
    searched = "search internet","internet search","google search","search on google","search on internet", "google search on"
    out =get_inputs()
    #print(out)
    if out == False:
        list3 = ["Have a good day","talk to you soon","Stay safe, stay home,take care","bye take care"]
        a3 = rands(list3)
        inputs(a3)
        break
    elif out == 'a':
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            inputs("hello Good morning" + str(name) )
        elif hour >= 12 and hour < 18:
            inputs("hello Good Afternoon" + str(name) )
        else:
            inputs("hello Good Evening" + str(name))

    elif out == 'b':
        aa = ["you called me "+a+" and i wish every one had a nickname as cool as mine","i am "+a+" But you can change it if you want to"]
        a2 = rands(aa)
        inputs(a2)
    elif out == "fine" or out == "i am fine":
        list2 = ["good to know","I am glad","I am glad to hear it"]
        a1 = rands(list2)
        inputs(a1)
    elif out in case:
        inputs("I was launched in this month,So i am Pretty young")
    elif out == "thank you" or out == "thankyou":
        list1 = ["welcome","My pleasure","happy to help","not a problem","That's what i am here for",]
        aaa= str(rands(list1))
        inputs(aaa)
    elif "i can't" in out or "can't" in out:
        list1 = ["yes you can","you can do anything don't be negative","okay i understand","Alright alright"]
        aaa= str(rands(list1))
        inputs(aaa)
    elif "wait" in out or "weit" in out:
        ab=10
        while ab>0:
            time.sleep(1)
            print(ab,"")
            ab=ab-1
    elif out in change:
        menu()
    elif "screenshot" in out:
        pyautogui.screenshot("img.png")
        im = Image.open("img.png")
        im.show()
    elif out in searched:
        searching()
    elif "calculater" in out:
        os.system("start calc")
    elif out == "help" or out == "help me" or out == "open help":
        helps()
   # if out == "camera" or out == "open camera" or out == "take picture":
    #    subprocess.
    elif "open youtube" in out:
        print("Opening Youtube...........")
        webbrowser.open("youtube.com")
    elif "open google" in out:
        print("Opening google...........")
        webbrowser.open("google.com")
    elif "time" in out:
        timee = datetime.datetime.now().strftime("%H:%M")
        inputs("time is "+ timee)
    elif "translate" in out:
        translates()
    elif "favourite" in out:
        if "colour" in out:
            inputs("i like blue,but i like you more")
        elif "food" in out:
            inputs("If you buy me i will eat anything")
        elif "drink" in out:
            inputs("I like anything you like")
        elif "superhero" in out:
            inputs("you had to ask that? Of course it is flash")
        elif "language" in out:
            inputs("i kinda have to stay with english..don't you think")

        else:
            inputs("I dont have anything favourite,,, well but you are my favourite")
    elif a in out:
         inputs("yes speaking "+name)
    elif "weather" in out:
        weather()
    elif "today" in out:
        day = str(datetime.datetime.today()).replace(":"," ")
        inputs(day[0:12])

    elif 'edit' in out or 'notepad' in out:
        inputs("Tell me what to do")
        editor()
    elif "send emails" in out or "send email" in out or "email" in out:
        steel1()
    elif "how are you" in out:
        list5 = ["I am fine Thanks for asking", "Doing great, thanks for asking","I am all good Just trying to my best for you"]
        a5 = rands(list5)
        inputs(a5)
    elif "who are you" in out or "who make you" in out or "who made you" in out:
        inputs("My name is "+a+"   and  i am created by Ashen Ranaweera using python language")
        inputs("if you want to know more please contact him..., details are in the help documentation, say help to open it")
        inputs("have fun with me.........,")
    elif "say" in out or "se" in out:
        out = str(out[3:])
        inputs(out)
    elif "what can you do" in out or "can you do" in out:
        inputs("I can do many things..if you wanna see the list of i can do read this documentation")
        subprocess.Popen(["notepad.exe","help.txt"])
    elif "music" in out:
        urls()
    elif "bored" in out or "sucks" in out or "no" in out:
        inputs("Do you want to listen to a song")
        out9 = get_inputs()
        if "yes" in out9 or "yeah" in out9 or "yup" in out9:
            urls()
        else:
            inputs("I understand..I am available if you need anything")
    else:
        try:
            if "what is the" in out or "what are" in out:
                result = wikipedia.summary(out, sentences=3).replace("-", " ")
                print("According to my data base :\n" + result)
                inputs(result)

            elif "who is the" in out or "who is" in out:
                out = str(out[10:])
                result = wikipedia.summary(out, sentences=3).replace("-", " ")
                print("According to my data base :\n" + result)
                inputs(result)

            else:
                get_inputs()
        except:
            print("Something wrong with the result")



