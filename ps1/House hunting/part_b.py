def main():
    portion_down_payment = .25
    annual_return = .04
    annual_salary = float(input("Enter your annual salary: "))
    potion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
    monthly_salary = annual_salary // 12
    current_saving = 0
    count_months = 0
    while current_saving < total_cost * portion_down_payment:
        current_saving += (current_saving * annual_return / 12) + (monthly_salary * potion_saved)
        count_months += 1
        if count_months % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
            monthly_salary = annual_salary // 12
    print("Number of months: ", count_months)