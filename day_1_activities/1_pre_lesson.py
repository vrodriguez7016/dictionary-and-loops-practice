# this is what we will use for the video intro to dictionaries

# dictionary = a collection of {key:value} pairs
#              orderd and changable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

#if capitals.get("Russia"):
#    print("That capital exists")
#else:
#    print("That capital doesn't exists")

# capitals.update({"Germany": "Berlin"}) # similar to append the list
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem() # removes the last item in the dict
# capitals.clear()

keys = capitals.keys() # returns all keys within dict

# interate over every key
for key in capitals.keys():
    print(key)

# interate over every value
values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

print(capitals)