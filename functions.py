def get_positve_value(prompt_text):
    """
    Prompt the user for a value and reprompts them if the value is a negtive
    """
    #prompt for value
    value = float(input(prompt_text))

    #check if it is positive
    while value < 0:
        print("Soryy value can not be a negetive")

        value = float(input(prompt_text))

    #return value
    return value

length  = get_positve_value("What is the length of the rectangle? ")
width = get_positve_value("What is the width of the rectangle? ")

area = length * width

print(f"The are is {area}")


