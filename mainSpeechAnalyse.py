'''
This program records two audios through the microphone and checks if the speech in both match

Install the following dependancies
PyAudio	0.2.11	0.2.11
SpeechRecognition	3.7.1	3.7.1
cffi	1.11.2	1.11.2
numpy	1.13.3	1.13.3
pip	9.0.1	9.0.1
setuptools	28.8.0	38.2.1
'''
import os
import SpeechToText as STT
import recordAudio as ra
import string

def main():
    person1 = "p1.wav"
    person2 = "p2.wav"

    input("Press Enter to record person 1: ")
    ra.recordSample(person1)
    input("Press Enter to record person 2: ")
    ra.recordSample(person2)
    print("Sending audio to Google Speech Recognition...")
    text1 = STT.getText(person1)
    print("Sending audio to Google Speech Recognition...")
    text2 = STT.getText(person2)

#    os.sytem('cls')
    print("\nP1: " + text1, "P2: " + text2, '\n', sep="\n")

    if not (text1 and text2):
        print("Failed to fetch audio/text.")
        quit()
    if text1.strip() == text2.strip():
        print("They said the same thing.")
    else :
        print("They said different things.")


if __name__ == '__main__':
    main()