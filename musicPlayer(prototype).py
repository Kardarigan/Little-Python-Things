import os
from playsound import playsound

filesNames = os.listdir("/home/darigan/Music/!")
musicName = input("Enter The Name of your Music: ")

for file in filesNames:
    if musicName in file and ".mp3" in file:
        fullPath = os.path.join("/home/darigan/Music/!", file)
        playsound(fullPath)
        print("We Found it :)")
        exit()
    else:
        print("This Song is not Defined...")