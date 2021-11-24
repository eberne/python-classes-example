""" Payroll example, no classes"""

e1 = ["John", "Smith", "111-11-1111", "salaried", 800]
e2 = ["Bill", "Jones", "222-22-2222", "hourly", 15, 39]

employee_list = (e1, e2)

def get_earnings(employee):
    if employee[3] == "salaried": return employee[4]
    if employee[3] == "hourly": return employee[4] * employee[5]
    return 0

def print_payroll(lst):
    for employee in lst:
        earnings = 0  # to catch invalid employee type
        if employee[3] == "salaried": earnings = employee[4]
        if employee[3] == "hourly": earnings = employee[4] * employee[5]
        print(f"Employee:  {employee[0]} {employee[1]}")
        print(f"SS Number: {employee[2]}")
        print(f"Earnings:  ${earnings:.2f}\n")

print_payroll(employee_list)
e2[4] *= 1.095  # Let's give Bill a 9.5% raise
print(f"Bill got a 9.5% raise to {e2[4]:.2f} per hour")
print_payroll([e2])
