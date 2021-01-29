from gtts import gTTS
import os
f=open("test.txt","r")
mytext=f.read().replace("\n"," ")
language="en"
output = gTTS(text=mytext,lang=language,slow=False)
output.save("output.mp3")
f.close()
os.system("start output.mp3")



