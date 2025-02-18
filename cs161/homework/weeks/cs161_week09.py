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
def largest_sum_subset_k(array: list[int], n: int, k: int) -> int:
    # Đề bài cho nguyên dương, gán bằng 0 là được rồi. 
    # Xài lệnh đao to búa lớn quá, người sau đọc phải đọc python document và đoán ý
    # -> FIXED
    largest = 0

    # Viết 2 vòng for kiểu lồng nhau mà đi pv là cook.
    # Đưa vòng for thứ 2 vào 1 hàm riêng, rồi gọi hàm đó ở trong vòng for thứ nhất.
    # Sau 3 tháng, có hiểu n - k + 1 là gì không? Tại sao không đặt thành biến cho dễ nhớ.
    # -> FIXED
    array_size = n
    adjacent_element_count = k
    sub_array_size = array_size - adjacent_element_count + 1

    for start in range(sub_array_size):
        end = start + adjacent_element_count
        largest = get_largest_with_sum_sub_array(largest, array, start, end)

    return largest


def get_largest_with_sum_sub_array(largest: int, array: list[int], start: int, end: int) -> int:
    sum_sub_array = 0

    for index in range(start, end):
        sum_sub_array = sum_sub_array + array[index]
        largest = max(largest, sum_sub_array)

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
# -> Fixed
def elements_intersection(array_1: list[int], array_2: list[int]) -> list[int]:
    # Nên xài list comprehension -> Fixed.
    result = [num for num in array_1 if num in array_2]

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
# -> Fixed
def reverse_array(array: list[int]) -> list[int]:
    return array[::-1]


if __name__ == '__main__':
    print('IX. CS161 Week 09:')

    test_array_1 = [1, 2, 6, 2, 3]
    print(f'1. Sum of biggest subset of k element of {test_array_1} is', largest_sum_subset_k(test_array_1, 5, 3))

    test_array_2 = [3, 5, 12, 67, 67, 45, 678]
    test_array_3 = [5, 23, 12, 45, 12, 67]
    print(f'\n2. Elements intersection between {test_array_2} and {test_array_3} is',
          elements_intersection(test_array_2, test_array_3))

    test_array_4 = [1, 2, 3, 4, 5]
    print(f'\n3. Reverse array of {test_array_4}:', reverse_array(test_array_4))
