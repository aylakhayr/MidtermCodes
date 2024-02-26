
try:
    age = int(input("How old are you? "))
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    # Do some sanity checks on age19
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative, or greater than 130")
    elif age < 18:
        print(" I am sorry, too young to play this drinking game everywhere in the world")
    elif age < 21 and country == "US":
        print("I am sorry, too young to play this drinking game in the US")
    else:
        drink = random.choice(drinks)