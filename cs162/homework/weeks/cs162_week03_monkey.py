import sys

'''
Assignment 9
A local zoo wants to keep track of how many pounds of food each of its n monkeys eats each day during
a typical week. 

Write a program that stores this information in a two-dimensional n × 7 array, where each
row represents a different monkey and each column represents a different day of the week. 

The program should first have the user input the data for each monkey. 
Then it should create a report that includes the following information:

+ Average amount of food eaten per day by the whole family of monkeys.
+ The least amount of food eaten during the week by any one monkey.
+ The greatest amount of food eaten during the week by any one monkey.
Input Validation: Do not accept negative numbers for pounds of food eaten.
'''

def get_food_data(monkey_count: int) -> list[list[float]]:
    data = []
    for index in range(monkey_count):
        monkey_data = []
        print(f'Enter food consumption for Monkey {index + 1}:')
        input_monkey_data(monkey_data)
        data.append(monkey_data)
    return data

def input_monkey_data(monkey_data: list[float]) -> None:
    for index in range(7):
        while True:
            try:
                food = float(input(f'Day {index + 1}: '))
                if food < 0:
                    print('Food consumption cannot be negative. Please enter a non-negative value.')
                else:
                    monkey_data.append(food)
                    break
            except ValueError:
                print('Invalid input. Please enter a valid number.')

def calculate_average_food_consumption(data: list[list[float]]) -> float:
    total_food = 0
    total_monkeys = len(data)
    total_days = 7

    for monkey in food_data:
        total_consumed_food_monkey = sum(monkey)
        total_food += total_consumed_food_monkey

    average_food = total_food / (total_monkeys * total_days)
    return average_food


def find_least_food_consumed(data: list[list[float]]) -> float:
    min_food = sys.maxsize
    for monkey in data:
        total_consumed_food_monkey = sum(monkey)
        min_food = min(min_food, total_consumed_food_monkey)
    return min_food


def find_greatest_food_consumed(data: list):
    max_food = -sys.maxsize - 1
    for monkey in data:
        total_consumed_food_monkey = sum(monkey)
        max_food = max(max_food, total_consumed_food_monkey)
    return max_food


if __name__ == '__main__':
    while True:
        try:
            number_of_monkeys = int(input('Enter the number of monkeys: '))
            if number_of_monkeys <= 0:
                print('The number of monkeys must be greater than zero.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    food_data = get_food_data(number_of_monkeys)
    average_amount = calculate_average_food_consumption(food_data)
    least_amount = find_least_food_consumed(food_data)
    greatest_amount = find_greatest_food_consumed(food_data)

    print(f'\nAverage food eaten per day by the whole family of monkeys: {average_amount:.2f} pounds')
    print(f'The least amount of food eaten by any monkey during the week: {least_amount:.2f} pounds')
    print(f'The greatest amount of food eaten by any monkey during the week: {greatest_amount:.2f} pounds')
