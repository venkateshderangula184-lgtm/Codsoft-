def chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I am just a program, but I am doing great!")
        elif "your name" in user_input:
            print("Chatbot: I am a Rule-Based Chatbot.")
        elif "help" in user_input:
            print("Chatbot: I can respond to greetings, ask my name, or say bye to exit.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")
          
chatbot()
