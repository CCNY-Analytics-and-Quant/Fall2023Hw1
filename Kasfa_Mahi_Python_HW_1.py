bal = 10000
deposit = 22500

ret_age = 50
cur_age = 21

# Run loop for each year
for year in range(ret_age - cur_age):
  bal = bal + deposit

# Output the results
print(bal)

acct_bal = 0
deposit = 22500
cur_age = 22
ret_age = 67
salary = 60000
matching = 0

for year in range(cur_age, ret_age):
    acct_bal = acct_bal + deposit

print(acct_bal)

# %%timeit
acct_bal = 0
deposit = 22500
cur_age = 22
ret_age = 67
salary = 60000
matching = salary * 0.05

for year in range(cur_age, ret_age):
    acct_bal = acct_bal + deposit + matching
print(acct_bal)

acct_bal = int(input('What is your current account balance? '))
deposit = int(input('How much will you contribute every year? '))
cur_age = 22
ret_age = 67

salary = 60000
rf_rate = 0.025
match_rate = 0.05
matching = 0

for year in range(cur_age, ret_age):
    salary *= 1 + rf_rate
    matching = salary * match_rate
    acct_bal += deposit + matching

print(acct_bal)

salary = 60000
acct_bal = 0

while salary < 100000:
    salary *= 1 + rf_rate
    matching = salary * match_rate
    acct_bal += deposit + matching
    
print(salary)

cur_age = int(input("Enter your current age: "))
ret_age = int(input("Enter your desired retirement age: "))
initial_bal = float(input("Enter your initial account balance: "))
annual_deposit = float(input("Enter your annual contribution: "))
salary = float(input("Enter your current salary: "))
rf_rate = 0.025  # Annual risk-free rate (assumed)
match_rate = float(input("Enter your employer's matching rate as a decimal (e.g., 0.05 for 5%): "))
desired_retirement_balance = float(input("Enter your desired retirement balance: "))

acct_bal = initial_bal
matching = 0

while cur_age < ret_age and acct_bal < desired_retirement_balance:
    # Update salary, matching, and account balance
    salary *= 1 + rf_rate
    matching = salary * match_rate
    annual_investment_return = acct_bal * 0.14  # 14% annual return
    acct_bal += annual_deposit + matching + annual_investment_return
    
    # Increment age
    cur_age += 1
    
if acct_bal >= desired_retirement_balance:
    retirement_age = cur_age
else:
    retirement_age = None


print(f"Retirement age: {retirement_age}")
print(f"Retirement balance achieved: ${acct_bal:,.2f}")


def calculate_retirement_with_for_loop(initial_bal, deposit, ret_age, cur_age):
    bal = initial_bal
    for year in range(ret_age - cur_age):
        bal += deposit
    return bal

def calculate_retirement_with_while_loop(initial_bal, deposit, ret_age, cur_age):
    bal = initial_bal
    while cur_age < ret_age:
        bal += deposit
        cur_age += 1
    return bal

# Calculate retirement with for loop
bal_for = calculate_retirement_with_for_loop(initial_bal, annual_deposit, ret_age, cur_age)
print(f"Retirement balance achieved (For Loop): ${bal_for:,.2f}")

# Calculate retirement with while loop
bal_while = calculate_retirement_with_while_loop(initial_bal, annual_deposit, ret_age, cur_age)
print(f"Retirement balance achieved (While Loop): ${bal_while:,.2f}")


# Credit to John Droescher 
# Receieved further clarification from Raqeeb Ahmed 