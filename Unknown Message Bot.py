import json
from urllib.request import urlopen, Request
import time


class Bot:
    def __init__(self, token: str, admin_id: int):
        self.token = token
        self.admin_id = admin_id
        self.get_url = f"https://api.telegram.org/bot{token}/getUpdates"
        self.send_url = f"https://api.telegram.org/bot{token}/sendMessage"

    def get_updates(self, offset=None):
        url = self.get_url
        if offset:
            url += f"?offset={offset}"
        with urlopen(url) as resp:
            return json.loads(resp.read())

    def send_message(self, chat_id, text):
        payload = {"chat_id": chat_id, "text": text}
        data = json.dumps(payload).encode("utf-8")
        req = Request(self.send_url, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        print(f"Sending payload: {payload}")
        with urlopen(req) as resp:
            return json.loads(resp.read())

    def handle_updates(self):
        offset = None
        while True:
            updates = self.get_updates(offset)
            if updates["result"]:
                for update in updates["result"]:
                    offset = update["update_id"] + 1
                    if "text" in update["message"]:
                        message = update["message"]["text"]
                        user_name = update['message']['from']['first_name']
                        user_id = update['message']['from']['username']
                        if message != '/start':
                            full_message = f"ID: @{user_id}\n\n{user_name}: {message}"
                            self.send_message(self.admin_id, full_message)
            time.sleep(1)


bot = Bot('7144127383:AAHHnJtEHk5VGrQK-h4H51BEQp4UYXAn2qo', 5522852608)

if __name__ == "__main__":
    bot.handle_updates()
