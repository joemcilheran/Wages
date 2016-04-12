def gethours():
    hoursWorked = input("How many hours did you work? \n")
    try:
        hoursWorked = float(hoursWorked)
        return hoursWorked
    except ValueError:
        print("Please enter a number(i.e. 24, not twenty-four)")
        return gethours()
            
def getrate():
    payPerHour = input("What is your hourly rate? \n")
    try:
        payPerHour = float(payPerHour)
        return payPerHour  
    except ValueError:
        print("Please enter a number(i.e. 24, not twenty-four)")   
        return getrate()

def computepay(hoursWorked,payPerHour):
    if hoursWorked <= 40:
        grosswages = hoursWorked * payPerHour
        print("Your Wages are: $",grosswages)
    else:
        grosswages = (payPerHour * 40) + ((hoursWorked - 40) * (payPerHour * 1.5)) 
        print("Your Wages are: $",grosswages)
        
computepay(gethours(),getrate())
        
        
        