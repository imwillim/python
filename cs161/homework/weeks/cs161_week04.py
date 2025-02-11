from datetime import timedelta
from typing import Union

import arrow

from common.validator import Validator


class CS161Week04:
    @classmethod
    def call(cls):
        print('IV. CS161 Week 04:')
        params = {
            'day': 1,
            'month': 12,
            'year': 2020
        }
        print('1. Absolute day:')
        print(CS161Week04.__absolute_day(**params))

        params['minus_day'] = 10
        print('2. Minus days:')
        print(CS161Week04.__minus_days(**params))

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

        print(CS161Week04.__day_difference(**params))

    @classmethod
    def __absolute_day(cls, **kwargs) -> str:
        try:
            Validator.validate_date(**kwargs)
            date = arrow.get(**kwargs)
            tomorrow = date.shift(days=-1)
            return tomorrow.format('DD MM YYYY')
        except ValueError as error:
            return str(error)

    @classmethod
    def __minus_days(cls, **kwargs) -> str:
        def validate(args):
            if not (0 < args['minus_day'] <= 10 ** 9):
                raise ValueError('Minus day must be greater than 0 and less than 10^9')

        try:
            Validator.validate_date(**kwargs)
            validate(kwargs)
            date = arrow.get(**kwargs)
            tomorrow = date.shift(days=-kwargs['minus_day'])
            return tomorrow.format('DD MM YYYY')
        except ValueError as error:
            return str(error)

    @classmethod
    def __day_difference(cls, **kwargs) -> Union[str, int]:
        try:
            Validator.validate_date(**kwargs['first_day'])
            Validator.validate_date(**kwargs['second_day'])

            first_day = arrow.get(**kwargs['first_day'])
            second_day = arrow.get(**kwargs['second_day'])
            difference = first_day - second_day
            return difference.days
        except ValueError as error:
            return str(error)
