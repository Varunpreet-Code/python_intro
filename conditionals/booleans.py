# Booleans
print("AND Comparisons:")
is_raining = False
is_cold = False
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)
is_raining = False
is_cold = True
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)
is_raining = True
is_cold = False
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)
is_raining = True
is_cold = True
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)
print("OR Comparisons:")
is_raining = False
is_cold = False
print(is_raining or is_cold, is_raining or not is_cold)
is_raining = False
is_cold = True
print(is_raining or is_cold, is_raining or not is_cold)
is_raining = True
is_cold = False
print(is_raining or is_cold, is_raining or not is_cold)
is_raining = True
is_cold = True
print(is_raining or is_cold, is_raining or not is_cold)


    
light_colour = "Red"
    car_detected = False
    if light_colour == "Red" and not car_detected:
      print("Do nothing.")
    elif light_colour == "Red" and  car_detected:
      print("Flash")
    elif light_colour == "Green" and not car_detected:
      print("Do Nothing")
    elif light_colour == "Green" and  car_detected:
      print("Do nothing")
    elif light_colour == "Amber" and not car_detected:
      print("Do nothing")
    else light_colour == "Amber" and car_detected:
      print("Do nothing")