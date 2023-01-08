
## Name:Ana Camba Gomes


##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
cost_of_dream_home = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as decimal:")) 

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05 

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

months = 0 
actual_downpayment = portion_down_payment * cost_of_dream_home

while amount_saved < actual_downpayment:
        investment_return = (amount_saved * (r/12)) 
        monthly_salary_saved = (yearly_salary * portion_saved) / 12 
        amount_saved = monthly_salary_saved + amount_saved + investment_return 
        months = months + 1
        if months % 6 ==0:
            yearly_salary_percentage = yearly_salary * semi_annual_raise
            yearly_salary = yearly_salary + yearly_salary_percentage
        
print('Number of months:' , months)

