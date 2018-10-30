annual_salary = float(input("What is your annual salaray"))
portion_saved = float(input("Enter the percent to be saved as a decimal"))
total_cost = float(input("What is the cost of your dream home"))
annual_saved = annual_salary*portion_saved
monthly_saved = annual_saved/12
portion_down_payment = .25 * total_cost
current_savings = monthly_saved 
r = .04
months = 1
# print(annual_salary,portion_saved,total_cost)

while current_savings < portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += monthly_saved
    months += 1
print("It will take {} months to save".format(months))