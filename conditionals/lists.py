food = [
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
print (food [0])
print (food [2])
print (food [9])
print (food [0:3])
print (food [7:10])
print(food [7])
print (food [-6])

#######
mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"], ["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]
for item in mailing_list:
 print(f"{item[0]} : {item[1]}")
