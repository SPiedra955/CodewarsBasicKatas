#Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, and returns
#a dictionary/hash which shows the least amount of coins used to make up that amount. The only coin denominations 
#considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). Therefor the dictionary 
#returned should contain exactly 4 key/value pairs.
#Notes:
#If the function is passed either 0 or a negative number, the function should return the dictionary with all values 
#equal to 0.If a float is passed into the function, its value should be rounded down, and the resulting dictionary should
#never contain fractions of a coin.

def loose_change(cents):
    
    change_dict = {'Nickels':0, 'Pennies':0, 'Dimes':0, 'Quarters':0}
    
    if cents <= 0:
        return change_dict
    
    while cents >= 1:
        
        if cents >= 25:
            change_dict['Quarters'] += 1
            cents -= 25
            
        elif cents >= 10:
            change_dict['Dimes'] += 1
            cents -= 10
            
        elif cents >= 5:
            change_dict['Nickels'] += 1
            cents -= 5
            
        else:
            change_dict['Pennies'] += 1
            cents -= 1
            
    return change_dict