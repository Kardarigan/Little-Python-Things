import pyshorteners

theUrl = input("Enter your URL: ")
shortner = pyshorteners.Shortener()
shortedUrl = shortner.tinyurl.short(theUrl)

print(shortedUrl)