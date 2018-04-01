'''
This program records a 7 second audio clip through the microphone and adds it as a transcript to a text file

Install the following dependencies
SpeechRecognition	3.7.1	3.7.1
'''

import os
import time as tm
import speech_recognition as sr
import platform

def getCurrentTime():
    TimeStamp = list(map(lambda x: str(x) + ' ', tm.localtime()))
    months = ['','January ','February ','March ','April ','May ','June ','July ','August ','September ','October ','November ','December ']
    time = TimeStamp[3] + TimeStamp[4] + months[int(TimeStamp[1])] + TimeStamp[2]
    return time

def addTranscript():

    time = getCurrentTime()
    print("Time: "+ time)


    r = sr.Recognizer()
    input("Press Enter and start Speaking: ")
    print("recording...")
    with sr.Microphone(0) as source:
        file = r.listen(source, phrase_time_limit=7)
    print('...finished\nSending to google...')
    try:
        transcript = r.recognize_google(file)
    except:
        print("Couldn't send or receive data.")
        transcript = ""

    if transcript == "":
        return 0
    print("\nTranscript: " + transcript)


    try:
        open('transcript.txt')
    except:
        open('transcript.txt','w')
    finally:
        f = open('transcript.txt','a')


    f.write("\nTime: " + time + "\nTranscript: " + transcript + "\n")
    f.close()
    print("Added to transcripts.\n")
    return 1

def showTranscript():
    try:
        f = open('transcript.txt')
    except:
        print("No file exists.")
        return 0
    print("+++TRANSCRIPTS+++")
    f = f.read()
    print(f)
    return 1

if __name__ == '__main__':
    clean = 'cls' if platform.system() == "Windows" else 'clear'
    try:
        while True:
            choice = input(r"Enter 'a' to add transcript, and 'r' to read transcript: ")
            choice = choice[0]
            os.system(clean)
            if choice == 'a' :
                addTranscript()
            elif choice == 'r':
                showTranscript()
    except KeyboardInterrupt:
        print("EXIT")
