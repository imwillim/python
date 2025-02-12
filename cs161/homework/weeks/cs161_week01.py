from typing import Union, Any

'''
P01 - THƯƠNG 2 SỐ NGUYÊN
Mô tả
    Viết hàm nhập vào 2 số nguyên. Lấy số thứ 1 chia số thứ 2 và in kết quả ra màn hình.
Dữ liệu đầu vào
    Một dòng duy nhất, chứa 2 số nguyên a và b, cách nhau một khoảng trắng.
    Trong đó, -10^9 <= a, b <= 10^9.
Dữ liệu đầu ra
    Thương của 2 số nguyên, theo định dạng a - b = c. Lấy 2 chữ số phần thập phân.
'''
def divide(first_integer: int, second_integer: int) -> Union[str, float]:
    def validate(divisor: int) -> None:
        if divisor == 0:
            raise ValueError('Divisor cannot be 0')

    try:
        validate(second_integer)
        return first_integer / second_integer
    except ValueError as exception:
        return str(exception)

'''
P02 - SỐ KWH ĐIỆN TIÊU THỤ
Mô tả
    Viết hàm nhận hai giá trị là chỉ số điện tháng trước và chỉ số điện tháng hiện tại.
    Tính số KWh điện mà gia đình đã tiêu thụ và in kết quả ra màn hình.
Dữ liệu đầu vào
    Tham số đầu tiên, một số nguyên dương, previous, chỉ số điện tháng trước.
    Tham số thứ hai, một số nguyên dương, current, chỉ số điện tháng hiện tại.
    Trong đó, 0 <= previous <= current <= 10^9.
Dữ liệu đầu ra
    Chỉ số điện tiêu thụ.
Ví dụ
    Input: 10 15
    Output: 5    
'''
def electric_consumption(previous: int, current: int) -> Union[str, int]:
    def validate(start: int, end: int) -> None:
        if start > end:
            raise ValueError('Previous must not be greater than current')
        if start < 0:
            raise ValueError('Previous must be greater than 0')
        elif start > 10 ** 9:
            raise ValueError('Previous must be less than 10^9')

    try:
        validate(previous, current)
        return current - previous
    except ValueError as exception:
        return str(exception)

'''
P03 - TÍNH TUỔI
Mô tả
    Viết hàm nhận giá trị năm sinh của một người. Tính tuổi của người đó (tính đến năm
    2025) và in kết quả ra màn hình
Dữ liệu đầu vào
    Một số nguyên dương duy nhất.
    Trong đó, 0 <= year of birth <= 2025.
Dữ liệu đầu ra
    Tuổi của người đó.
'''
def calculate_age(age) -> Union[Union[str, int], Any]:
    def validate(year: int) -> None:
        if year > 2025:
            raise ValueError('Age must not be greater than 2025')

    try:
        validate(age)
        return 2025 - age
    except ValueError as exception:
        return str(exception)

'''
P04 - TÍNH TÍNH TIỀN MUA HÀNG
Mô tả
    Viết hàm nhận hai giá trị là số lượng và đơn giá một sản phẩm. Tính tiền phải trả = tiền hàng +
    tiền thuế. Tiền hàng = số lượng * đơn giá. Thuế = 10% của tiền hàng.
Dữ liệu đầu vào
    Tham số đầu tiên, một số nguyên dương, quantity, số lượng sản phẩm.
    Tham số thứ hai, một số thực dương, price, đơn giá một sản phẩm.
    Trong đó, -10^9 <= quantity, price <= 10^9.
Dữ liệu đầu ra
    Tổng tiền phải trả. Lấy 0 chữ số phần thập phân.
'''
def calculate_package(price, quantity) -> Union[Union[str, float], Any]:
    def validate(money: int, amount: int) -> None:
        if money < 0:
            raise ValueError('Price must not be less than 0')

        if amount < 0:
            raise ValueError('Amount must not be less than 0')

    try:
        validate(price, quantity)
        before_tax = price * quantity
        tax = before_tax * 0.1
        return before_tax - tax
    except ValueError as exception:
        return str(exception)

'''
P05 - ĐỔI TIỀN
Mô tả
    Viết chương trình nhập vào một số nguyên dương money, chẵn đến hàng nghìn. Xét các tờ tiền
    mệnh giá 500.000, 200.000, 100.000, 50.000, 20.000, 10.000, 5.000, 2.000 và 1.000. Với cách
    đổi tiền ưu tiên tờ mệnh giá cao trước tiên, hãy in ra các tờ tiền đổi được.
Dữ liệu đầu vào
    Một số nguyên dương n duy nhất, money, số tiền cần đổi. 0 < money <= 10^9
Dữ liệu đầu ra
    9 dòng, theo định dạng, mệnh giá: số tờ.
Ví dụ:
    Input: 2361000
    Output:
        500000: 4
        200000: 1
        100000: 1
        50000: 1
        20000: 0
        10000: 1
        5000: 0
        2000: 0
        1000: 1
'''
def convert_money_vnd(money: int) -> str:
    def validate(cash: int) -> None:
        if money % 500 != 0:
            raise ValueError('Money must be in VND')

        if cash < 0:
            raise ValueError('Money must not be less than 0')
        if cash > 10 ** 9:
            raise ValueError('Money must not be greater than 10^9')

    try:
        validate(money)
        ratio_chart = {
            500000: 0,
            200000: 0,
            100000: 0,
            50000: 0,
            20000: 0,
            10000: 0,
            5000: 0,
            2000: 0,
            1000: 0
        }
        for ratio in ratio_chart:
            if money >= ratio:
                ratio_chart[ratio] = money // ratio
                money %= ratio

        chart = str()
        for ratio, count in ratio_chart.items():
            chart += f'{ratio}: {count}\n'
        return chart
    except ValueError as exception:
        return str(exception)


if __name__ == '__main__':
    print('I. CS161 Week 01:')
    print('1. Divide exercise:')

    print('\n2. Electric consumption:')
    print(electric_consumption(10, 15))

    print('\n3. Age calculation:')
    print(calculate_age(2020))

    print('\n4. Package calculation:')
    print(calculate_package(1000, 10))

    print('\n5. Money conversion:')
    print(convert_money_vnd(10024000))
