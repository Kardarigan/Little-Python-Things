import random

lunchMeals = ["Qormesabzi", "Tahchin Morgh", "Kima", "Dampokhtak", "Adas Polo", "Sabzi Polo with Morgh", "Zereshk Polo with Morgh (Sospaz)", "Loobia Polo", "Kookoo Sibzamini", "Kalam Polo", "Gooshtekoofteh", "Nokhod Polo", "Joojeh Tabe'e", "Chelo Kabab"]
dinnerMeals = ["Kookoo Sibzamini","Kookoo Sabzi","Pasta","Kashkebademjoon","Kotlet Sibzaminikham","Shirazian Kotlet", "Kotlet with Sibzamini Pokhte", "Sandewich from birron","Ash","Loobia Pokhte","Lasagna","Pirashky","Samosas","Egg", "Adassi", "Nugett", "Tonemahi","Pizza","Noodle","Salad Macarony","Olivier salad", "Falafel","Donair","Abgosht","Fileh sookhary with frenchrise","Dopiazeh", "Chelo Kabab"]

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
