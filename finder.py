import os
import difflib

while True:
    def find_similars(fileName):
        similarFiles = []
        for root, dirs, files in os.walk("/home/darigan"):
            for file in files:
                similarity = difflib.SequenceMatcher(None, fileName.lower(), file.lower()).ratio()
                if similarity >= 0.9:
                    similarFiles.append(os.path.join(root, file))
        return similarFiles

    def main():
        fileName = input("Enter your File Name: ")
        similarFiles = find_similars(fileName)
        if similarFiles:
            print("We Found something: \n")
            for similarFile in similarFiles:
                print(similarFile)            
            input("If your looking fo something else Press a Key...")
        else:
            input("There is no related File(Press a Key to retry)...")
    
    if __name__ == "__main__":
        main()
