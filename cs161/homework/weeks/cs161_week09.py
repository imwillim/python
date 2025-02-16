import sys
from typing import Optional

'''
P01 - TỔNG LỚN NHẤT TRONG DÃY CON CỦA MẢNG
Mô tả
    Nhập mảng một chiều có n phần tử là những số nguyên dương.
    In ra tổng lớn nhất của k phần tử liên tiếp xuất hiện trên mảng.
Dữ liệu đầu vào
    Dòng 1: Nhập số nguyên n > 0 - độ lớn của mảng
            Nhập số nguyên 0 < k < n

    Dòng 2: Nhập n số nguyên dương vào mảng.
Dữ liệu đầu ra
    In tổng
Ví dụ
    Input: array=[3, 1, 2, 3, 4, 5], n=6, k=3
    Output: 12
'''
# Không ai tính tiền `blank line`.
def largest_sum_subset_k(array: list[int], n: int, k: int) -> Optional[int]:
    # Đề bài cho nguyên dương, gán bằng 0 là được rồi. 
    # Xài lệnh đao to búa lớn quá, người sau đọc phải đọc python document và đoán ý.
    largest = -sys.maxsize
    
    # Viết 2 vòng for kiểu lồng nhau mà đi pv là cook. 
    # Đưa vòng for thứ 2 vào 1 hàm riêng, rồi gọi hàm đó ở trong vòng for thứ nhất.
    # Sau 3 tháng, có hiểu n - k + 1 là gì không? Tại sao không đặt thành biến cho dễ nhớ.
    for start in range(n - k + 1):
        sum_subset = 0
        end = start + k
        for index in range(start, end):
            sum_subset += array[index]
            largest = max(largest, sum_subset)
    
    return largest

'''
P02 - CÁC PHẦN TỬ CÙNG XUẤT HIỆN TRÊN 2 MẢNG
Mô tả
    Cho hai mảng a và b có lần lượt m và n phần tử. Các phần tử trong mỗi mảng khác nhau từng đôi một. Tìm những giá trị cùng xuất hiện trên hai mảng. Mở rộng: Giả sử có phần tử trùng.
Dữ liệu đầu vào
    Dòng 1: Nhập số nguyên 0<n,m <=10^9 ; nhập số phần tử mảng,
    Dòng 2: Nhập mỗi mảng a,b trên từng dòng
    Điều kiện: Các phần tử trong mỗi mảng khác nhau từng đôi một.
Dữ liệu đầu ra
    Tìm và in những giá trị cùng xuất hiện trên hai mảng. Mở rộng: Giả sử có phần tử trùng.
Ví dụ
    Input: array1=[3, 1, 2, 3, 4, 5], array2=[1, 2, 3, 4, 5, 6]
    Output: [3, 4, 5]
'''
# Không ai tính tiền `blank line`.
# nên đặt a_1 hoặc arr_1
def elements_intersection(arr1: list[int], arr2: list[int]):
    # Nên xài list comprehension.
    result = [num if num in arr2 for num in arr1]

    # for num in arr1:
    #     if num in arr2:
    #         result.append(num)

    return result

'''
P03 - ĐẢO NGƯỢC MẢNG
Mô tả
    Nhập mảng một chiều có n phần tử là những số nguyên dương. Đảo ngược mảng
Dữ liệu đầu vào
    Dòng 1: Nhập số nguyên 0<n<=10^9, độ lớn của mảng
    Dòng 2: Nhập n số nguyên dương vào mảng.
Dữ liệu đầu ra
    In mảng đảo ngược.
Ví dụ:
    Input: array=[1, 2, 3, 4, 5]
    Output: [1, 2, 3, 4, 5]    
'''
# Tự code nào.
# Không ai tính tiền `blank line`.
def reverse_array(array: list[int]):
    reversed_iterator = reversed(array)
    return list(reversed_iterator)

if __name__ == '__main__':
    print('IX. CS161 Week 09:')
    print('1. Sum of biggest subset of k element is', largest_sum_subset_k([1, 2, 6, 2, 3], 5, 3))

    print('\n2. Elements intersection:', elements_intersection([3, 5, 12, 67, 67, 45, 678], [5, 23, 12, 45, 12, 67]))

    print('\n3. Reverse array:', reverse_array([1, 2, 3, 4, 5]))
