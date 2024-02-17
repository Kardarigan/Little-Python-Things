import random

lunchMeals = ["Qormesabzi", "Tahchin Morgh", "Kima", "Dampokhtak", "Adas Polo", "Sabzi Polo with Morgh", "Zereshk Polo with Morgh (Sospaz)", "Loobia Polo", "Kookoo Sibzamini", "Kalam Polo", "Gooshtekoofteh", "Nokhod Polo", "Joojeh Tabe'e", "Chelo Kabab","Egg"]
dinnerMeals = ["Kookoo Sibzamini","Kookoo Sabzi","Pasta","Kashkebademjoon","Kotlet Sibzaminikham","Shirazian Kotlet", "Kotlet with Sibzamini Pokhte", "Sandewich from birron","Ash","Loobia Pokhte","Lasagna","Pirashky","Samosas","Egg", "Adassi", "Nugett", "Tonemahi","Pizza","Noodle","Salad Macarony","Olivier salad", "Falafel","Donair","Abgosht","Fileh sookhary with frenchrise","Dopiazeh", "Chelo Kabab","Burger"]

suggestedMeals = set()

while True:
    theMeal = input("What kind of meal do you have in mind to offer?[l/d] ")
    if theMeal == "l":
        if len(suggestedMeals) == len(lunchMeals) + len(dinnerMeals):
            meal = random.choice(lunchMeals)
            while meal in suggestedMeals:
                meal = random.choice(lunchMeals)
        else:
            print("I Suggested all Meals that i knew ;)")
        suggestedMeals.add(meal)
        print(f"I suggest you {meal} :)")
    elif theMeal == "d":
        if len(suggestedMeals) == len(dinnerMeals) + len(dinnerMeals):
            meal = random.choice(dinnerMeals)
            while meal in suggestedMeals:
                meal = random.choice(dinnerMeals)
        else:
            print("I Suggested all Meals that i knew ;)")
        suggestedMeals.add(meal)
        print(f"I suggest you {meal} :)")
    else:
        print("Try again [l/d]")
        pass
