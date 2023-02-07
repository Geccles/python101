name = "Galina"
def myfunc(name):
    name = "name changed"
    return name

print(myfunc(name)) # we will get the overwrite name here
print(name) # we will get the default value "Galina" because we didn't call our function which is where we change the name value
