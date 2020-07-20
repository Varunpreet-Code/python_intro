import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    celsius = (temp_in_farenheit -32) * 5.0/9.0
    celsius =round(celsius, 1)
    return celsius


def calculate_mean(total, num_items):
    return round(total/num_items,1)


    

    """Calculates the mean.


    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    



def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)



        min_temp = []
        max_temp = []
        date = []
        desc = []
        rain_chance = []
        desc_pm = []
        rain_chance_pm =[]

        for weather in json_data["DailyForecasts"]:
            min_temp.append(convert_f_to_c(weather["Temperature"] ["Minimum"] ["Value"]))
            max_temp.append(convert_f_to_c(weather["Temperature"] ["Maximum"] ["Value"]))
            date.append(convert_date(weather["Day"]))
            
            desc.append(weather["Day"]["LongPhrase"])
            rain_chance.append(weather["Day"]["RainProbability"])
            desc_pm.append(weather["Night"]["LongPhrase"])
            rain_chance_pm.append(weather["Night"]["RainProbability"])


            mean_min_c = sum(min_temp) / len(min_temp)
            mean_min = format_temperature(mean_min_c)

            mean_max_c = sum(max_temp) / len(max_temp)
            mean_max = format_temperature(mean_max_c)

            min_index = min_temp.index(min(min_temp))
            low_day = date [min_index]

            max_index = max_temp.index(max(max_temp))
            high_day = date [max_index]


        final_output1 = f"""5 Day Overview\n\tThe lowest temperture will be {min(min_temp)}, and will occur on {low_day}
            \n\tThe highest temperature will be {max(max_temp)}, and will occur on {high_day}\n\tThe average low this week is {mean_min}\n\tThe average high this week is {mean_max}\n"""

        final_output2 = ""
        for x in range(5):

            

    final_output2 = final_output2 + (f"""-------{date[x]}----------\nMinimum Temperture:{min_temp[x]}\nMaximum
            Temperature:{max_temp[x]}\nDaytime:{desc[x]}\n\tChance of rain:\t{rain_chance[x]}%\nNighttime: {desc_pm[x]}
            \n\tChance of rain:\t {rain_chance_pm[x]}%\n""")
        final_final_output = final_output1 + final_output2
        return final_final_output







#     day = []
#     date = []
#     min_temp = []
#     max_temp = []
#     mean_min_result = []
#     daytime = []
#     nightime = []
#     rain_chance_pm = []

#     weather_results: [
# "day",
# "time",
# "min_temp",
# "max_temp",
# "day_time",
# "night_time",
# "day_rain_chance",
# "night_rain_chance"
# "mean_result"
# ] 

   
#     for items in json_data["DailyForecasts"]:
#       DailyForecasts =[]
#     total_min_result = 0
#     counter = 0
#     total_max_result = 0
#     for items in json_data["DailyForecasts"]:

#         min_temp.append(convert_f_to_c(items["Temperature"] ["Minimum"] ["Value"]))
#         max_temp.append(convert_f_to_c(items["Temperature"] ["Minimum"] ["Value"]))
#         total_min_result = total_min_result + (convert_f_to_c(items["Temperature"] ["Minimum"] ["Value"]))
#         counter = counter + 1
#         total_max_result = total_max_result + (convert_f_to_c(items["Temperature"] ["Minimum"] ["Value"]))
#         date_time.append(convert_date(items["date"]))
#         night_time.append(items["date"] ["Moon"])
#         day_rain_chance(items["day"]["RainProbability"])
#         night_rain_chance(items["night"]["RainProbability"])



#     mean_min_result = calculate_mean(total_min_result, counter)
#     mean_max_result = calculate_mean(total_max_result, counter)
#     num_days = len(json_data["DailyForecasts"])
#     return f"{num_days} Day Overview"f"""5 Day Overview\n\tThe lowest temperture will be {mean_min(min_temp)}, and will occur on {low_day}\n\tThe highest temperature will be {mean_max(max_temp)}, and will occur on {high_day}\n\tThe average low this week is {mean_min}\n\tThe average high this week is {mean_max}\n"""
        
    
    
                  
# #     final_output2 = ""
# # for x in range(5):
# #     final_output2 = final_output2 + (f"-------- {date[x]} ----------\n minimum")

       


    
    # print("--------" + items["Date"] + "--------")
    # print("Minimum Temperature: " + items["Temperature"]["Minimum"]["ValueString"])
    # print("Maximum Temperature: " + items["Temperature"]["Maximum"]["ValueString"])
       

    #print(json_data)       
    print(calculate_mean(200,5))


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))