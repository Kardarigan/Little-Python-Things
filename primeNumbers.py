qualifyNums = [2,3,5,7]
def if_its_prime(number):
    if number < 2:
        print("It's less than 2!")
        return False
    else:
        for num in qualifyNums:
            if number % num == 0:
                if number not in qualifyNums:
                    print(f"{str(theNumber)} Not a Prime Number :)")
                    return False
            else:
                print(f"{number} is a Prime Number :)")
                return True
    
    
theNumber = int(input("Enter your Number: "))
if_its_prime(theNumber)