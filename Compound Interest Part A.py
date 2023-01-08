## Name: Ana Camba Gomes



##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
cost_of_dream_home = float(input("Enter the cost of your dream home:"))



#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25 
amount_saved = 0
r = 0.05 #annual rate of return 
monthly_salary_saved = (yearly_salary * portion_saved) / 12 

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
months = 0
actual_downpayment = portion_down_payment * cost_of_dream_home

while amount_saved <= actual_downpayment:
        investment_return = (amount_saved * (r/12)) 
        amount_saved = monthly_salary_saved + amount_saved + investment_return 
        months = months + 1
print('Number of months:' , months)
        
        
        
        
    
    
    
