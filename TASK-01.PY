
import random  # For random jokes or responses
import datetime  # For time and date

def chatbot():
    user_name = None  # To remember the user's name
    interaction_count = 0  # Count how many times we've chatted
    
    print("Hey! I'm an upgraded simple bot. Type 'help' for what I can do, or 'bye' to quit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        interaction_count += 1
        
        # Greeting responses
        if "hello" in user_input or "hi" in user_input or "hey" in user_input:
            if user_name:
                print(f"Bot: Hey {user_name}! Nice to see you again.")
            else:
                print("Bot: Hello! What's your name?")
        
        # Name handling
        elif "my name is" in user_input or "i am" in user_input:
            # Simple way to extract name
            words = user_input.split()
            if "name" in user_input:
                name_index = words.index("name") + 2  # Assuming "my name is [name]"
            else:
                name_index = words.index("am") + 1
            if name_index < len(words):
                user_name = words[name_index].capitalize()
                print(f"Bot: Got it, {user_name}! Nice to meet you.")
            else:
                print("Bot: Sorry, I didn't catch your name. Try 'my name is [your name]'.")
        
        elif "what's your name" in user_input or "who are you" in user_input:
            print("Bot: I'm a simple chatbot built with Python. You can call me Bot.")
        
        # How are you
        elif "how are you" in user_input:
            responses = ["I'm good, thanks!", "Doing well, how about you?", "Fantastic, as always!"]
            print(f"Bot: {random.choice(responses)}")
        
        # Weather
        elif "weather" in user_input:
            print("Bot: I can't check real weather, but imagine it's nice outside!")
        
        # Time and date
        elif "time" in user_input:
            now = datetime.datetime.now()
            print(f"Bot: The current time is {now.strftime('%H:%M:%S')}.")
        
        elif "date" in user_input:
            today = datetime.date.today()
            print(f"Bot: Today's date is {today.strftime('%Y-%m-%d')}.")
        
        # Jokes
        elif "joke" in user_input or "tell me a joke" in user_input:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call fake spaghetti? An impasta!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!"
            ]
            print(f"Bot: {random.choice(jokes)}")
        
        # Basic math
        elif "calculate" in user_input or "math" in user_input:
            print("Bot: I can do simple math. Try something like '2 + 3' or '10 * 5'.")
        
        elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
            try:
                # Simple eval for basic math (be careful with this in real code!)
                result = eval(user_input.replace(" ", ""))
                print(f"Bot: The result is {result}.")
            except:
                print("Bot: Sorry, I couldn't calculate that. Keep it simple like '2 + 3'.")
        
        # Help
        elif "help" in user_input:
            print("Bot: Here's what I can do:")
            print("- Greet me with hello, hi, or hey.")
            print("- Tell me your name with 'my name is [name]'.")
            print("- Ask 'how are you', 'what's your name', 'weather', 'time', 'date'.")
            print("- Say 'joke' for a funny one.")
            print("- Do basic math like '2 + 3'.")
            print("- Say 'bye' to quit.")
        
        # Bye
        elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
            if user_name:
                print(f"Bot: Bye {user_name}! We chatted {interaction_count} times. Come back soon!")
            else:
                print(f"Bot: See ya! We had {interaction_count} interactions.")
            break
        
        # Default
        else:
            responses = [
                "Hmm, not sure what you mean. Try 'help' for options.",
                "I didn't get that. Maybe ask about the weather or tell a joke?",
                "Sorry, my brain is simple. What else can I help with?"
            ]
            print(f"Bot: {random.choice(responses)}")

# Run the chatbot
chatbot()
