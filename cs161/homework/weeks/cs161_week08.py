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
Ví dụ
    Input: 7546789876
    Output: 7,546,789,876
'''
# Đúng
def integer_to_string(number: int) -> str:
    return f'{number:,}'


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
    Input: n=3, string='Những quy tắc đạo đức có một vị trí rất quan trọng'
    Output:
        a. Những-quy-tắc-đạo-đức-có-một-vị-trí-rất-quan-trọng
        b. Những , quan , trọng
        c. Có, Những
'''
# Đúng, nhưng lần sau nên tách thành 3 hàm khác nhau. Mỗi hàm làm 1 việc.
# Hàm chỉ xử lý, việc in ra đáp án nên để trong hàm main.
# tên biến string giống keyword (của các ngôn ngữ khác) nên nên đổi tên biến khác.
# Nếu return None thì để trống, không cần tường minh.
def process_string(string: str, n: int) -> None:
    sentence = string.replace(' ', '-')
    print('a. ' + sentence)

    raw_sentence = string.split(' ')
    filtered_words = [word for word in raw_sentence if len(word) > n]
    print('b. ' + (', '.join(filtered_words)))

    min_word = min(raw_sentence, key=len)
    max_word = max(raw_sentence, key=len)

    print(f'c. {min_word}, {max_word}')

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
# Bài này không dùm hàm có sẵn, tự code.
# Đây là 1 trong các bài phỏng vấn. Bài gốc là chuẩn hoá chuỗi hoặc đếm từ (word)
def normalize_name(name) -> str:
    return name.strip().title()


if __name__ == '__main__':
    print('VIII. CS161 Week 08:')
    print('1. Integer to string:', integer_to_string(1234567890))

    print('\n2. Process string:')
    process_string('Những quy tắc đạo đức có một vị trí rất quan trọng', 3)

    print('\n3. Normalize name:', normalize_name(' nguyEn VAN aB '))
