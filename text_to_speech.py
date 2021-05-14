from gtts import gTTS
import os

#myText=" Bismillah"
fileHandler=open("sourcedata.txt","r")
myText=fileHandler.read().replace("\n"," ")
language='en'
output=gTTS(text=myText,lang=language, slow=False)
output.save("Bismillah.mp3")
fileHandler.close()
os.system("start Bismillah.mp3")