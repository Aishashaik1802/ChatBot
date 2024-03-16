import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to help you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse.",]
    ],
    [
        r"(.*) created ?",
        ["I was created by a human programmer.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tokyo, Japan',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you later :)"]
    ],
]

# Create a chatbot
def chatbot():
    print("Hi, I'm a chatbot. You can ask me anything. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    while True:
        try:
            user_input = input("You: ")
            response = chat.respond(user_input)
            print("Bot:", response)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()
