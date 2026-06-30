import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

class Student:
    def __init__(self, name, talent, truth_bullets):
        self.name = name
        self.talent = talent
        self.truth_bullets = truth_bullets
        self.suspicion = random.randint(10, 50)
        self.alive = True
        self.votes_against = 0

def start_trial(students, victim_name):
    for s in students:
        if s.name == victim_name:
            s.alive = False
            break

    print(f"BODY DISCOVERED: {victim_name} is dead!")
    print('CLAS TRIAL BEGINS!\n')

    evidence = pd.DataFrame({
        'Student': [s.name for s in students],
        'Talent': [s.talent for s in students],
        'Suspicion': [s.suspicion for s in students],
        'Alive': [s.alive for s in students],
        'Truth_Bullets': [random.randint(0, 5) for _ in range(len(students))]
    })

    alive_mask = evidence['Alive'] == True
    evidence.loc[alive_mask, 'Suspicion'] += np.random.randint(10, 40, size=len(evidence[alive_mask]))

    print('EVIDENCE ANALYSIS:')
    print(evidence[['Student', 'Talent', 'Suspicion']])

    for round_num in range(1, 4):
        print(f"\n ARGUMENT ROUND {round_num}!")

        for s in students:
            if not s.alive or s == students[0]:
                continue

            if s.truth_bullets > 0 and random.random() < 0.5:
                s.truth_bullets -= 1
                s.suspicion -= random.randint(5, 15)
                print(f" -> {s.name} fires truth bullet! Suspicion drops.")
            else:
                s.suspicion += random.randint(10, 15)
                print(f" -> {s.name} stumbles... Suspicoin rises!")

    alive_studends = [s for s in students if s.alive]
    suspicions = np.array([s.suspicion for s in alive_studends])
    blackened_idx = np.argmax(suspicions)
    blackened = alive_studends[blackened_idx]

    print(f'TIME TO VOTE!')
    for s in alive_studends:
        if s != blackened:
            blackened.votes_against += 1

    return blackened, evidence

def plot_trial(evidence, blackened):
    alive_data = evidence[evidence['Alive'] == True]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    colors = ['red' if name == blackened.name else 'gray' for name in alive_data['Suspicion']]
    
    ax1.bar(alive_data['Student'], alive_data['Suspicion'], color=colors)
    ax1.set_title('FINAL SUSPICION LEVELS')
    ax1.set_xlabel('Studnet')
    ax1.set_ylabel('Suspicion %')
    ax1.tick_params(axis='x', rotation=45)

    bullets_used = evidence['Truth_Bullets'].values
    ax2.pie(bullets_used, labels=evidence['Student'], autopct='%1.1f%%')
    ax2.set_title('TRUTH BULLETS REMAINING')

    plt.tight_layout()
    plt.show()

def execute_blackened(blackened):
    print(f'''
{'=' * 50}
PUNISHMENT TIME!
{blackened.name}, the Ultimate {blackened.talent}, has been found guilty!
Votes received: {blackened.votes_against}
EXECUTION: {blackened.name} faces the ultimate punishment...
{'=' * 50}
''')

def survival_stats(students):
    alive = [s for s in students if s.alive]
    dead = [s for s in students if s.alive]

    sruvival_df = pd.DataFrame({
        'Status': ['Alive', 'Dead'],
        'Count': [len(alive), len(dead)]
    })

    print('SURVIVAL STATISTICS:')
    print(sruvival_df)
    print(f'Survival Rate: {len(alive)/len(students)*100:.1f}%')

    return sruvival_df


students = [
    Student('Enishima', 'Modeling', 2),
    Student('Naegi', 'Lucky', 5),
    Student('Togami', 'Affluent Progeny', 6),
    Student('Kuwata', 'Baseball Player', 1),
    Student('Ishimaru', 'Moral Compass', 3),
    Student('Hagakure', 'Fortune Teller', 2),
    Student('Kirigiri', 'Detective', 5),
    Student('Celeste', 'Gambler', 4),
    Student('Asahina', 'Swimming Pro', 1),
    Student('Ogami', 'Martial Arts', 3),
    Student('Fukawa', 'Writer', 2),
    Student('Owada', 'Biker Gang Leader', 4),
    Student('Yamada', 'Fanfic Writer', 1),
    Student('Fujisaki', 'Programmer', 5),
]

students.append(Student('Maizono', 'Pop Sensation', 0))
students[-1].alive = False

victim = 'Maizano'

blackened, evidence = start_trial(students, victim)
plot_trial(evidence, blackened)
execute_blackened(blackened)
survival_stats(students)