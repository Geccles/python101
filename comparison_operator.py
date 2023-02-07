can_code = True

if can_code:
    print("You know how to code")
else:
    print("You don't know how to code yet")

teacher = "Harry Potter"

if teacher.lower() == "harry potter":
    print("You are a wizard")
else:
    print("You must be a muggle")

name = input("What is your name? ")
if name.lower() == "harry potter":
    print("Welcome back Harry Potter")
    patronous = "stag"
elif name.lower() == "ron weasley":
    patronous = "jack russell terrier"
elif name.lower() == "hermione granger":
    patronous = "otter"
else:
    print("You're not Harry Potter!! Go get!")
    patronous = "muggle"

print(f"Your patronous is a {patronous}")

your_age = input("What is your age? ")
formatted_age = int(your_age)
if formatted_age < 18:
    print("You can't vote")
elif formatted_age < 21:
    print("You can't drink alcohol yet")
else:
    print("You can vote and drink")

if formatted_age >= 10 and name == "harry potter":
    print(f"{name} you can go to hogwarts")
else:
    print(f"{name} you can't go to hogwarts yet")
