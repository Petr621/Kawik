import pyttsx3
import audioread
import time
import pyautogui
engine = pyttsx3.init()
voices = engine.getProperty('voices')
import os
import sys
from colorama import init, Fore
from colorama import Back
from colorama import Style
import subprocess
from alive_progress import alive_bar
import keyboard

for voice in voices:
    if voice.name == 'IVONA 2 Maxim OEM - Russian male voice [22kHz]':
        engine.setProperty('voice', voice.id)

def speak(query):
    engine.setProperty("rate", speed)
    engine.save_to_file(query, "saved_file.mp3")
    engine.runAndWait()
    with audioread.audio_open('saved_file.mp3') as f:
        sec = (f"{f.duration}").strip('().')
        totalsec = int(sec[:sec.find('.')]) + 0.3
    pyautogui.press("8")
    mylist = []
    i = 1
    while i<100:
        mylist.append(i)
        i += 1
    os.system('cls')
    with alive_bar(len(mylist)) as bar:
        for i in mylist:
            bar()
            time.sleep(totalsec/len(mylist))
            if keyboard.is_pressed('9'):
                break
#    time.sleep(totalsec)
    os.system('cls')

def takeCommand():
    query = input(Fore.GREEN +"=> ")
    return query
    
if __name__ == '__main__' :
    speed = 125
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    proc = subprocess.Popen('C:/Users/petr_/Downloads/soundpad/Soundpad.exe', startupinfo=startupinfo)
    os.system('cls')
    print(Fore.GREEN + """
            ╔╗╔═╗╔═══╗╔╗──╔╗╔══╗╔╗╔═╗
            ║║║╔╝║╔═╗║║╚╗╔╝║╚╣─╝║║║╔╝
            ║╚╝╝─║║─║║╚╗║║╔╝─║║─║╚╝╝─
            ║╔╗║─║╚═╝║─║╚╝║──║║─║╔╗║─
            ║║║╚╗║╔═╗║─╚╗╔╝─╔╣─╗║║║╚╗
            ╚╝╚═╝╚╝─╚╝──╚╝──╚══╝╚╝╚═╝ 
                                          by Zozick

        """)
    time.sleep(5)
    speak("Робот кавик к вашим услугам")
    os.system('cls')
    speed1 = input("Введите скорость чтения (125) \n=> ")
    if speed1.isdigit() == False:
        speed = 125
    else: speed = int(speed1)
    os.system('cls')
    while True:
        query = takeCommand().lower()
        if query == "kill":
            os.system("taskkill /im Soundpad.exe")
            os.system("taskkill /im Soundpad.exe")
            os.system("taskkill /im Soundpad.exe")
            os.system('cls')
            sys.exit("Program stopped")
        if len(query) >= 1:
            speak(query)   
        else: os.system('cls')