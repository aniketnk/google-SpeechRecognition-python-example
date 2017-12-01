# import time
#
#
# print(time.localtime())
# TimeStamp = list(map(lambda x: str(x) + ' ', time.localtime()))
# print(TimeStamp)
# print(int('11 ') + 9)

import speech_recognition as sr

r = sr.Recognizer()
#source = sr.Microphone(0)
print("Start Speaking...")
with sr.Microphone(0) as source:
    file = r.listen(source, phrase_time_limit= 7)
print('Sending to google...')
print(r.recognize_google(file))