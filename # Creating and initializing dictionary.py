# Creating and initializing dictionary
d = {"name": "Rahul", "age": 20}

print("Dictionary:", d)

# Accessing elements
print("Name:", d["name"])
print("Age:", d["age"])

# Adding new element
d["city"] = "Mumbai"
print("After adding element:", d)

# Updating element
d["age"] = 21
print("After updating element:", d)

# Removing element
del d["city"]
print("After removing element:", d)

# Merging dictionaries
d2 = {"course": "Python"}
d.update(d2)
print("After merging dictionaries:", d)