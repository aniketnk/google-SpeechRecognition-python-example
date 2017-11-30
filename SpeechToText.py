import speech_recognition as sr

def getText(audio):

    AUDIO_FILE = (audio)
    r = sr.Recognizer() #class which has Speech recognition functionality

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        return r.recognize_google(audio)

    except sr.UnknownValueError:
        print ("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print ("Could not request results from Google Speech Recognition service);{0}".format(e))

    return r"'None'"

#print(getText("file.wav"))