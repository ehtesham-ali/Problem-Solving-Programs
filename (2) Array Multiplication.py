# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def array_multiplication(lst):
    '''
    This function takes in a list of numbers (lst) and returns a new list such that each element at index
    i of the new array is the product of all the numbers in the original array except the one at i
    '''
    modified_lst = lst[:]
    return_lst = []
    current_value = 1

    for val in lst:
        modified_lst.remove(val)
        
        # This nested for loop goes through all the numbers (excluding val in line 14 as demanded in the promt) and multiplies them, then appending that value in line 20
        for nested_val in modified_lst:
            current_value *= nested_val
        
        return_lst.append(current_value)
        modified_lst = lst[:]
        current_value = 1
    
    print(return_lst)
    return return_lst
