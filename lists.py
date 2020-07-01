print("lists yay!")
tea_collection = ["Earl Grey", "Peppermint", "Lemon and Ginger", "Strawberry Cream"]
print(tea_collection)
print(tea_collection[0])
print(tea_collection[3])
print(tea_collection[0:2])
print(tea_collection[2:4])
# print(tea_collection[73])
print(tea_collection[-1])
print(tea_collection[-2])
print(tea_collection[1:-1])
print(tea_collection[-3:-1])

tea_collection[-1] = "Melbourne Breakfast"
print(tea_collection)

print(tea_collection[-3:])

print()

tea_collection.append("Chai")
print(tea_collection)
print(len(tea_collection))

tea_collection.extend(["new york Breakfast", "Berry"])
print(tea_collection)

print()

print(tea_collection.pop())
print(tea_collection)

print(tea_collection.pop())
print(tea_collection)

tea_collection = [
    ["Earl Grey", "Melbourne Breakfast", "Chai"],
    ["Peppermint", "Lemon and Ginger", "Strawberry Cream"]
]
print(tea_collection)
print(tea_collection[0])
print(tea_collection[0][0])

black_teas = tea_collection[0]
print(black_teas[0])

tea_collection.append(["Chamomile", "Green", "Dandelion"])
print(tea_collection)
print(len(tea_collection))
if len(tea_collection) > 3:
    print("greater than 3")
else:
    print("less than or equal to 3")
black_teas = tea_collection[0]
print(black_teas)
if "Chai" in black_teas:
    print("Yay! we have chai!")
foods = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit",
"mango",
"kiwifruit"
]
print(foods)    
print(foods[0])
print(foods[2])
print(foods[9])
print(foods[7])