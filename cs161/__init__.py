from cs161.homework.weeks.cs161_week01 import CS161Week01
from cs161.homework.weeks.cs161_week03 import CS161Week03
from cs161.homework.weeks.cs161_week04 import CS161Week04
from cs161.homework.weeks.cs161_week08 import CS161Week08


class CS161Homework:
    @classmethod
    def call(cls):
        print('CS161 Homework:')
        CS161Week01.call()
        CS161Week03.call()
        CS161Week04.call()
        CS161Week08.call()