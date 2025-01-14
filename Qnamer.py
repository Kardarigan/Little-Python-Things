import os
import random
import string

def renameAll(path):
    items = os.listdir(path)

    for item in items:
        itemPath = os.path.join(path, item)

        if os.path.isfile(itemPath):
            fileExtension = os.path.splitext(item)[-1]
            randomNum = random.randint(100, 999)
            newFileName = f"{randomNum}_{item}"
            os.rename(itemPath, os.path.join(path, newFileName))

        elif os.path.isdir(itemPath):
            renameAll(itemPath)
    print('Misson Complete Sire')

targetPath = input("What's Your Target ?")

renameAll(targetPath)
