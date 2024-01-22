c, l, n, s = 0, 0, 0, 0

password = input("Enter your Password: ")
capLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowLetters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
specials = "!@#$%^&*()?"

if (len(password) >= 8):
    for i in password:
        if (i in capLetters):
            c += 1
        if (i in lowLetters):
            l += 1
        if (i in numbers):
            n += 1
        if (i in specials):
            s += 1
else:
    print("Your Password is too short (its Length have to atleas 10)")

if (c >= 1 and l >= 1 and n >= 1 and s >= 1):
    print("password is Strong!")
elif (c >= 1 and l >= 1 and n >= 1):
    print("password is Good!")
else: 
    print("password is Weak, try another Password...")
