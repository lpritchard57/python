class Employee:
    def __init__(self, name, emp_number):
        self.__name = name
        self.__emp_number = emp_number

    def get_name(self):
        return self.__name
    
    def get_emp_number(self):
        return self.__emp_number
    
    def set_name(self, name):
        self.__name = name

    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

class ProductionWorker(Employee):
    def __init__(self, name, emp_number, shift_number, hourly_rate):
        super().__init__(name, emp_number)
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.__shift_number
    
    def get_hourly_rate(self):
        return self.__hourly_rate
    
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

def main():
    print("Enter the following details of the employee: ")
    print(" ")
    name = input("Enter employee name: ")
    emp_number = input("Enter employee number: ")
    shift_number = int(input("Enter shift number(1 for day, 2 for night): "))
    hourly_rate = float(input("Enter hourly rate:"))
    print(" ")

    worker = ProductionWorker(name, emp_number, shift_number, hourly_rate)

    print("Details of the Employee: ")
    print(" ")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_emp_number())
    if worker.get_shift_number() == 1:
        print("Shift: Day")
    elif worker.get_shift_number() == 2:
        print("Shift: Night")
    else:
        print("Invalid entry")
    print("Pay Rate: ", worker.get_hourly_rate())

main()
