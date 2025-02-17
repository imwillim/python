
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

# Chưa thấy lấy 2 chữ số phần thập phân, nhưng thôi tạm chấp nhận.
# Chú ý là phép / là chia lấy phần thập phân, // là chia lấy phần nguyên.
# Hàm vừa trả float vừa trả str. Handle thí mẹ.
# Trong trường hợp này cứ để raise exception ra ngoài, không cần handle.
def divide(first_integer: int, second_integer: int):
    try:
        return first_integer / second_integer
    except ZeroDivisionError as exception:
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

# Đúng
def electric_consumption(previous: int, current: int) -> int:
    return current - previous

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

# Đúng
def calculate_age(birth_year: int) -> int:
    return 2025 - birth_year


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
# Không ai tính tiền `blank line`.
# Output phải là số int như đề bài yêu cầu.
# -> Fixed
def calculate_package(price: int, quantity: int) -> int:
    cost_before_tax = price * quantity
    tax = cost_before_tax * 0.1

    return int(cost_before_tax - tax)

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
# Không ai tính tiền `blank line`.
def convert_money_vnd(money: int) -> str:
    exchange_table = {
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

    # Đúng. Nếu gặp trường hợp này trong tương lai thì có hàm `divmod``
    for value in exchange_table:
        if money >= value:
            exchange_table[value] = money // value
            money %= value

    table = '' # str() cũng được, nhưng không ai viết vậy.

    for value, count in exchange_table.items():
        table += f'{value}: {count}\n' # Tốt, biết xài string formater.

    return table


if __name__ == '__main__':
    print('I. CS161 Week 01:')
    print('1. Divide exercise:', divide(1, 0))

    print('\n2. Electric consumption:', electric_consumption(10, 15))

    print('\n3. Age calculation:', calculate_age(2020))

    print('\n4. Package calculation:', calculate_package(1000, 10))

    print('\n5. Money conversion:', convert_money_vnd(10024000))
