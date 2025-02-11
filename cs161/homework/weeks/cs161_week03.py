import arrow
import calendar

from common.validator import Validator


class CS161Week03:
    @classmethod
    def call(cls) -> None:
        print('II. CS161 Week 02:')
        print('1. Passed or Failed:')
        params = {
            'assignment': 8,
            'lab': 9,
            'final': 10,
            'cheating': 0
        }
        print(CS161Week03.__passed(**params))

        print('2. Leap Year:')
        print(CS161Week03.__leap_year(2000))

        print('3. Days in Month:')
        params = {
            'month': 12,
            'year': 2020,
        }
        print(CS161Week03.__days_in_month(**params))

        params['day'] = 18
        print('4. Tomorrow:')
        print(CS161Week03.__tomorrow(**params))

        params['type'] = 'C'
        print('5. Rental:')
        print(CS161Week03.__rent(**params))

    @classmethod
    def __passed(cls, **kwargs) -> str:
        def validate(args):
            for key in ['assignment', 'lab', 'final']:
                if not (0 <= args[key] <= 10):
                    raise ValueError(f'{key} must be between 0 and 10')

            if not (0 <= args['cheating'] <= 1):
                raise ValueError('Cheating must be 0 or 1')

        try:
            validate(kwargs)
            grade = (kwargs['assignment'] * 0.3) + (kwargs['lab'] * 0.3) + (kwargs['final'] * 0.4)
            rounded_grade = round(grade, 1)

            if kwargs['cheating'] == 1:
                return f'{rounded_grade} FAILED'

            if grade < 5:
                return f'{rounded_grade} FAILED'
            else:
                return f'{rounded_grade} PASSED'
        except ValueError as e:
            return str(e)
        except KeyError as error:
            return f'Missing keyword argument: {str(error)}'

    @classmethod
    def __leap_year(cls, year):
        def validate(valid_year):
            if not (0 < valid_year <= 10 ** 9):
                raise ValueError('Year must be greater than 0 and less than 10^9')

        validate(year)
        if year % 400 == 0:
            return 'Nam nhuan'

        if year % 100 == 0 and year % 4 != 0:
            return 'Nam nhuan'
        else:
            return 'Khong phai nam nhuan'

    @classmethod
    def __days_in_month(cls, **kwargs):
        def validate(args):
            if not (1 <= args['month'] <= 12):
                raise ValueError('Month must be between 1 and 12')

            if not (0 < args['year'] <= 10 ** 9):
                raise ValueError('Year must be greater than 0 and less than 10^9')

        try:
            validate(kwargs)
            days = calendar.monthrange(**kwargs)[1]
            return days
        except ValueError as error:
            return str(error)
        except KeyError as error:
            return f'Missing keyword argument: {str(error)}'

    @classmethod
    def __tomorrow(cls, **kwargs):
        try:
            Validator.validate_date(**kwargs)
            date = arrow.get(**kwargs)
            tomorrow = date.shift(days=1)
            return tomorrow.format('DD MM YYYY')
        except ValueError as error:
            return str(error)
        except KeyError as error:
            return f'Missing keyword argument: {str(error)}'

    @classmethod
    def __rent(cls, **kwargs):
        def validate(args):
            if not (0 < args['day'] <= 10 ** 9):
                raise ValueError('Day must be greater than 0 and less than 10^9')

            if args['type'] not in ('A', 'B', 'C'):
                raise ValueError('Type must be A, B or C')

        try:
            validate(kwargs)
            rental_type = {
                'A': {'price': 450000, 'tax': 0.1},
                'B': {'price': 350000, 'tax': 0.08},
                'C': {'price': 25000, 'tax': 0.08},
            }
            before_tax = rental_type[kwargs['type']]['price'] * kwargs['day']
            if kwargs['day'] > 12:
                tax = before_tax * rental_type[kwargs['type']]['tax']
                return before_tax - tax
            else:
                return before_tax
        except ValueError as error:
            return str(error)
        except KeyError as error:
            return f'Missing keyword argument: {str(error)}'
