def simple_chatbot():
    print("Chatbot: Hello! I'm a basic chatbot. Type 'bye' to exit.")
    
    while True:
        # Get and clean user input
        user_input = input("You: ").lower().strip()
        
        # Rule-based responses
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit loop
        else:
            print("Chatbot: I didn't understand that.")

# Start the chatbot
if __name__ == "__main__":
    simple_chatbot()