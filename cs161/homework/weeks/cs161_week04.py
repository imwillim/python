from cs161.homework.weeks.cs161_week03 import is_leap_year, get_days_in_month, validate_day

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
# Không ai tính tiền `blank line`.
# -> Fixed

def get_absolute_day(day: int, month: int, year: int) -> int:
    try:
        validate_day(day, month, year)

        return calculate_absolute_day(day, month, year)
    except ValueError as error:
        print(error)

        return -1


# Không ai tính tiền `blank line`.
def calculate_absolute_day(day: int, month: int, year: int):
    absolute_day = 0

    # Hạn chế xài +=
    # -> Fixed
    for specific_year in range(1970, year):
        absolute_day = absolute_day + get_days_in_year(specific_year)

    for specific_month in range(1, month):
        absolute_day = absolute_day + get_days_in_month(specific_month, year)

    absolute_day = absolute_day + day

    return absolute_day


def get_days_in_year(year):
    if is_leap_year(year):
        return 366

    return 365


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
# Không ai tính tiền `blank line`.
def minus_days(day: int, month: int, year: int, minus_day: int) -> str:
    try:
        validate_day(day, month, year)

        return process_minus_days(day, month, year, minus_day)
    except ValueError as error:
        return str(error)


# Code lại, lồng quá nhiều cấp
# -> Fixed
def process_minus_days(day: int, month: int, year: int, minus_day: int):
    while minus_day >= day:
        minus_day = minus_day - day
        month = month - 1

        if month == 0:
            month = 12
            year = year - 1

        day = get_days_in_month(month, year)

        if month == 2 and is_leap_year(year):
            day = 29

    day = day - minus_day

    return f'{day} {month} {year}'


'''
Mô tả
    Viết chương trình nhập vào 2 ngày. Tính khoảng cách giữa 2 ngày đó.
Dữ liệu đầu vào
    Một dòng duy nhất, sáu số nguyên dương: day1, month1, year1; day2, month2, year2. 
    Trong đó:
        1 <= d1, d2 <= 28,29,30,31 tuỳ m1,m2
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
# -> Fixed
def day_difference(day_1: int, month_1: int, year_1: int,
                   day_2: int, month_2: int, year_2: int) -> int:
    try:
        validate_day(day_1, month_1, year_1)
        validate_day(day_2, month_2, year_2)

        absolute_day_1 = get_absolute_day(day_1, month_1, year_1)
        absolute_day_2 = get_absolute_day(day_2, month_2, year_2)

        return absolute_day_1 - absolute_day_2
    except ValueError as error:
        print(error)

        return -1


if __name__ == '__main__':
    print('IV. CS161 Week 04:')

    print('1. Absolute day:', get_absolute_day(1, 10, 2020))

    print('\n2. Minus days:', minus_days(1, 1, 2025, 1000))

    # Sao xuống dòng nhìn gớm vậy -> DONE
    print('\n3. Day difference:', day_difference(1, 12, 2020, 15, 8, 2020))
