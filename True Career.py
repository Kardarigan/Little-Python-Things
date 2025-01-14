import random

def play_game():
    print("⚽ Welcome to *Dark Whistle* ⚽")
    print("You are a young football star rising through the ranks.")
    print("But the league is corrupt, and a dangerous conspiracy threatens your career—and your life.")
    print("Make the right decisions to uncover the truth and protect yourself!\n")
    
    stages = [
        "You overhear your coach talking to someone about 'fixing matches.' Later, he asks you to meet him in private. What do you do?",
        "During a match, your teammate whispers that the game is rigged, and he’s been paid to miss chances. How do you respond?",
        "You find a threatening note in your locker: 'Lose the next match, or pay the price.' What’s your plan?",
        "At a charity gala, you see the league president exchanging a briefcase with a known criminal. He notices you staring. What do you do?",
        "A journalist contacts you, claiming to have evidence of corruption involving your team. Do you trust them?",
        "You catch your teammate trying to tamper with the referee’s car before a big match. What’s your move?",
        "Your agent warns you that if you speak out, you might lose your contract and sponsors. Will you stay quiet?",
        "During a game, you’re fouled hard, but the referee ignores it. The opposing team captain whispers, 'Stay down if you know what’s good for you.' What do you do?",
        "You receive anonymous footage showing your coach accepting a bribe. Will you expose him or keep it quiet?",
        "It’s the final match of the season. Winning will expose the corruption, but losing may keep you safe. What’s your choice?"
    ]
    
    choices = [
        ["1. Meet the coach and play along", "2. Avoid him and investigate on your own"],
        ["1. Confront the teammate on the field", "2. Report him after the match"],
        ["1. Inform the police and ask for protection", "2. Pretend to comply but plan to fight back"],
        ["1. Follow the league president discreetly", "2. Act casual and avoid suspicion"],
        ["1. Share what you know with the journalist", "2. Keep your distance and investigate further"],
        ["1. Stop your teammate and warn the referee", "2. Secretly record the tampering as evidence"],
        ["1. Stay quiet and focus on your career", "2. Speak out, even if it risks everything"],
        ["1. Fight back and continue playing", "2. Pretend to be injured and stay cautious"],
        ["1. Leak the footage to the press", "2. Confront the coach directly"],
        ["1. Play to win and expose the truth", "2. Lose intentionally to stay safe"]
    ]
    
    outcomes = [
        ["The coach reveals part of the plan, but you’re now under suspicion.", 
         "You discover more about the conspiracy but remain unnoticed."],
        ["Your teammate denies everything, but the tension rises.", 
         "The league starts investigating based on your report."],
        ["The police promise protection, but threats intensify.", 
         "Your clever plan exposes the threat without direct conflict."],
        ["The president gets suspicious and sends someone after you.", 
         "You avoid suspicion, but miss crucial details."],
        ["The journalist publishes a major story, but now you’re a target.", 
         "You uncover more leads while staying under the radar."],
        ["The referee appreciates your warning and watches closely.", 
         "Your recording becomes key evidence in the investigation."],
        ["Your silence protects your career, but the corruption grows.", 
         "Speaking out causes chaos, but you inspire others to act."],
        ["Your bravery earns respect, but you’re now a marked target.", 
         "Playing it safe keeps you out of trouble, for now."],
        ["The footage causes a scandal, but you lose your coach’s trust.",
"The coach tries to cover it up, but you gain leverage."],
        ["Your victory inspires fans and shakes the league!", 
         "Losing keeps you safe, but the corruption continues."]
    ]
    
    score = 0  # Track your success in uncovering the truth

    print("⚠️ The game begins now! ⚠️\n")
    for i in range(len(stages)):
        print(f"Stage {i + 1}: {stages[i]}")
        print(choices[i][0])
        print(choices[i][1])
        
        choice = input("Choose 1 or 2: ")
        while choice not in ["1", "2"]:
            choice = input("Invalid choice! Please choose 1 or 2: ")
        
        outcome = random.choice([0, 1])  # Randomly decide success or failure
        print(outcomes[i][int(choice) - 1])
        
        if outcome == 1:
            print("✔️ Good move! You’re getting closer to the truth.\n")
            score += 10
        else:
            print("❌ That decision might come back to haunt you.\n")

    print("🏁 Game Over! 🏁")
    if score >= 70:
        print(f"🎉 You scored {score} points! You exposed the corruption and became a hero!")
    else:
        print(f"Your score is {score}. The truth remains hidden, but your story isn’t over yet.")

# Run the game
if __name__ == "__main__":
    play_game()






