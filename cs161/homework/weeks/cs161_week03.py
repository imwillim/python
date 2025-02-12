import arrow
import calendar

from common.utils import validate_date

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
def passed(**kwargs) -> str:
    def validate(args):
        for key in ['assignment', 'lab', 'final']:
            if not (0 <= args[key] <= 10):
                raise ValueError(f'{key} must be between 0 and 10')

        if not (0 <= args['cheating'] <= 1):
            raise ValueError('Cheating must be 0 or 1')

    try:
        validate(kwargs)
        grade = (kwargs['assignment'] * 0.3) + (kwargs['lab'] * 0.3) + (kwargs['final'] * 0.4)
        rounded_grade = round(grade, 1)

        if kwargs['cheating'] == 1:
            return f'{rounded_grade} FAILED'

        if grade < 5:
            return f'{rounded_grade} FAILED'
        else:
            return f'{rounded_grade} PASSED'
    except ValueError as e:
        return str(e)
    except KeyError as error:
        return f'Missing keyword argument: {str(error)}'

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
def leap_year(year):
    def validate(valid_year):
        if not (0 < valid_year <= 10 ** 9):
            raise ValueError('Year must be greater than 0 and less than 10^9')

    validate(year)
    if year % 400 == 0:
        return 'Nam nhuan'

    if year % 100 == 0 and year % 4 != 0:
        return 'Nam nhuan'
    else:
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
def days_in_month(**kwargs):
    def validate(args):
        if not (1 <= args['month'] <= 12):
            raise ValueError('Month must be between 1 and 12')

        if not (0 < args['year'] <= 10 ** 9):
            raise ValueError('Year must be greater than 0 and less than 10^9')

    try:
        validate(kwargs)
        days = calendar.monthrange(**kwargs)[1]
        return days
    except ValueError as error:
        return str(error)
    except KeyError as error:
        return f'Missing keyword argument: {str(error)}'

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
def tomorrow(**kwargs):
    try:
        validate_date(**kwargs)
        date = arrow.get(**kwargs)
        next_day = date.shift(days=1)
        return next_day.format('DD MM YYYY')
    except ValueError as error:
        return str(error)
    except KeyError as error:
        return f'Missing keyword argument: {str(error)}'


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
def rent(**kwargs):
    def validate(args):
        if not (0 < args['day'] <= 10 ** 9):
            raise ValueError('Day must be greater than 0 and less than 10^9')

        if args['type'] not in ('A', 'B', 'C'):
            raise ValueError('Type must be A, B or C')

    try:
        validate(kwargs)
        rental_type = {
            'A': {'price': 450000, 'tax': 0.1},
            'B': {'price': 350000, 'tax': 0.08},
            'C': {'price': 25000, 'tax': 0.08},
        }
        before_tax = rental_type[kwargs['type']]['price'] * kwargs['day']
        if kwargs['day'] > 12:
            tax = before_tax * rental_type[kwargs['type']]['tax']
            return before_tax - tax
        else:
            return before_tax
    except ValueError as error:
        return str(error)
    except KeyError as error:
        return f'Missing keyword argument: {str(error)}'

if __name__ == '__main__':
    print('II. CS161 Week 02:')
    print('\n1. Passed or Failed:')
    params = {
        'assignment': 8,
        'lab': 9,
        'final': 10,
        'cheating': 0
    }
    print(passed(**params))

    print('\n2. Leap Year:')
    print(leap_year(2000))

    print('\n3. Days in Month:')
    params = {
        'month': 12,
        'year': 2020,
    }
    print(days_in_month(**params))

    params['day'] = 18
    print('\n4. Tomorrow:')
    print(tomorrow(**params))

    params['type'] = 'C'
    print('\n5. Rental:')
    print(rent(**params))
