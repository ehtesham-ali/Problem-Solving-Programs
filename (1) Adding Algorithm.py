# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def adding_algorithm(lst, k):
    '''
    This function takes in a lst of numbers (lst) and a number (k) and determines wheather any 2 numbers in lst add up to k
    '''

    modified_lst = lst[:]
    current_value = None

    for num in lst:
        modified_lst.remove(num)

        # This nested for loop checks if num plus any other numbers (excluding itself, which is why we remove that value in line 13) in that list add up to k
        for nested_num in modified_lst:
            current_value = num + nested_num
            if current_value == k:
                print(f'{num} + {nested_num} = {k}')
                print(True)
                return True
        modified_lst = lst[:]
    
    print(False)
    return False
