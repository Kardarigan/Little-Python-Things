import random

lunchMeals = ["Qormesabzi","Qormesabzi","Qormesabzi","Qormesabzi","Qormesabzi","Qormesabzi","Qormesabzi","Qormesabzi"]
dinnerMeals = ["Pasta","Pasta","Pasta","Pasta","Pasta","Pasta","Pasta","Pasta","Pasta","Pasta","Pasta","Pasta"]

while True:
    theMeal = input("What kind of meal do you have in mind to offer?[l/d] ")
    if theMeal == "l":
        meal = random.choice(lunchMeals)
        print(f"I suggest you {meal} :)")
    elif theMeal == "d":
        meal = random.choice(dinnerMeals)
        print(f"I suggest you {meal} :)")
    else:
        print("Try again [l/d]")
        pass