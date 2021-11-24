"""Example of classes using OOP with inheritance"""

class Employee:

    def __init__(self, first_name, last_name, soc_sec_num):
        self.first_name = first_name
        self.last_name = last_name
        self.soc_sec_num = soc_sec_num

class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, soc_sec_num, weekly_pay):
        super().__init__(first_name, last_name, soc_sec_num)
        self.weekly_pay = weekly_pay
        self.emp_type = "Salaried"

    def get_earnings(self):
        return self.weekly_pay

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, soc_sec_num, hourly_rate, num_hours):
        super().__init__(first_name, last_name, soc_sec_num)
        self.hourly_rate = hourly_rate
        self.num_hours = num_hours
        self.emp_type = "Hourly"

    def get_earnings(self):
        return self.num_hours * self.hourly_rate

def print_payroll(lst):
    for employee in lst:
        print(f"Employee:  {employee.first_name} {employee.last_name}")
        print(f"SS Number: {employee.soc_sec_num}")
        print(f"Earnings:  ${employee.get_earnings():.2f}\n")

e1 = SalariedEmployee("John", "Smith", "111-11-1111", 800)
e2 = HourlyEmployee("Bill", "Jones", "222-22-2222", 15, 40)
employee_list = (e1, e2)
print_payroll(employee_list)
e2.hourly_rate *= 1.1  # give Bill a raise
print(f"Bill got a 10% raise to {e2.hourly_rate:.2f} per hour")
bill = (e2,)
print_payroll(bill)
