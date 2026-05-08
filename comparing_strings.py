animal = input("What is your favourite animal? ")
animal_lc = animal.lower()

sound = ""

if animal_lc == "cat":
    sound = "meow"
elif animal_lc== "dog":
    sound = "ruff"
else:
    sound = "unkown"

print(f"The {animal} makes he sound: {sound}.")