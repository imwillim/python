import math
import arrow
from arrow import Arrow
from typing import Union, Any

'''
Assignment 1
Write a program to load an array of circles.
Sum of their area and save the result to another text file.

# input.txt
3
3 4 1.2
-4 5 4.6
1 2 7.0

Note: 3 4 1.2 means a circle with center point is at (3,4) and radius is 1.2
'''
# Hàm này làm gì trả về gì đâu mà define rtype.
def sum_area_of_circles(file_name: str) -> Union[Union[str, float], Any]:
    result = get_total_area(file_name)
    write_area_to_file('output1.txt', result)

# Code lại, hàm quá rối.
# Mỗi hàm làm một việc thôi.
def get_total_area(input_file: str) -> Union[str, Any]:
    try:
        with open(input_file, 'r') as file:
            size = int(file.readline())
            lines = file.readlines()
            total_area = 0.0
            for line in lines:
                center_x, center_y, radius = line.split()
                area = math.pi * float(radius) * float(radius)
                total_area += area
            return total_area
    except FileNotFoundError as error:
        return str(error.strerror + ': ' + error.filename)

def write_area_to_file(output_file: str, area: float) -> None:
    with open(output_file, 'w') as file:
        file.write(str(area))

'''
Assignment 2
Write a program to load an array of dates.
Sort the array in ascending order and save the array to another text file.

# input.txt
3
2019 01 04
2019 12 31
2019 01 15
'''
def sort_dates(file_name: str) -> Union[str, Any]:
    sorted_dates = get_sorted_dates(file_name)
    write_dates_to_file('output2.txt', sorted_dates)

# Code lại, hàm quá rối.
def get_sorted_dates(input_file: str) -> Union[str, list[Arrow]]:
    try:
        with open(input_file, 'r') as file:
            size = int(file.readline())
            lines = file.readlines()
            dates = []
            for line in lines:
                year_string, month_string, day_string = line.split()
                year = int(year_string)
                month = int(month_string)
                day = int(day_string)
                date = arrow.get(year, month, day)
                dates.append(date)
            return sorted(dates)
    except FileNotFoundError as error:
        return str(error.strerror + ': ' + error.filename)

def write_dates_to_file(output_file: str, dates: list[Arrow]) -> None:
    with open(output_file, 'w') as file:
        for date in dates:
            file.write(date.format('DD MM YYYY') + '\n')

if __name__ == '__main__':
    print('I. CS162 Week 01:')
    print('1. Sum of area of circles - Printed to output1.txt')
    sum_area_of_circles('input1.txt')

    print('2. Sorted dates - Printed to output2.txt')
    sort_dates('input2.txt')
