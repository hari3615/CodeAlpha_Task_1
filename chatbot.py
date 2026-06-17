print("Simple Chatbot")
print("Type 'bye' to stop")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")
    
    elif user == "how are you":
        print("Bot: I am fine!")

    elif user == "what is your name":
        print("Bot: I am a Python chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand.")