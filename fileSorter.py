import os, shutil

# thePath = input("Enter your Folder's Path: ")
thePath = "/home/darigan/Downloads/YYC/"
folderNames = ["D Gallery", "D Musics", "D Docs"]
filesNames = os.listdir(thePath)

for z in range(0,3):
    if not os.path.exists(thePath + folderNames[z]):
        os.makedirs(thePath + folderNames[z])

for file in filesNames:
    if ".csv" in file and not os.path.exists(thePath + "D Docs" + file):
        shutil.move(thePath + file, thePath + "D Docs")
    elif ".zip" in file and not os.path.exists(thePath + "D Docs" + file):
        shutil.move(thePath + file, thePath + "D Docs")
    elif ".mp3" in file and not os.path.exists(thePath + "D Musics" + file):
        shutil.move(thePath + file, thePath + "D Musics")
    elif ".jpg" in file and not os.path.exists(thePath + "D Gallery" + file):
        shutil.move(thePath + file, thePath + "D Gallery")
    elif ".mp4" in file and not os.path.exists(thePath + "D Gallery" + file):
        shutil.move(thePath + file, thePath + "D Gallery")
    else:
        print(f"The File with name '{file}' is in none of the File Types\/")