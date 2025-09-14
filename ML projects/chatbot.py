import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define patterns (regex) and responses for the chatbot
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

# Create chatbot instance using predefined pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to start chatbot interaction
def start_chat():
    print("ChatBot: Hello!")
    while True:
        user_input = input("You: ")  # Take user input
        if user_input.lower() in ["bye", "quit", "exit"]:   # Exit condition
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)      # Generate response
        print("ChatBot:", response)
        
# Run chatbot
start_chat()