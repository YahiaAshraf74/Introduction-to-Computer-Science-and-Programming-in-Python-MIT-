def main():
    semi_annual_raise = .07
    annual_return = .04
    portion_down_payment = .25
    total_cost = 1_000_000
    number_of_months = 36
    annual_salary = float(input("Enter your annual salary: "))

    def can(percentage, annual_salary):
        monthly_salary = annual_salary / 12
        saving_money = 0
        for i in range(0, number_of_months):
            saving_money += (saving_money * annual_return / 12) + (monthly_salary * percentage)
            if i % 6 == 0 and i != 0:
                annual_salary += annual_salary * semi_annual_raise
                monthly_salary = annual_salary // 12
        return saving_money

    def bisection_search(annual_salary):
        start = 0
        end = 10000
        number_of_steps = 0
        best_saving = 0.0
        while start < end:
            number_of_steps += 1
            mid = (start + end) / 2
            saving_mid = can(mid / 10000, annual_salary)
            if abs(saving_mid - total_cost * portion_down_payment) < 100:
                return mid / 10000, number_of_steps
            elif saving_mid > total_cost * portion_down_payment:
                end = mid - 1
            else:
                start = mid

    ans = bisection_search(annual_salary)
    if ans == None:
        print("It is not possible to pay the sown payment in three years.")
    else:
        print("Best savings rage: ", ans[0])
        print("Steps in bisection search: ", ans[1])
    # current_saving = 0
    # count_months = 0
    # while current_saving < total_cost * portion_down_payment:
    #     current_saving += (current_saving * annual_return / 12) + (monthly_salary)
    #     count_months += 1
    #     if count_months % 6 == 0:
    #         annual_salary += annual_salary * semi_annual_raise
    #         monthly_salary = annual_salary // 12
    # print("Number of months: ", count_months)
