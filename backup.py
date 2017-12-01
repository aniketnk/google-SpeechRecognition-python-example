'''
This program records two audios through the microphone and adds it as a transcript to a text file

Install the following dependencies
PyAudio	0.2.11	0.2.11
SpeechRecognition	3.7.1	3.7.1
cffi	1.11.2	1.11.2
numpy	1.13.3	1.13.3
pip	9.0.1	9.0.1
setuptools	28.8.0	38.2.1
'''

import os
import speech_recognition as sr
import SpeechToText as STT
import recordAudio as ra
import string
import functools as ft
import time as tm


def addTranscript():
    # timeWav = "time.wav"
    # isNotValid = 1
    # while(isNotValid):
    #     isNotValid = 0
    #     input("Press Enter to record time (in hour : minutes : month : day -")
    #     ra.recordSample(timeWav,5)
    #     print("Sending time to Google Speech Recognition...")
    #     time = STT.getText(timeWav)
    #     print("time: " + time)
    #     if not len(time.split()) == 4:
    #         print("Say a valid time.")
    #         isNotValid = 1


    TimeStamp = list(map(lambda x: str(x) + ' ', tm.localtime()))
    months = ['', 'January ', 'February ', 'March ', 'April ', 'May ', 'June ', 'July ', 'August ', 'September ',
              'October ', 'November ', 'December ']
    time = TimeStamp[3] + TimeStamp[4] + months[int(TimeStamp[1])] + TimeStamp[2]
    print("Time: " + time)

    # transcriptWav = "transcript.wav"
    # input("Press Enter to record a 7 second transcript: ")
    # ra.recordSample(transcriptWav,7)
    # print("Sending transcript to Google Speech Recognition...")
    # transcript = STT.getText(transcriptWav)

    r = sr.Recognizer()
    print("Start Speaking...")
    with sr.Microphone(0) as source:
        file = r.listen(source, phrase_time_limit=7)
    print('Sending to google...')
    try:
        transcript = r.recognize_google(file)
    except:
        print("Couldn't send or receive data.")
        transcript = None

    print("Transcript: " + transcript)

    try:
        open('transcript.txt')
    except:
        open('transcript.txt', 'w')
    finally:
        f = open('transcript.txt', 'a')

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
    try:
        while True:
            choice = input(r"Enter 'a' to add transcript, and 'r' to read transcript: ")
            choice = choice[0]
            os.system('cls')
            if choice == 'a':
                addTranscript()
            elif choice == 'r':
                showTranscript()
    except KeyboardInterrupt:
        print("EXIT")
