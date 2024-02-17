questions = ("How many planets are in our solar system?: ",
            "On which planet, if any, is a day longer than a year?: ",
            "What is the name of the Mars-sized object that collided with Earth?: ",
            "How long does it take for light to travel from the Sun’s core to the surface?: ",
            "Which planet in the solar system is the hottest?: ")

options = (("A. 7", "B. 8", "C. 9", "D. 10"),
           ("A. Mercury", "B. Venus", "C. Jupiter", "D. None"),
           ("A. Planet X", "B. Mars", "C. Theia", "D. Gaia"),
           ("A. 40,000 years", "B. 400,000 years", "C. 10,000 years", "D. 100,000 years"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num= 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print(f"""
---------------------
GAME OVER! \o/\n
Your Score ---> {score}
---------------------
""")
