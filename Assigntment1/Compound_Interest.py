"This is a program to calculate Compound Interest"

principal       = int(input("Enter the principal amount: "))
rate            = int(input("Enter the rate: "))
no_of_times     = int(input("Enter the no of times: "))
time            = int(input("Enter the time period: "))

"We are calculating Compound Interest using the formula CI = principal*(1+Rate/(100*n))^(n*time)-principal"

compound_interest= principal*(1+rate/(100*no_of_times))**(no_of_times*time)-principal
print(compound_interest)