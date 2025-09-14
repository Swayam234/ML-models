import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('wordnet')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created by you!", "You can call me ChatBot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm fine. How can I assist you today?"]
    ],
    [
        r"(.*) your name?",
        ["My name is ChatBot. What's yours?"]
    ],
    [
        r"(.*) (help|support) (.*)",
        ["Sure, I'm here to help. Tell me your problem."]
    ],
    [
        r"(.*) (coding|skills) (.*)",
        ["I know about coding.Which language would you like to prefer? Python or java?"]
    ],
    [
        r"(.*) (learning|like) (.*)",
        ["I would try my best to give the code according to your problem."]
    ],
    [
        r"quit|bye|exit",
        ["Bye! Have a nice day.", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that.", "Can you rephrase it?"]
    ]
]

chatbot = Chat(pairs, reflections)

def start_chat():
    print("ChatBot: Hello!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "quit", "exit"]:
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

start_chat()