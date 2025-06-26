import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("investment - to calculate the amount of interest you will earn on your investment")
print("bond       - to calculate the amount youll have to pay on a home loan. \n")

user_choice = input('Enter either "investment" or "bond" from the menu above to proceed: ')

if user_choice == "investment":
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter interest rate(as a number, e.g, 8 for 8%): "))
    years = float(input("Enter the number of years you plan to invest: "))
    interest = (input('Type "simple" or "compound" to choose the interest type: ')).lower()
    
    r = interest_rate / 100 
    
    if interest == "simple" : 
       total_amount = deposit * (1 + r * years) 
       print(f"\nTotal amount after {years} years with 'simple' interest: R{total_amount:.2f}")
    elif interest == "compound" :
        total_amount = deposit * math.pow((1 + r),years )   
        print(f"\nTotal amount after {years} years with compound interest: R{total_amount: .2f}")
    else: 
        print("\nInvalid interest type. Please choose either 'simple' or 'compound'. ")   

elif user_choice == "bond":
    house_value = float(input("Enter the present value of the house: "))  
 
    interest_rate = float(input("Enter the annual interest rate(e.g., 7 for 7%) ")) 
    months = int(input("Enter the number of months you plan to repay the bond: "))  
    
    annual_rate = interest_rate / 100
    monthly_rate = annual_rate / 12
    
    repayment = (monthly_rate * house_value)  / - math.pow((1 + monthly_rate), -months)
    print(f"\nYour monthly repayment is: R{repayment:.2f}")
else:
    print("\nInvalid input. Please choose either 'investment' or 'bond'. ") 
       
                                                 
    
                                                              
                                                              
                                                              
                                                              
                                                              
                                                              
    