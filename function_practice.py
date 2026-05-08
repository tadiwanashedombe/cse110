
def compute_area_square(side1):
    """
    Calculate the area if a square
    """

    result = compute_area_rectangle(side1, side1)

    return result


def compute_area_rectangle(length, width):
    """
    Calculate the area if a square
    """

    result = width * length

    return result

def compute_area_circle(radius):
    """
    Calculate the area if a circle
    """

    result = (22/7) * (radius ** 2)

    return result

shape = "no"

while shape != "quit":
    shape = input("What shape do you have? (rectangle, square, circle) or (quit) ")

    #rectangle
    if shape.lower() == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        result = compute_area_rectangle(length, width)

        print(f"The area of your rectangle is :{result}")
    #square
    elif shape.lower() == "square":
        length = float(input("Enter the lengthof 1 side: "))

        result = compute_area_square(length)

        print(f"The area of your square is :{result}")
    #circle
    elif shape.lower() == "circle":
        radius = float(input("Enter the radius: "))

        result = compute_area_circle(radius)

        print(f"The area of your circle is :{result}")
    elif shape.lower() == "quit":
        print("Exiting...")
    else:
        print(f"{shape} is no listed try again")