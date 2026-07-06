import random
from datetime import datetime

jokes = [
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why do programmers prefer Python? Because it's easy to read!",
    "Why was the computer cold? It forgot to close its Windows!"
]

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking. 😊"

    elif "your name" in user_input:
        return "I'm a Python GUI Chatbot."

    elif "time" in user_input:
        return datetime.now().strftime("Current Time: %I:%M %p")

    elif "date" in user_input:
        return datetime.now().strftime("Today's Date: %d-%m-%Y")

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "thank" in user_input:
        return "You're welcome! 😊"

    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day! 👋"

    else:
        return "Sorry, I don't understand that yet."