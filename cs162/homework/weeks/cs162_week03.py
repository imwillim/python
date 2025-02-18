from statistics import median
from typing import Union

from cs162.homework.weeks.cs162_week01 import get_lines_from_file

'''
Assignment 1:

In statistics, when a set of values is sorted in ascending or descending order, its median is the middle
value. If the set contains an even number of values, the median is the mean, or average, of the two
middle values. Write a function that accepts as arguments the following:
A) An array of integers
B) An integer that indicates the number of elements in the array
The function should determine the median of the array. This value should be returned as a double.
(Assume the values in the array are already sorted.)
'''


def get_median(array: list[int], size: int) -> float:
    middle = size // 2

    if size % 2 == 1:
        return array[middle]

    mid_1 = array[middle - 1]
    mid_2 = array[middle]
    return (mid_1 + mid_2) / 2


'''
Assignment 2:

Write a function that accepts an int array and the array’s size as arguments. The function should create
a new array that is twice the size of the argument array. The function should copy the contents of the
argument array to the new array and initialize the unused elements of the second array with 0.
'''


def double_array(array: list[int], size: int) -> list[int]:
    double_size = 2 * size
    new_array = [0] * double_size

    for index in range(size):
        new_array[index] = array[index]
    return new_array


'''
Assignment 3

One of your professors has asked you to write a program to grade her final exams, which consist of only
20 multiple-choice questions. Each question has one of four possible answers: A, B, C, or D. The file
CorrectAnswers.txt contains the correct answers for all of the questions, with each answer written on a
separate line.
• The first line contains the number of answers.
• The second line contains the answer to the first question
• The third line contains the answer to the second question, and so forth.

Write a program that reads the contents of the CorrectAnswers.txt file into a char array, and then reads
the contents of another file, containing a student’s answers, into a second char array
StudentAnswers.txt (the format of StudentAnswers.txt is the same as CorrectAnswers.txt).

The program should determine the number of questions that the student missed and then display the
following:
• A list of the questions missed by the student, showing the correct answer and the incorrect answer
provided by the student for each missed question
• The total number of questions missed
• The percentage of questions answered correctly. This can be calculated as
    Correctly Answered Questions / Total Number of Questions

If the percentage of correctly answered questions is 70% or greater, the program should indicate that the
student passed the exam. Otherwise, it should indicate that the student failed the exam.    
'''


def process_answer():
    student_answers = get_answers_from_file('StudentAnswers.txt')
    correct_answers = get_answers_from_file('CorrectAnswers.txt')
    total_answer_count = len(correct_answers)

    print_answers(student_answers, correct_answers)
    print_answers_with_wrong_answers(student_answers, correct_answers, total_answer_count)


def get_answers_from_file(file_name: str) -> list[str]:
    answers_lines = get_lines_from_file(file_name)
    return get_answers_from_lines(answers_lines)


def get_answers_from_lines(answer_lines: str) -> list[str]:
    return [line.strip() for line in answer_lines]


def print_answers(student_answers, correct_answers):
    print('---Process answer of student----')
    wrong_answers = get_wrong_answers(student_answers, correct_answers)
    print('I.a Correct answers:', correct_answers)
    print('I.b Wrong answers:', wrong_answers)


def print_answers_with_wrong_answers(student_answers: list[str], correct_answers: list[str], total_answer_count: int):
    wrong_answers = get_wrong_answers(student_answers, correct_answers)

    filtered_wrong_answers = [answer for answer in wrong_answers if answer != ""]
    wrong_answer_count = len(filtered_wrong_answers)
    print('II. The total number of questions missed:', wrong_answer_count)

    correct_answer_count = total_answer_count - wrong_answer_count
    correct_percentage = (correct_answer_count / total_answer_count) * 100
    print('III. Percentage of questions answered correctly:', correct_percentage)

    result = 'PASSED' if correct_percentage >= 0.7 else 'FAILED'
    print('IV. CONCLUSION: Student ', result)


def get_wrong_answers(student_answers: list[str], correct_answers: list[str]) -> list[str]:
    wrong_answers = []
    for index in range(len(student_answers)):
        if student_answers[index] == correct_answers[index]:
            wrong_answers.append('')
        else:
            wrong_answers.append(student_answers[index])
    return wrong_answers


if __name__ == '__main__':
    print('III. CS162 Week 03:')
    print('1. Median:', get_median([1, 2, 3, 4, 5], 5))
    print('2. Double array:', double_array([1, 2, 3, 4, 5], 5))
    print('\n3. Read answer:')
    process_answer()
