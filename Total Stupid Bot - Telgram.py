import json
from urllib.request import urlopen, Request
from time import sleep
from datetime import datetime


# Define the Bot class to interact with Telegram's API
class Bot:
    def __init__(self, token: str):
        # Store the token and initialize the API URLs for the bot
        self.token = token
        self.get_url = f"https://api.telegram.org/bot{token}/getUpdates"
        self.send_url = f"https://api.telegram.org/bot{token}/sendMessage"

    def get_updates(self, offset=None):
        # Retrieve updates from Telegram API, using offset to avoid duplicates
        url = self.get_url
        if offset:
            url += f"?offset={offset}"
        with urlopen(url) as resp:
            return json.loads(resp.read())

    def send_message(self, chat_id, text):
        # Send a message to a specific chat ID
        data = json.dumps({"chat_id": chat_id, "text": text}).encode("utf-8")
        req = Request(self.send_url, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        with urlopen(req) as resp:
            return json.loads(resp.read())


# Define a file to store user scores
SCORES_FILE = "user_scores.json"


# Load scores from the file
def load_scores():
    try:
        with open(SCORES_FILE, "r") as file:
            data = file.read().strip()
            if not data:  # If file is empty, return an empty dictionary
                return {}
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or contains invalid JSON, return an empty dictionary
        return {}


# Save scores to the file
def save_scores(scores):
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file, indent=4)


# Initialize the bot with a token
bot = Bot("7827368982:AAEd9JxzlL_QWaz6zl79fFYImloSD0IR_aI")

# Define quiz questions
questions = [
    {
        "question": "Who's the Creator?", # Questions itself
        "choices": ["George Lucas", "Steven Spielberg", "James Cameron", "Christopher Nolan"], # Potential choices
        "answer": 0,  # Correct answer index
    },
    {
        "question": "Why did Anakin join the Darkside?",
        "choices": ["For his Empire", "For saving his Wife's life", "For Getting higher Ground", "To prove himself to Jedi Council"],
        "answer": 1,
    },
    {
        "question": "Where did Luke find out Darth Vader is his father?",
        "choices": ["Tatooine", "Dagobah", "Yavin 4", "Bespin"],
        "answer": 3,
    },
    {
        "question": "Complete this sentence:\nMay...",
        "choices": ["Your coffee be strong and your Monday be short", "The Force be with you", "I?", "May your soul rise up to heaven"],
        "answer": 1,
    },
]

# Keep track of user states and scores
user_states = {}  # Stores active game state for each user
user_scores = load_scores()  # Load scores from file
last_update_id = None  # Tracks the last update ID proccesed
first_entry = True  # Used to send a welcome back message on first game interaction

# Main loop to handle updates from Telegram
while True:
    response = bot.get_updates(offset=last_update_id)  # Fetch updates
    if not response.get("result"):  # If no updates, wait and retry
        sleep(5)
        continue

    # Process each update from the API response
    for update in response["result"]:
        last_update_id = update["update_id"] + 1  # Update offset to avoid duplicates
        user_id = str(update["message"]["from"]["id"])  # Extract user ID
        text = update["message"]["text"]  # Extract user message

        # If the user is new, ask for their name and initialize their score record
        if user_id not in user_scores:
            bot.send_message(user_id, "Welcome! What's your name?")
            user_scores[user_id] = {"name": None, "scores": []}  # Initalize user record
            save_scores(user_scores)  # Save to file
            continue

        # If the user's name is not set, treat the current message as their name
        if user_scores[user_id]["name"] is None:
            user_scores[user_id]["name"] = text.strip()  # Set the name
            save_scores(user_scores)  # Save to file
            bot.send_message(user_id, f"Hello {user_scores[user_id]['name']}! Let's start the game.")
            user_states[user_id] = {"question_index": 0}  # Initialize game state
            current_question = questions[0]
            # Send the tirst question
            message = f"{current_question['question']}\n" + "\n".join([f"{i + 1}. {choice}" for i, choice in enumerate(current_question["choices"])])
            bot.send_message(user_id, message)
            continue

        # Greet returning users with a welcome back message
        if first_entry and user_scores[user_id]["name"]:
            first_entry = False
            bot.send_message(user_id, f"Welcome back {user_scores[user_id]['name']}.\nLet's do some business then, eh!")

        # Handle the /report command to show user's score history
        if text == "/report":
            if user_scores[user_id]["scores"]:  # If the user has scores
                score_records = user_scores[user_id]["scores"]
                report_message = f"Your Score History, {user_scores[user_id]['name']}:\n\n" + "\n".join(
                    [f"{record['date']} ==> {record['score']} 🍳" for record in score_records]
                )
            else:
                report_message = "No score history found. Play a game first!"
            bot.send_message(user_id, report_message)
            continue

        # If the user is not in an active game state, start a new game
        if user_id not in user_states:
            user_states[user_id] = {"question_index": 0}  # Initialize game state
            current_question = questions[0]
            # Send the first question
            message = f"{current_question['question']}\n" + "\n".join(
                [f"{i + 1}. {choice}" for i, choice in enumerate(current_question["choices"])]
            )
            bot.send_message(user_id, message)
        else:
            # Handle user's answer to the current question
            state = user_states[user_id]
            current_question = questions[state["question_index"]]

            try:
                answer = int(text) - 1  # Convert user input to a uindex
                if 0 <= answer < len(current_question["choices"]):  # Validate answer
                    correct_answer = current_question["answer"]
                    if answer == correct_answer:  # Checking currect answer
                        bot.send_message(user_id, "Correct! 👍🏿")
                        current_date = datetime.now().strftime("%Y-%m-%d")
                        # Update or add today's score
                        if not user_scores[user_id]["scores"] or user_scores[user_id]["scores"][-1]["date"] != current_date:
                            user_scores[user_id]["scores"].append({"date": current_date, "score": 1})
                        else:
                            user_scores[user_id]["scores"][-1]["score"] += 1
                        save_scores(user_scores)  # Save to file
                    else:
                        # Inform the user about the correct answer
                        bot.send_message(user_id, f"Incorrect! 😔\nThe correct one was {current_question['choices'][correct_answer]}")

                    # Move to the next question or end the game
                    state["question_index"] += 1
                    if state["question_index"] < len(questions):  # There is still some questions
                        next_question = questions[state["question_index"]]
                        message = f"{next_question['question']}\n" + "\n".join(
                            [f"{i + 1}. {choice}" for i, choice in enumerate(next_question["choices"])]
                        )
                        bot.send_message(user_id, message)
                    else:  # No more questions remains
                        bot.send_message(user_id, "All done! Use /report to see your score history. Come back anytime.")
                        first_entry = False
                        del user_states[user_id]  # End game state
                else:
                    bot.send_message(user_id, "Please select a valid option.")
            except ValueError:
                bot.send_message(user_id, "Please enter a number corresponding to the choices.")

    sleep(2)  # Delay before tryinna get new updates