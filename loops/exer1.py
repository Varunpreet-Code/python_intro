


# num1 = input("Enter a number: ")
# num2 = input("Enter a another number")
# while True:
#     if num1 and num2 == "":
# #         break
    
# #     results = float(num1) + float(num2)
# # print(results)

# import json
# with open("data/quiz.json") as json_file:
#     json_data = json.load(json_file)
    
# quiz = json_data["quiz"] 


# for number, item in quiz.items():
#     print(f"Question {number}: " + item["question"])
#     for options in item["options"]:
#         print("      " + options)



groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]


total = 0
for item in groceries:
    quantity = input(f"how many units {item[0]} would you buy? ")
    item[1] = item[1] * int(quantity)
    total += item[1]
total = f"${total:.2f}"
print("====Izzy's Food Emporium====")
for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}")
print("============================")
print(f"{total:>27}")