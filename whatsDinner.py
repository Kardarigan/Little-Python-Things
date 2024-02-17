import random

lunchMeals = ["Qormesabzi", "Tahchin Morgh", "Kima", "Dampokhtak", "Adas Polo", "Sabzi Polo with Morgh", "Zereshk Polo with Morgh (Sospaz)", "Loobia Polo", "Kookoo Sibzamini", "Kalam Polo", "Gooshtekoofteh", "Nokhod Polo", "Joojeh Tabe'e", "Chelo Kabab","Egg"]
dinnerMeals = ["Kookoo Sibzamini","Kookoo Sabzi","Pasta","Kashkebademjoon","Kotlet Sibzaminikham","Shirazian Kotlet", "Kotlet with Sibzamini Pokhte", "Sandewich from birron","Ash","Loobia Pokhte","Lasagna","Pirashky","Samosas","Egg", "Adassi", "Nugett", "Tonemahi","Pizza","Noodle","Salad Macarony","Olivier salad", "Falafel","Donair","Abgosht","Fileh sookhary with frenchrise","Dopiazeh", "Chelo Kabab","Burger"]

suggestedLunches = set()
suggestedDinner = set()

while True:
    theMeal = input("What kind of meal do you have in mind to offer?[l/d] ")

    if theMeal == "l":
        if len(suggestedLunches) == len(lunchMeals):
            print("I Suggested all Meals that i knew ;)")
            pass
        else:
            meal = random.choice(lunchMeals)
            while meal in suggestedLunches:
                meal = random.choice(lunchMeals)
            suggestedLunches.add(meal)
            print(f"I suggest you {meal} :)")

    elif theMeal == "d":
        if len(suggestedDinner) == len(dinnerMeals):
            print("I Suggested all Meals that i knew ;)")
            pass
        else:
            meal = random.choice(dinnerMeals)
            while meal in suggestedDinner:
                meal = random.choice(dinnerMeals)
            suggestedDinner.add(meal)
            print(f"I suggest you {meal} :)")
    else:
        print("Try again [l/d]")
        pass
