setItems = {"item 1", "item 2", "item 3"}
print(setItems) # does not keep it's order

setItems.add("item 2")
print(setItems) # it will ignore duplicates

setItems.remove("item 2") # removes "item 2" and will only have two items in our set
print(setItems)
