# chatbot_logic.py

def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    elif "your name" in user_input:
        return "I'm ChatBot! Your virtual assistant."

    elif "course" in user_input:
        return "You can check the course list in the student portal."

    elif "attendance" in user_input:
        return "Please wait... fetching your attendance record."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I didn't understand that. Please try something else."