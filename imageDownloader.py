import urllib.request as theUr

def dlImage(url, name, path):
    fullPath = path + name + ".jpg"
    theUr.urlretrieve(url, fullPath)
    
imageUrl = input("Enter your Image's URL: ")
imageName = input("Whats your Image's Name: ")
imagePath = input("Enter your Destination Path: ")

dlImage(imageUrl, imageName, imagePath)