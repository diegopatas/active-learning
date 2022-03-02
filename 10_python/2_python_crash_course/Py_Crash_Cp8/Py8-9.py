# Program MESSAGES
def show_messages(messages: list):
    """Print messages from a list."""
    for m_i in messages:
        print(f"The message for you is: {m_i.title()}.")

def send_messages(messages: list, newplace: list):
    """Move messages"""
    while messages:
        extract = messages.pop()
        print(f"The message {extract} were moved.")
        newplace.append(extract)


messages = ['how are you?', 'how have you been?', "what's up?"]
sent = []

show_messages(messages)
send_messages(messages, sent)
print(f"{messages}\n{sent}")
