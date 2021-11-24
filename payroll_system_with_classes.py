""" Payroll system using classes"""

import emp_types

def print_payroll(lst):
    for employee in lst:
        print(f"Employee:  {employee.first_name} {employee.last_name}")
        print(f"SS Number: {employee.soc_sec_num}")
        print(f"Earnings:  ${employee.get_earnings():.2f}\n")

e1 = emp_types.SalariedEmployee("John", "Smith", "111-11-1111", weekly_pay=800)
e2 = emp_types.HourlyEmployee("Bill", "Jones", "222-22-2222", num_hours=39, hourly_rate=15)
employee_list = (e1, e2)
print_payroll(employee_list)
for emp in employee_list:
    if emp.first_name == "Bill":
        emp.hourly_rate *= 1.095  # Let's give Bill a 9.5% raise
        print(f"Bill got a 9.5% raise to {emp.hourly_rate:.2f} per hour")
        print_payroll([emp])
