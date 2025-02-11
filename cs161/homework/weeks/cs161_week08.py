class CS161Week08:
    @classmethod
    def call(cls):
        print('VIII. CS161 Week 08:')
        print('1. Integer to string:')
        print(CS161Week08.__integer_to_string(1234567890))

    @classmethod
    def __integer_to_string(cls, number: int) -> str:
        return f'{number:,}'

    @classmethod
    def __process_string(cls, string: str) -> str:
        sentence = string.replace(' ', ',')
        print(sentence)
