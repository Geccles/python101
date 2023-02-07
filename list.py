lst = ["string", 4, 4.5, ["another list", 4.7], "Galina"] # keeps it's order unlike a set

lst.append("Brian") # adds a string "Brian" to the end of the list
lst.remove(lst[0]) # removes the first item in array
lst.pop() # removes the last added item in array which is string "Brian"

for item in lst:
    print(item)
