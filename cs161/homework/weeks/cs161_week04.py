from typing import Union
import arrow

'''
P01 - SỐ THỨ TỰ TUYỆT ĐỐI CỦA NGÀY
Mô tả
    Viết chương trình nhập vào 1 ngày.
    Tính số thứ tự tuyệt đối của ngày, tính từ mốc 1/1/1970.
Dữ liệu đầu vào
    Một dòng duy nhất, 3 số nguyên dương, day, month, year.
    Trong đó:
        1 <= day <= 28, 29, 30, 31 tuỳ month
        1 <= month <= 12
        1 <= year <= 10^9
Dữ liệu đầu ra
    Số thứ tự của ngày trong năm
Ví dụ
    Input: 10 1 1970
    Output: 10

    Input: 10 1 1971
    Output 375
'''
# Không xài hàm có sẵn.
def absolute_day(day, month, year) -> Union[str, int]:
    try:
        epoch_time_date = arrow.get(1970, 1, 1)
        date = arrow.get(year, month, day)
        difference = date - epoch_time_date
        return difference.days
    except ValueError as exception:
        return str(exception)

'''
P02 - TRỪ ĐI N NGÀY
Mô tả
    Viết chương trình trừ n ngày vào một ngày tháng năm.
Dữ liệu đầu vào
    Một dòng duy nhất, bốn số nguyên dương day, month, year, n, cách nhau một khoảng trắng.
    Trong đó 
        1 <= day <= 28,29,30,31 tuỳ month
        1 <= month <= 12 
        1 <= year <= 10^9
        1 <= n <= 10^9
Dữ liệu đầu ra
    Ngày tháng năm kết quả, cách nhau 1 khoảng trắng
'''
# Không xài hàm có sẵn.
def minus_days(day, month, year, minus_day) -> str:
    try:
        date = arrow.get(year, month, day)
        tomorrow = date.shift(days=-minus_day)
        return tomorrow.format('DD MM YYYY')
    except ValueError as error:
        return str(error)

'''
Mô tả
    Viết chương trình nhập vào 2 ngày. Tính khoảng cách giữa 2 ngày đó.
Dữ liệu đầu vào
    Một dòng duy nhất, sáu số nguyên dương: day1, month1, year1; day2, month2, year2. 
    Trong đó:
        1<=d1,d2<=28,29,30,31 tuỳ m1,m2
        1 <= m1, m2 <= 12
        1 <= y1 <= y2 <= 10^9
Dữ liệu đầu ra
    Khoảng cách giữa 2 ngày
Ví dụ
    Input 
        day1=20 month1=11 year1=2019 
        day2=25 month2=11 year2=2019   
    Output: 5      
'''
# Không xài hàm có sẵn.
def day_difference(day1: int, month1: int, year1: int,
                   day2: int, month2: int, year2: int):
    try:
        first_day = arrow.get(year1, month1, day1)
        second_day = arrow.get(year2, month2, day2)
        difference = first_day - second_day
        return difference.days
    except ValueError as error:
        return str(error)

if __name__ == '__main__':
    print('IV. CS161 Week 04:')

    print('1. Absolute day:', absolute_day(1, 10, 2000))

    print('\n2. Minus days:', minus_days(1, 1, 2025, 5))

    # Sao xuống dòng nhìn gớm vậy
    print('\n3. Day difference:', day_difference(1, 12, 2020,
                                                 15, 8, 2020))
