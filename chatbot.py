import re
import random
# Define the chatbot's rules and responses
rules = {
    'greeting': {
        'patterns': [r'hello', r'hi', r'hey'],
        'responses': ['Hello! Welcome to our food ordering service.', 'Hi there! How can I assist you with your order?']
    },
    'menu': {
        'patterns': [r'menu', r'options'],
        'responses': ['Sure! Here is our menu: ...\n 1.Pav Bhaji \n 2.Vada Pav \n 3.Maggi \n 4.Chai'],
    },
    'food items': {
        'patterns': [r'Vada Pav', r'Pav Bhaji', r'Chai', r'Maggi'],
        'responses': ['Do you want to confirm your order??'],
    },
    'order': {
        'patterns': [r'order', r'I want to order'],
        'responses': ['Great! Please let me know what items you would like to order.'],
    },
    'customization': {
        'patterns': [r'customize', r'special request'],
        'responses': ['Certainly! Let me know your specific requirements or any dietary restrictions.'],
    },
    'confirm_order': {
        'patterns': [r'confirm', r'place order'],
        'responses': ['Perfect! Your order has been placed. The estimated delivery time is approximately 30 minutes.'],
    },
    'gratitude': {
        'patterns': [r'thank you'],
        'responses': ['My pleasure']
    },
    'cancel_order': {
        'patterns': [r'cancel', r'change', r'update'],
        'responses': ['I apologize for the inconvenience. Please contact our customer support for order modifications.'],
    },
    'goodbye': {
        'patterns': [r'bye', r'goodbye', r'see you'],
        'responses': ['Thank you for choosing our food ordering service.', 'Goodbye!'],
    },
    'default': {
        'responses': ['Im sorry, I didnt understand that. Can you please rephrase?']
    }
}

# Function to match user input with patterns


def match_patterns(user_input, patterns):
    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            return True
    return False

# Function to get chatbot's response


def get_response(user_input):
    for intent, data in rules.items():
        patterns = data.get('patterns')
        if patterns and match_patterns(user_input, patterns):
            responses = data.get('responses')
            return random.choice(responses)
    return random.choice(rules['default']['responses'])

# Main conversation loop


def chat():
    print("Chatbot: Hello! Welcome to our food ordering service.")
    while True:
        user_input = input("User: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        # Exit the loop if the user says goodbye
        if any(re.search(pattern, user_input) for pattern in rules['goodbye']['patterns']):
            break


# Start the chatbot
if __name__ == '__main__':
    chat()
