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
# Code lại, hàm quá rối.
# Mỗi hàm làm một việc thôi.
# -> Fixed
def process_sum_area_of_circles(file_name: str):
    lines = get_lines_from_file(file_name)
    total_area = calculate_total_area_from_lines(lines)
    write_area_to_file('output1.txt', total_area)

def get_lines_from_file(input_file: str) -> Union[str, list[str]]:
    try:
        with open(input_file, 'r') as file:
            size = int(file.readline())
            lines = file.readlines()
            return lines
    except FileNotFoundError as error:
        return str(error.strerror + ': ' + error.filename)

def calculate_total_area_from_lines(lines: list[str]) -> float:
    total_area = 0
    for line in lines:
        center_x, center_y, radius = line.split()
        area = math.pi * float(radius) * float(radius)
        total_area += area
    return total_area

def write_area_to_file(output_file: str, area: float):
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

# Code lại, hàm quá rối.
# -> Fixed
def sort_dates(file_name: str):
    lines = get_lines_from_file(file_name)
    string_dates = get_string_dates_from_lines(lines)
    sorted_dates = sort_date(string_dates)
    write_dates_to_file('output2.txt', sorted_dates)

def get_string_dates_from_lines(lines: str):
    return [line.strip() for line in lines]

def sort_date(string_dates):
    return sorted(string_dates)

def write_dates_to_file(output_file: str, dates: list[str]) -> None:
    with open(output_file, 'w') as file:
        for date in dates:
            file.write(date + '\n')

if __name__ == '__main__':
    print('I. CS162 Week 01:')
    print('1. Sum of area of circles - Printed to output1.txt')
    process_sum_area_of_circles('input1.txt')

    print('2. Sorted dates - Printed to output2.txt')
    sort_dates('input2.txt')
