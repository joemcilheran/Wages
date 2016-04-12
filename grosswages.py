while True:
    hoursWorked = input("How many hours did you work? \n")
    try:
        hoursWorked = float(hoursWorked)
    except ValueError:
        print("Please enter a number(i.e. 24, not twenty-four)")
        continue
    break
while True:
    payPerHour = input("How much do you get paid per hour? \n")    
    try:
        payPerHour = float(payPerHour)
    except ValueError:
        print("Please enter a number(i.e. 24, not twenty-four)")
        continue
    break
if hoursWorked <= 40:
    grossWages = hoursWorked * payPerHour
else: 
    grossWages = (payPerHour * 40) + ((hoursWorked - 40) * (payPerHour * 1.5))
print("Your gross wages are: ",grossWages)