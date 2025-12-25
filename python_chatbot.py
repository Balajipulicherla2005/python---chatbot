
from nltk.chat.util import Chat, reflections

pairs = [
    [r'hi|hello|hey', ['Hi!', 'Hello!', 'Hey there!']],

    [r'how are you', ['I am fine, hoping you are good too']],

    [r'are you mad', ['Nice joke']],

    [r'sorry', ['A machine cannot have feelings, it’s okay!']],

    [r'what problem does your chatbot solve',
     ['The chatbot solves the problem of quickly answering common user questions '
      'without human support. It reduces response time, provides 24/7 assistance, '
      'and helps users get instant information such as FAQs, guidance, and basic support.']],

    [r'who are the target users of the chatbot',
     ['The target users are:\n'
      '- Students seeking information\n'
      '- Website visitors needing quick help\n'
      '- Customers looking for basic support\n'
      '- Beginners who want simple and clear answers\n'
      'The chatbot is designed to be easy to use for non-technical users.']],

    [r'what type of chatbot is it',
     ['This chatbot is a rule-based chatbot developed using Python. '
      'It works on predefined rules and responses. User input is matched '
      'with stored patterns, and the chatbot returns the appropriate response. '
      'It can be upgraded to an AI-based chatbot in the future.']],

    [r'why did you choose python',
     ['Python is chosen because:\n'
      '- It has simple and readable syntax\n'
      '- Strong NLP and AI library support\n'
      '- Beginner-friendly\n'
      '- Fast development and easy debugging\n'
      '- Libraries like NLTK, spaCy, and Flask help chatbot development']],

    [r'what features are included in your chatbot',
     ['The chatbot includes:\n'
      '- User-friendly text-based interaction\n'
      '- Predefined question-answer responses\n'
      '- Fallback response for unknown queries\n'
      '- Continuous conversation until exit\n'
      '- Easy to update and extend responses']],

    [r'quit|exit|bye', ['Goodbye! Have a nice day']]
]
def start_chat():
    print("Hi! I am a chatbot. Ask me anything (type 'quit' to exit).")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    start_chat()


