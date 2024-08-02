import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"hi|hello", ["Hello!", "Hi there!"]),
    (r"what is your name?", ["I am a chatbot"]),
    (r"how are you?", ["I'm just a program, but I'm doing great!"]),
    (r"quit", ["Bye! Take care."])
    ]

def chatbot():
    print("hi, I'm the chatbot! Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print(f"Bot: {response}")
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chatbot()