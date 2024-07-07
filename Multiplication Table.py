number = int(input("Enter a Adad => "))

for i in range(1, number+1):
    row = ""
    for j in range(1, number+1):
        row += str(i * j) + "\t"

    print(row)