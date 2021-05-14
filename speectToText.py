import speech_recognition as sprec
rec1=sprec.Recognizer()
with sprec.Microphone() as source:
    audioFromMic=rec1.listen(source)
    convertedTextFromAudio=rec1.recognize_google(audioFromMic)
    print(convertedTextFromAudio)