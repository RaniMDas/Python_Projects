"This is a program to calculate Simple Interest"
principal       = int(input("Enter the principal amount :"))
rate            = int(input("Enter the rate :"))
time            = int(input("Enter the time period :"))

"We are calculating Simple Interest using its formula (Principal*rate*time)/100"
simple_interest = (principal*rate*time)/100

"We are printing Simple Interest for the time period"
print("The Simple Interest for 5 years is :", simple_interest) 