import random

rangeNum = int(input("how many characters do want? "))

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()?"

password= " "
for z in range(rangeNum):
    password += random.choice(chars)


print(password)