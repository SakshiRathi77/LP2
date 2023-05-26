import re
import random
rules = {
    'greetings':
    {
    'pattern':[r'hi',r'hello',r'whatsup'],
    'response':["hello, I am having a great day, what about you ?  "]
    }
,
    'end':
    {
    'pattern':[r'bye',r'getlost',r'Goodbye'],
    'response':["thankyou for using me please come again"]
    }
    ,
    'questions':
    {
        'pattern':[r'what',r'why',r'how'],
        'response':["can you tell me why do you want to know that"]
    },
    'default':
    {
        'response':["sorry for inconvinence but i cant understand you "]
    }

}




def match_patterns(user_input, patterns):
    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            return True
    return False


def get_response(user_input):
    for intent, data in rules.items():
        patterns = data.get('pattern')
        if patterns and match_patterns(user_input, patterns):
            responses = data.get('response')
            return responses[0]
    return rules['default']['response'][0]
    


def chat():
    print("Chatbot: Hello! Welcome to our food ordering service.")
    while True:
        user_input = input("User: ")
        response = get_response(user_input)
        print("Chatbot:", response)
        # Exit the loop if the user says goodbye
        if any(re.search(pattern, user_input) for pattern in rules['end']['pattern']):
            break


# Start the chatbot
if __name__ == '__main__':
    chat()

    