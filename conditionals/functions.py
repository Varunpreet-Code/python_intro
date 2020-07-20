def addition(a, b):
    #print(first_number)
    #print(f"a: {a}, b: {b}")
    results = float(a) + float(b)
    #print(results)
    return results
    


# a = 3
# b = 5
# addition(a, b)
# addition(12,17)
# addition_result = addition(b,a)
# print(addition_result)


    

#addition(2, 3)
#addition(4, 5)
#ddition(6, 8)

#first_number = input("Pick a number: ")
#second_number = input("Pick a nmber: ")
#addition(first_number, second_number)

#def is_odd(number):
   # if number%2 == 0:
    #    return False
    #else:
     #   return True



#counter = 5
#while counter > 0:
 #   if counter%2 == 0:
  #      print(f"{counter} is an odd number.")
    #else:
  #      print(f"{counter} is an even number.")
   # counter -= 1



# def format_grocery_item(item_name, item_cost):
#     return f"{item_name :<20} ${item_cost: .2f}"


#     groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]
# for item_ingroceries:
#     print(format_grocery_item(item[0], item[1]))


##################################
# def f_to_c(temp1):
#     temp = (temp1 - 32)*5/9
#     return temp


# temp1 = [32, 113, 26.6]
# for i in temp1:
#     print(f"{i}C = {f_to_c(i)}F")



number = []
new_number_string = input("Type a number to add: ")

while len(new_number_string) > 0:
    new_number = int(new_number_string)
    number.append(new_number)
    new_number_string = input("Type a number to add: ")

mean = sum(number)/len(number)
print("The average of the numbers is {mean}")