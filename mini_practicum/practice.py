def max(an_array, index=0, max_value=None):
    '''
    This function returns the highest number value in a given array
    '''
    if len(an_array) == 0:
        return None # Returns none if the length of an array is equal to 0
    
    if max_value == None:
        max_value = an_array[index]
    
    if index == len(an_array):
        # Stops recursive immediately and returns the max value if the index has reached to the end of an array
        return max_value

    if an_array[index] > max_value:
        # Updates max value and calls for next iteration
        return max(an_array, (index+1), max_value=an_array[index])
    else:
        # Otherwise call the next stack
        return max(an_array, (index+1), max_value=max_value)
    
def power(base, exponent):
    '''
    This function is a mathematical formula that return power calculation using divide and conquer method
    '''
    if exponent < 0:
        # If exponent value is less than 0, it is undefined, return None
        return None
    
    if exponent == 0:
        # If exponent value is equal to 0, return 1
        return 1
    
    if exponent == 1:
        # If exponent value is 1 then return the base value
        return base
    
    # If it all passes the guard clauses, it will now go into the actual calculation below:
    
    if exponent % 2 == 0:
        # power calculation when exponent is even
        return power(base, exponent//2) * power(base, exponent//2)
    else:
        # power calculation when exponent is odd
        return base * power(base, exponent//2) * power(base, exponent//2)