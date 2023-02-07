fav_foods = ["Tacos", "burritos", "Salmon", "Shrimp"]

for food in fav_foods:
    if food == "Tacos":
        shell_type = input("Do you like soft or hard shell? ")
        print(f"You like {shell_type} {food}")

person = {
    "name": "Galina",
    "gender": "female",
    "birthMonth": "January"
}

for key, value in person.items():
    print(f"The key is {key} and the value is {value}")
