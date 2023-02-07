age = input("What is your age? ")
data_type = type(age)
print(data_type)

age = int(age)
data_type = type(age)
print(data_type)

print("Your age in dog years is", (age * 7))

grocery_list = ["apples", "bananas", "milk", "water", "milk"]
grocery_list = set(grocery_list)
print(type(grocery_list)) # our duplicate item "milk" should only show up once
