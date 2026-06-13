print("Welcome to ChatBot!")
print("Type 'bye' to exit.")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I am fine, thanks!")

    elif user == "what is your name":
        print("Bot: My name is ChatBot.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")