person = {
    "firstName": "Galina",
    "lastName": "Nosti",
    "gender": "female",
}

print(person["gender"]) # prints out value for key item "gender"

person["birthMonth"] = "January" # adds a new key value of "birthMonth": "January" to our dictionary
print(person)

del person["birthMonth"] # removes the key value pair for "birthMonth"
print(person)
