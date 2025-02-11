from typing import Union, Any

class CS161Week01:
    @classmethod
    def call(cls) -> None:
        print('I. CS161 Week 01:')
        print('1. Divide exercise:')
        print(CS161Week01.__divide(10, 0))

        print('\n2. Electric consumption:')
        print(CS161Week01.__electric_consumption(10, 15))

        print('\n3. Age calculation:')
        print(CS161Week01.__calculate_age(2020))

        print('\n4. Package calculation:')
        print(CS161Week01.__calculate_package(1000, 10))

        print('\n5. Money conversion:')
        print(CS161Week01.__convert_money_vnd(10024000))

    @classmethod
    def __divide(cls, first_integer: int, second_integer: int) -> Union[str, float]:
        def validate(divisor: int) -> None:
            if divisor == 0:
                raise ValueError('Divisor cannot be 0')

        try:
            validate(second_integer)
            return first_integer / second_integer
        except ValueError as exception:
            return str(exception)

    @classmethod
    def __electric_consumption(cls, previous: int, current: int) -> Union[str, int]:
        def validate(start: int, end: int) -> None:
            if start > end:
                raise ValueError('Previous must not be greater than current')
            if start < 0:
                raise ValueError('Previous must be greater than 0')
            elif start > 10 ** 9:
                raise ValueError('Previous must be less than 10^9')

        try:
            validate(previous, current)
            return current - previous
        except ValueError as exception:
            return str(exception)

    @classmethod
    def __calculate_age(cls, age) -> Union[Union[str, int], Any]:
        def validate(year: int) -> None:
            if year > 2025:
                raise ValueError('Age must not be greater than 2025')

        try:
            validate(age)
            return 2025 - age
        except ValueError as exception:
            return str(exception)

    @classmethod
    def __calculate_package(cls, price, quantity) -> Union[Union[str, float], Any]:
        def validate(money: int, amount: int) -> None:
            if money < 0:
                raise ValueError('Price must not be less than 0')

            if amount < 0:
                raise ValueError('Amount must not be less than 0')

        try:
            validate(price, quantity)
            before_tax = price * quantity
            tax = before_tax * 0.1
            return before_tax - tax
        except ValueError as exception:
            return str(exception)

    @classmethod
    def __convert_money_vnd(cls, money: int) -> str:
        def validate(cash: int) -> None:
            if money % 500 != 0:
                raise ValueError('Money must be in VND')

            if cash < 0:
                raise ValueError('Money must not be less than 0')
            if cash > 10 ** 9:
                raise ValueError('Money must not be greater than 10^9')

        try:
            validate(money)
            ratio_chart = {500000: 0,
                           200000: 0,
                           100000: 0,
                           50000: 0,
                           20000: 0,
                           10000: 0,
                           5000: 0,
                           2000: 0,
                           1000: 0,
                           500: 0}
            for ratio in ratio_chart:
                if money >= ratio:
                    ratio_chart[ratio] = money // ratio
                    money %= ratio

            chart = str()
            for ratio, count in ratio_chart.items():
                chart += f'{ratio}: {count}\n'
            return chart
        except ValueError as exception:
            return str(exception)
