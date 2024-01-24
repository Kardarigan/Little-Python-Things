email = input("Enter Your Email: ")

try:
    userName = email[:email.index("@")]
    domainName = email[email.index("@")+1:email.index(".com")]


    print(f"Your Username is {userName} and your Domain Name is {domainName}")
except:
    email = input("Please Enter a Valid Email: ")