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
    return(temp_in_farenheit*9/5) + 32


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = total/num_items

    return mean



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

    date = []
    min_temp = []
    max_temp = []
    day_time = []
    rain_chance = []
    night_time = []
    rain_chance = []

    #for items in json_data["DailyForecasts"]:
     
daystring = ""
for forecast in json_data["DailyForecasts"]:
        daystring = daystring + f'\n\n-------- {convert_date(forecast["Date"])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(forecast["Temperature"]["Minimum"]["Value"]))}\nMaximum Temperature: {format_temperature(convert_f_to_c(forecast["Temperature"]["Maximum"]["Value"]))}\nDaytime: {forecast["Day"]["LongPhrase"]}\n    Chance of rain:  {forecast["Day"]["RainProbability"]}%\nNighttime: {forecast["Night"]["LongPhrase"]}\n    Chance of rain:  {forecast["Night"]["RainProbability"]}%'
        return f'{num_days_in_data} Day Overview\n    The lowest temperature will be {format_temperature(min_list[0][0])}, and will occur on {min_list[0][1]}.\n    The highest temperature will be {format_temperature(max_list[-1][0])}, and will occur on {max_list[-1][1]}.\n    The average low this week is {format_temperature(ave_min)}.\n    The average high this week is {format_temperature(ave_max)}.{daystring}'
        
        
        
        
        
        
        
    #print("--------" + items["Date"] + "--------")
        













    #print(json_data)       
    #print(calculate_mean(200,5))













if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





