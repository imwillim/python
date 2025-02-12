import sys

'''
P01 - IN SỐ NGUYÊN Ở DẠNG CHUỖI
Mô tả
    Viết hàm nhập một số nguyên, xuất lại số đó ở dạng chuỗi nhưng có dấu „,‟ ngăn cách
    hàng ngàn, hàng triệu, hàng tỉ (tùy vào độ lớn của số nhập)
Dữ liệu đầu vào
    Dòng 1: Nhập 1 số nguyên 0<=n<=10^20
Dữ liệu đầu ra
    In chuỗi số có dấu thập phân
'''
def integer_to_string(number: int) -> str:
    def validate(input) -> None:
        if not (0 <= input <= 10 ** 20):
            raise ValueError('Number must be between 0 and 10^20')
    try:
        validate(number)
        return f'{number:,}'
    except ValueError as error:
        return str(error)

'''
P02 - XỬ LÝ CHUỖI
Mô tả
    Nhập một chuỗi S từ bàn phím chỉ bao gồm các ký tự chữ và khoảng trắng.
        a. In các từ trên mỗi hàng liên tiếp.
        b. Đếm xem có bao nhiêu từ có nhiều hơn n ký tự có trong chuỗi S.
        c. Tìm từ ngắn nhất và dài nhất
Dữ liệu đầu vào
    Tham số đầu tiên: Nhập chuỗi S chỉ có các ký tự chữ và khoảng trắng.
    Tham số thứ hai: nhập 0 < n <= 10^20
Dữ liệu đầu ra
    a. In các từ cách nhau dấu -
    b. In số từ có nhiều hơn n ký tự
    c. In từ ngắn nhất và dài nhất.
Ví dụ
    Input: 7546789876
    Output: 7,546,789,876
'''
def process_string(**kwargs) -> None:
    def validate(args) -> None:
        if not (0 < args['n'] <= 10 ** 9):
            raise ValueError('N must be between 0 and 10^9')

    try:
        validate(kwargs)
        sentence = kwargs['string'].replace(' ', '-')
        print(sentence)

        raw_sentence = kwargs['string'].split(' ')
        filtered_words = [word for word in raw_sentence if len(word) > kwargs['n']]
        print((", ".join(filtered_words)))

        min_word = min(raw_sentence, key=len)
        max_word = max(raw_sentence, key=len)

        print(f'{min_word}, {max_word}')
    except ValueError as error:
        print(error)
    except KeyError as error:
        print(f'Missing keyword argument: {str(error)}', file=sys.stderr)

'''
P03 - CHUẨN HÓA HỌ VÀ TÊN
Mô tả
    Viết hàm nhập vào một chuỗi. Thực hiện chuẩn hóa chuỗi đầu vào theo các nguyên tắc sau:
    + Mỗi chữ cách nhau bởi một khoảng trắng duy nhất.
    + Không có khoảng trắng ở đầu chuỗi và cuối chuỗi.
    + Chữ cái đầu từ của mỗi chữ phải viết hoa, các chữ cái còn lại trong chữ viết thường.
Dữ liệu đầu vào
    Một dòng duy nhất, chứa chuỗi là họ và tên của một người. Họ và tên bao gồm 2 chữ trở lên,
    mỗi chữ cách nhau bởi một hoặc nhiều dấu cách.
Dữ liệu đầu ra
    Chuỗi họ và tên đã được chuẩn hóa.
Ví dụ:
    Input: ' nguyEn VAN a '
    Output: 'Nguyen Van A'
'''
def normalize_name(name) -> str:
    return name.strip().title()

if __name__ == '__main__':
    print('VIII. CS161 Week 08:')
    print('1. Integer to string:')
    print(integer_to_string(1234567890))

    print('\n2. Process string:')
    params = {
        'string': 'Những quy tắc đạo đức có một vị trí rất quan trọng',
        'n': 3
    }
    process_string(**params)

    print('\n3. Normalize name:')
    print(normalize_name(' nguyEn VAN a '))
