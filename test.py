def display_regular(text):
    """
    Display regular text
    """
    print(text)

def display_uppercase(text):
    """
    Display uppercase text
    """
    print(text.upper())

def display_lowercase(lower):
    """
    Display lowercase text
    """
    print(lower.lower())


text = input("What is your message? ")

display_regular(text)
display_uppercase(text)
display_lowercase(text)