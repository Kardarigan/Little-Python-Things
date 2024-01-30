import os

pathDirectory = input('\033[31mEnter Your Directory : ')
backup = open('allNames.txt', 'w')
backup.close()
try:
    allNames = os.listdir(pathDirectory)
    print(allNames)
    backup = open('allNames.txt', 'a')
    for name in allNames:
        name = f"' {name} ',"
        backup.write(name)
except Exception as e:
    print(f'\033[35m{e}')