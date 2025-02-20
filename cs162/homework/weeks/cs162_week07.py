'''
1. Recursion 22
sumOfDigits
You are given the following prototype

int sumOfDigits(int x)

Please implement this recursive function in order to
calculate the sum of all digits in the decimal representation of x.
'''


def sum_of_digits(integer: int) -> int:
    if integer == 0:
        return 0

    last_digit = integer % 10

    return last_digit + sum_of_digits(integer // 10)


'''
3.4 Recursion with array
a. Output the array of integer values to screen.
'''


def print_array(array, index=0):
    if index == len(array):
        return

    print(array[index], end=' ')
    print_array(array, index + 1)


'''
b. Output the array of integer values to screen in reversed order.
'''


def print_array_reversed(array, index=None):
    if index is None:
        index = len(array) - 1

    if index < 0:
        return

    print(array[index], end=' ')
    print_array_reversed(array, index - 1)


'''
c. Find the sum of positive numbers in the array.
'''


def sum_positive_numbers(array, index=0):
    if index == len(array):
        return 0

    if array[index] > 0:
        current_value = array[index]
    else:
        current_value = 0

    return current_value + sum_positive_numbers(array, index + 1)


'''
d. Count all distinct values in the array.
'''


def count_distinct(array, index=0, distinct_values=None):
    if distinct_values is None:
        distinct_values = set()

    if index == len(array):
        return len(distinct_values)

    distinct_values.add(array[index])

    return count_distinct(array, index + 1, distinct_values)


'''
e. Check whether the array only contains odd numbers.
'''


def contains_only_odd(array, index=0):
    if index == len(array):
        return True

    if array[index] % 2 == 0:
        return False

    return contains_only_odd(array, index + 1)


'''
f. Find the maximum value in the array.
'''


def find_max_value(array, index=0, current_max=None):
    if index == len(array):
        return current_max

    if current_max is None:
        current_max = array[index]

    if array[index] > current_max:
        current_max = array[index]

    return find_max_value(array, index + 1, current_max)


if __name__ == '__main__':
    print('III. CS162 Week 03:')

    number = 12345
    print(f'1. Sum of digits of {number}:', sum_of_digits(number))

    print('\n2. Recursion with array')

    numbers = [1, 1, 4, -4, -5, -6, 7, 8, 9]

    print('\na. Array elements:')
    print_array(numbers)

    print('\nb. Reversed array:')
    print_array_reversed(numbers)

    print('\nc. Sum of positive numbers:', sum_positive_numbers(numbers))
    print('d. Number of distinct values:', count_distinct(numbers))
    print('e. Does the array contain only odd numbers?', contains_only_odd(numbers))
    print('f. Maximum value in the array:', find_max_value(numbers))
