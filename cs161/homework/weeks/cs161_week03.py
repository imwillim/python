import arrow
import calendar

'''
P01 - ĐẬU HAY RỚT
Mô tả
    Viết hàm cho phép giảng viên lí thuyết nhập điểm bài tập, điểm thực hành, điểm lí thuyết,
    và cho biết sinh viên có gian lận trong môn học hay ko. Cho biết sinh viên đó đậu hay rớt môn
    học này.
    
    Biết rằng, tỉ lệ điểm là 30% điểm bài tập, 30% điểm thực hành và 40% điểm lí thuyết. Sinh viên
    gian lận sẽ được tính 0đ tổng cộng. Sinh viên điểm từ 5 trở lên là đậu.
Dữ liệu đầu vào
    Gồm có 4 tham số.
        Tham số 1, số thực, điểm bài tập, assignment.
        Tham số 2, số thực, điểm thực hành, lab.
        Tham số 3, số thực, điểm lí thuyết, final.
        Tham số 4, số nguyên, cho biết sinh viên đó có gian lận hay ko, cheating.
        0 <= assignment, lab, final <= 10.
    0 <= cheating <= 1.
Dữ liệu đầu ra
    Một dòng duy nhất, gồm có 2 thông tin, điểm tổng cộng (làm tròn 1 chữ số thập phân), total và
    kết quả PASSED (đậu) / FAILED (rớt).
Ví dụ
    Input: assignment=9.5, lab=8.5, final=8.0, cheating=0
    Output: 8.6 PASSED
'''

# Sao lúc khai báo có kiểu dữ liệu, lúc không vậy? Thống nhất 1 style thôi.
# cheating -> is_cheating như vầy mới đúng ngữ nghĩa
# trong python nên để is_cheating là True/False
# Rồi làm tròn 1 chữ số đâu.
def passed(assignment, lab, final, cheating) -> str:
    assignment_rate = assignment * 0.3
    lab_rate = lab * 0.3
    final_rate = final * 0.4

    grade = assignment_rate + lab_rate + final_rate
    rounded_grade = round(grade, 1)

    if cheating == 1:
        return f'{rounded_grade} FAILED'

    if grade < 5:
        return f'{rounded_grade} FAILED'

    # Không nên xài else.
    
    return f'{rounded_grade} PASSED'


'''
P02 - NĂM NHUẬN
Mô tả
    Viết hàm nhận giá trị là một năm. Cho biết năm đó có phải năm nhuận hay không.
Dữ liệu đầu vào
    Một số nguyên dương, year.
    Trong đó, 0 < year <= 10^9.
Dữ liệu đầu ra
    Cho biết năm đó có phải năm nhuận hay không.
Ví dụ
    Input: 2000
    Output: Nam nhuan
    
    Input: 2019
    Output: Khong phai nam nhuan
'''
# Hàm này nên là is_leap_year và trả về boolean
def leap_year(year):
    if year % 400 == 0:
        return 'Nam nhuan'

    if year % 100 == 0 and year % 4 != 0:
        return 'Nam nhuan'
    
    # Không nên xài else.

    return 'Khong phai nam nhuan'

'''
P03 - SỐ NGÀY TRONG THÁNG
Mô tả
    Viết hàm nhận hai giá trị là một tháng và một năm. Cho biết tháng đó có bao nhiêu ngày.
Dữ liệu đầu vào
    Tham số đâu tiên: month, số nguyên dương
    Tham số thứ hai: year, số nguyên dương
    Trong đó, 0 < year <= 10^9 và 1 <= month <= 12.
Dữ liệu đầu ra
    Số ngày trong tháng đó.
Ví dụ
    Input: 1 2019
    Output: 31
    
    Input: 2 2019
    Output: 28
    
    Input: 2 2020
    Output: 29   
'''
# Trời mẹ, code bình thường, xài if, không được xài hàm có sẵn
def days_in_month(month, year):
    days = calendar.monthrange(year, month)[1]
    return days

'''
P04 - NGÀY MAI
Mô tả
    Viết hàm nhận vào 3 giá trị ngày tháng năm. Cho biết ngày mai là ngày mấy.
Dữ liệu đầu vào
    Tham số đâu tiên: day, số nguyên dương
    Tham số thứ hai: month, số nguyên dương
    Tham số thứ ba: year, số nguyên dương
    Trong đó, 0 < year <= 10^9, 1 <= month <= 12, 1 <= day <= 31.
Dữ liệu đầu ra
    Ngày mai, tomorrow.
Ví dụ
    Input: 1 10 2019
    Output: 2 10 2019
    
    Input: 31 10 2019
    Output: 1 11 2019
    
    Input: 31 12 2019
    Output: 1 1 2020
'''
# Trời mẹ, code bình thường, xài if, không được xài hàm có sẵn
# Không ai tính tiền `blank line`.
def tomorrow(day, month, year):
    try:
        date = arrow.get(day, month, year)
        next_day = date.shift(days=1)
        return next_day.format('DD MM YYYY')
    except ValueError as error:
        return str(error)

'''
P26 - TIỀN THUÊ PHÒNG
Mô tả
    Tính tiền thuê phòng khi biết số ngày thuê và loại phòng (một trong 3 loại A, B hoặc C) với qui
    định như sau:
        Loại A : 450,000 đ/ngày
        Loại B : 350,000 đ/ngày
        Loại C : 25,000đ/ngày

    Nếu thuê quá 12 ngày thì phần trăm được giảm trên tổng số tiền (tính theo giá qui định)
    là: 10% cho phòng loại A, 8% cho phòng loại B hay C.
Dữ liệu đầu vào
    0 < SoNgay <= 10^9, LoaiPhong=[A, B, C];
Dữ liệu đầu ra
    Giá tiền
Ví dụ
    Input: 5 A
    Output: 2250000
    
    Input: 10 B
    Output: 3500000
    
    Input: 7 C
    Output: 175000
'''
# Không ai tính tiền `blank line`.
def rent(day, room_type):
    rental_type = {
        'A': {'price': 450000, 'tax': 0.1},
        'B': {'price': 350000, 'tax': 0.08},
        'C': {'price': 25000, 'tax': 0.08},
    }

    specific_rental_type = rental_type[room_type]
    rent_before_tax = specific_rental_type['price'] * day
    
    # Áp dụng kĩ thuật fast return, đảo ngược điêu kiện để code ngắn hơn

    if day < 12:
        return rent_before_tax
    
    tax = rent_before_tax * specific_rental_type['tax']

    return rent_before_tax - tax


if __name__ == '__main__':
    print('II. CS161 Week 02:')
    print('\n1. Passed or Failed:')
    print(passed(8, 9, 10, 0))

    print('\n2. Leap Year:')
    print(leap_year(2000))

    print('\n3. Days in Month:')
    print(days_in_month(12, 2020))

    print('\n4. Tomorrow:')
    print(tomorrow(2, 1, 1999))

    print('\n5. Rental:')
    print(rent(12, 'C'))
