
## Name: Ana Camba Gomes

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit:"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25 
epsilon = 100
high = 1.0
low = 0.0

down_payment = cost_of_dream_home * portion_down_payment
amount_saved = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

steps = 0
months = 36 
r = 0.0

if initial_deposit * (1+1/12)**months < down_payment - epsilon:
    r = None
    print('Best savings rate:', r)
    print('Steps in bisection search:', steps)
    
elif initial_deposit >= down_payment - epsilon:
    r = 0.0
    print('Best savings rate:', r)
    print('Steps in bisection search:', 0)

else:
    amount_saved = initial_deposit

    while abs(amount_saved - down_payment) >= epsilon:
        r = (high + low)/2.0
        amount_saved = initial_deposit * (1+r/12)**months
        steps = steps + 1
        
        if amount_saved > down_payment + epsilon:
            high = r
            
        else: 
            
            low = r

    print('Best savings rate:', r)
    print('Steps in bisection search:', steps)
    

    
    


        

        
    
   
    
    


        

