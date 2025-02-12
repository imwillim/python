from typing import Union
import arrow

from common.utils import validate_date


def absolute_day(**kwargs) -> str:
    try:
        validate_date(**kwargs)
        date = arrow.get(**kwargs)
        tomorrow = date.shift(days=-1)
        return tomorrow.format('DD MM YYYY')
    except ValueError as error:
        return str(error)


def minus_days(**kwargs) -> str:
    def validate(args):
        if not (0 < args['minus_day'] <= 10 ** 9):
            raise ValueError('Minus day must be greater than 0 and less than 10^9')

    try:
        validate_date(**kwargs)
        validate(kwargs)
        date = arrow.get(**kwargs)
        tomorrow = date.shift(days=-kwargs['minus_day'])
        return tomorrow.format('DD MM YYYY')
    except ValueError as error:
        return str(error)


def day_difference(**kwargs) -> Union[str, int]:
    try:
        validate_date(**kwargs['first_day'])
        validate_date(**kwargs['second_day'])

        first_day = arrow.get(**kwargs['first_day'])
        second_day = arrow.get(**kwargs['second_day'])
        difference = first_day - second_day
        return difference.days
    except ValueError as error:
        return str(error)


if __name__ == '__main__':
    print('IV. CS161 Week 04:')
    params = {
        'day': 1,
        'month': 12,
        'year': 2020
    }
    print('1. Absolute day:')
    print(absolute_day(**params))

    params['minus_day'] = 10
    print('2. Minus days:')
    print(minus_days(**params))

    print('3. Day difference:')
    params['first_day'] = {
        'day': 1,
        'month': 12,
        'year': 2020
    }

    params['second_day'] = {
        'day': 15,
        'month': 8,
        'year': 2020
    }

    print(day_difference(**params))
