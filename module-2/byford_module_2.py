def calculate_pay(hours_worked, hourly_rate):
    if hours_worked > 40:
        regular_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours_worked * hourly_rate

    return total_pay


def main():
    employee_name = "John Smith"
    hours_worked = 45
    hourly_rate = 21.75

    total_pay = calculate_pay(hours_worked, hourly_rate)

    print("Employee:", employee_name)
    print("Hours Worked:", hours_worked)
    print("Hourly Rate: $", hourly_rate)
    print("Total Pay: $", round(total_pay, 2))


main()