'''
Your task is to implement a simple logger using Singleton Design Pattern,
Link: https://www.mkyong.com/logging/log4j-hello-world-example/
to log to a text log file (text file).
'''
import arrow


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def log(self, message: str, level: str = 'INFO'):
        timestamp = arrow.Arrow.utcnow().format('YYYY-MM-DD HH:mm:ss')
        log_message = f'[{timestamp}] [{level}] {message}\n'

        with open('log.txt', 'a') as file:
            file.write(log_message)

        print(log_message.strip())


if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()

    print('Logger1 and Logger2 are similar, True or False ? ->', logger1 is logger2, end='\n\n')

    logger1.log('This is an info message.')
    logger1.log('This is a warning message.', level='WARNING')
    logger1.log('This is an error message.', level='ERROR')
