def validate_date(**kwargs):
    if not (1 <= kwargs['day'] <= 31):
        raise ValueError('Day must be between 1 and 31')

    if not (1 <= kwargs['month'] <= 12):
        raise ValueError('Month must be between 1 and 12')

    if not (0 < kwargs['year'] <= 10 ** 9):
        raise ValueError('Year must be greater than 0 and less than 10^9')
