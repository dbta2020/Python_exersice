fix_tax_rate = 0.22
rent = 3000
salary = float(input("enter your salary: "))
income_net = salary*(1 - fix_tax_rate) 
# we will check if the net income is enough to afford rent
if income_net >= rent:
    print("You can rent this house")
else:
    print("you need to find a new job.")
if income_net - rent >= 1000:
    print("You can afford this house and have save more than 1000.")
else:
    print("You can save less than 1000.")
# #3.Using if statements    

