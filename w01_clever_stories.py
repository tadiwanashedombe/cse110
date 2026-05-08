#Added two more variable "color and time" describing time of the day and color of the sky outside.

adjective = input("Enter an adjective: ")  
animal = input("Enter an animal: ")
verb = input("Enter a verb: ") 
exclamation = input("Enter an exclamation: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")  

time = input("Enter a time of day: ") 
color = input("Enter a color: ")
print()

print("Your story is : ")
print()
print(f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. '{exclamation.capitalize()}!' I yelled. But all I could think to do was to {verb1} over and over. Miraculously, that caused it to stop, but not before it tried to {verb2} right in front of my family.It was at {time} and the sky was {color}. The {animal} started to {verb1}.")
