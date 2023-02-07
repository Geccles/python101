# we have a function that takes a name and fav food
def somename(name, fav_food):
    return f"Hello, {name} I see your favorite food is {fav_food}"

name = input("What is your name? ")
fav_food = input("What is your favorite food? ")

foo = somename(name, fav_food)
print(foo)

def exp(num1, num2):
    return num1 * num2

big_num = exp(33,6)
print(big_num)
