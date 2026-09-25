def calculate_commission(total_sales: float, commission_rate: float = 0.05) -> float:
    return total_sales * commission_rate

check_target = lambda total_sales, sales_target=50000.0: total_sales >= sales_target

def calculate_total_income(base_salary: float, commission: float, bonus: float) -> float:
    return base_salary + commission + bonus

def calculate_projected_income(monthly_income: float, months: int) -> float:
    if months <= 0:
        return 0.0
    return monthly_income + calculate_projected_income(monthly_income, months - 1)

def display_report(
    name: str, 
    total_sales: float, 
    commission: float, 
    bonus: float, 
    total_income: float, 
    target_reached: bool
) -> None:
    print("\nSales commission report")
    print(f"Employee: {name}")
    print(f"Total sales: {total_sales:.2f} THB")
    print(f"Commission: {commission:.2f} THB")
    print(f"Bonus: {bonus:.2f} THB")
    print(f"Total income: {total_income:.2f} THB")
    print(f"Sales target reached: {'Yes' if target_reached else 'No'}")


if __name__ == "__main__":
    name = input("Employee name: ")
    base_salary = float(input("Base monthly salary: "))
    total_sales = float(input("Total monthly sales: "))

    commission = calculate_commission(total_sales)
    target_reached = check_target(total_sales)
    bonus = 2000.0 if target_reached else 0.0
    total_income = calculate_total_income(base_salary, commission, bonus)

    display_report(name, total_sales, commission, bonus, total_income, target_reached)