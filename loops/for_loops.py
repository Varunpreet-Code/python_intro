# tea_collection = [
#     "Earl Grey",
#     "Melbourne Breakfast",
#     "Chai",
#     "Peppermint",
#     "Lemon and Ginger",
#     "Strawberry Cream",
#     "Chamomile",
#     "Green",
#     "Dandelion"
# ]
# print(type(tea_collection))
# for tea in tea_collection:
#     print(tea)
#     print(type(tea))
   

# tea_collection = [
#     ["Black", "Earl Grey", "Melbourne Breakfast", "Chai"],
#     ["Flavoured", "Peppermint", "Lemon and Ginger", "Strawberry Cream"],
#     ["Health", "Chamomile", "Green", "Dandelion"]
# ]
# for tea_category in tea_collection:
#     print(f"{tea_category[0]} Teas:")
#     for tea in tea_category[1:]:
#         print(f"       {tea}")

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]

# for item in groceries:
#     print(f"{item[0]:>20}${item[1]: .2f}")

# num1 = input("Enter a number: ")
# while True:
#     if num1 == "":
#         break
# else: num2 = input("Enter another number: ")
#     results = float(num1) + float(num2)
# print(results)


mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"], ["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]


for item in mailing_list:
 print(f"{item[0]} : {item[1]}")