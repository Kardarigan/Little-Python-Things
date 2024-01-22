print("Choose your Operator: \n",
      "[1] Add\n",
      "[2] Subtract\n",
      "[3] Multiply\n",
      "[4] Divide\n")

operator = input()

num1st = input("Enter your First Number: ")
num2nd = input("Enter your Seccond Number: ")

num1st = int(num1st)
num2nd = int(num2nd)

if operator == "1":
    print(num1st+num2nd)
elif operator == "2":
    print(num1st-num2nd)
elif operator == "3":
    print(num1st*num2nd)
elif operator == "4":
    print(num1st/num2nd)
else:
    print("what?")
