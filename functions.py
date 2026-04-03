def computepay( ):
     #requesting  the hours from the user
    hours = input("Enter hours: ")
     #converting the string to a float
    hrs = float(hours)

    #requesting the rate per hour from the user
    rateperhour = input("Enter rate per hour: ")

    #converting the rate per hour from string to float
    rpm = float(rateperhour)

   #standard working hours is 40 for all the workers
    standard_hour = 40

   #conditional if someone works more than 40 hours
    if hrs > standard_hour :
        overtime = hrs - standard_hour
        pay = (standard_hour * rpm) + (rpm * overtime * 1.5)
        return pay

    else:
       pay = standard_hour * rpm
       return pay


#calling the function
print("Pay",computepay())
