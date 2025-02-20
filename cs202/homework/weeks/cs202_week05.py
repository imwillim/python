'''
Assignment 01 - Company
Công ty ABC cần xây dựng ứng dụng quản lý thông tin và tính lương cho nhân viên. Thông tin mỗi nhân viên bao gồm: mã nhân viên, họ tên, ngày sinh, địa chỉ.
Công ty có 2 loại nhân viên với cách tính lương như sau:
- Lương(Nhân viên sản xuất): số sản phẩm * 20.000 vnđ
- Lương(Nhân viên công nhật): số ngày * 300.000 vnđ

Áp dụng tính kế thừa + tất cả các thuộc tính phải là private, khai báo class NVSanXuat và NVCongNhat kế thừa class NhanVien và cài đặt các hàm sau:
1. Nhập thông tin nhân viên
2. Xuất thông tin nhân viên ra màn hình
3. Tính lương nhân viên
4. Cài đặt 5 constructor cho mỗi class
5. Vẽ sơ đồ lớp thể hiện quan hệ giữa 3 class nhân viên

Hãy cài đặt các hàm sau của class CongTy:
6. Nhập danh sách các nhân viên
7. Tính tổng tiền lương của tất cả nhân viên
8. Có bao nhiêu NVSX trong công ty
9. Nhập vào chuỗi, tìm nhân viên có tên tương ứng
10. Có bao nhiêu nhân viên sinh trong tháng 5
'''


class Employee:
    def __init__(self, employee_id, name, date_of_birth, address):
        self.employee_id = employee_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address

    def display_info(self):
        return f'ID: {self.employee_id}, Name: {self.name}, Date of birth: {self.date_of_birth}, Address: {self.address}'

    def calculate_salary(self):
        pass

    def get_name(self):
        return self.name

    def get_birth_month(self):
        return int(self.date_of_birth.split('/')[1])


class ProductionWorker(Employee):
    def __init__(self, employee_id, name, date_of_birth, address, product_count):
        super().__init__(employee_id, name, date_of_birth, address)

        self.product_count = product_count

    def calculate_salary(self):
        return self.product_count * 20000


class DailyWorker(Employee):
    def __init__(self, employee_id , name, date_of_birth, address, work_days):
        super().__init__(employee_id, name, date_of_birth, address)

        self.work_days = work_days

    def calculate_salary(self):
        return self.work_days * 300000


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_total_salary(self):
        total_salary = 0

        for employee in self.employees:
            total_salary = total_salary + employee.calculate_salary()

        return total_salary

    def count_production_workers(self):
        count = 0

        for employee in self.employees:
            if isinstance(employee, ProductionWorker):
                count = count + 1

        return count

    def find_employee_by_name(self, name):
        for employee in self.employees:
            if name in employee.get_name():
                info = employee.display_info()

                return f'{info}'

        return None

    def count_employees_born_in_may(self):
        count = 0

        for employee in self.employees:
            if employee.get_birth_month() == 5:
                count = count + 1

        return count


if __name__ == '__main__':
    john = ProductionWorker('001', 'John Doe', '15/05/1990', 'New York', 100)
    jane = DailyWorker('002', 'Jane Smith', '20/06/1992', 'Los Angeles', 25)
    mike = ProductionWorker('003', 'Mike Johnson', '10/05/1985', 'Chicago', 150)

    company = Company()

    company.add_employee(john)
    company.add_employee(jane)
    company.add_employee(mike)

    print('Total company salary:', company.get_total_salary())
    print('Number of production workers:', company.count_production_workers())
    print('Find employee by name "John" - ', company.find_employee_by_name('John'))
    print('Number of employees born in May:', company.count_employees_born_in_may())
