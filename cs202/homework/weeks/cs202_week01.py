'''
class Fraction
a. input
b. output
c. reduce
d. add
e. subtract
f. multiply
g. divide
h. compare
i. sign: less than 0, equal to 0 or greater than 0
'''


def gcd(x, y):
    while y != 0:
        # x = y
        # y = x % y
        x, y = y, x % y

    return x


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator

    def reduce(self):
        common_divisor = gcd(self.numerator, self.denominator)

        self.numerator = self.numerator // common_divisor
        self.denominator = self.denominator // common_divisor

    def __str__(self):
        if self.numerator == 0:
            return '0'

        if self.denominator < 0:
            return f'-{self.numerator}/{self.denominator * -1}'

        return f'{self.numerator}/{self.denominator}'

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return Fraction(new_numerator, new_denominator)

    def compare(self, other) -> int:
        left = self.numerator * other.denominator
        right = other.numerator * self.denominator

        if left == right:
            return 0

        if left > right:
            return 1

        return -1

    def sign(self) -> str:
        if self.numerator == 0:
            return 'Equal to 0'

        if self.denominator > 0 and self.numerator > 0:
            return 'Greater than 0'

        return 'Less than 0'




if __name__ == '__main__':
    fraction_1 = Fraction(-1, 2)
    fraction_2 = Fraction(1, 4)
    fraction_3 = Fraction(2, -4)

    print('Output of fraction 1:', fraction_1)
    print('Output of fraction 2:', fraction_2)
    print('Output of fraction 3:', fraction_3, end='\n\n')

    fraction_3.reduce()
    print(f'Reduced of fraction 3:', fraction_3, end='\n\n')

    print(f'{fraction_1} + {fraction_2} =', fraction_1.add(fraction_2))
    print(f'{fraction_1} - {fraction_2} =', fraction_1.subtract(fraction_2))
    print(f'{fraction_1} * {fraction_2} =', fraction_1.multiply(fraction_2))
    print(f'{fraction_1} / {fraction_2} =', fraction_1.divide(fraction_2), end='\n\n')

    print(f'Compare {fraction_1} of {fraction_2}:', fraction_1.compare(fraction_2), end='\n\n')

    print(f'Sign of {fraction_1}:', fraction_1.sign())
    print(f'Sign of {fraction_2}:', fraction_2.sign())
