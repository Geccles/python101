# only has count and index attributes which means they take less memory
# use tuples for lists that never need to change
foods = ("pizza", "orange", "avocado", "pasta",)

for food in foods:
    print("This is a", food)
