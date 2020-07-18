groceries = {
    "Baby Spinach": 2.78,
    "Hot chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "carrots": 0.56,
    "oranges": 3.08,
}

print(groceries)

#print(groceries["Baby Spinach"])
#print(groceries["Crackers"])

groceries["Crackers"] = 2.50
#print(groceries)

groceries["Avocado"] = 1.00

for item in groceries:
    print(item)
    print(groceries[item])

print()


for item, price in groceries.items():
 print(item, price)



 cohorts = {
     "perth": ["Anna", "Viv", "Nic", "Teagen"],
     "Brisbane": ["TEagen","Vivian", "Nic","Joy"]
 }
 print(cohorts)

 for cohort, peeps in cohorts.items():
     print(cohort)
     for peep in peeps:
         print(peep)
         print()

all_cohorts = {
    2019: {
        "perth": ["Anna", "Sarah", "Nina", "Ellie"]
    },
    2020: {
        "perth": ["Anna", "Viv", "Nic", "Teagen"],
        "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
    }
}

#for year, cohorts in all_cohorts.items():
     print(year)
#for city, cohort in cohorts.items():
       # print(city, cohort)