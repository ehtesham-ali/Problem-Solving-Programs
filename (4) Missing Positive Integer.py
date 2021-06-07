# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def missing_positive_integer(lst):
    '''
    This function takes in a list (lst) and returns the lowest positive interger that is missing from the list
    '''
    sorted_lst = sorted(lst)
    final_lst = []
    index = 0
    change = False

    # This for loop puts all numbers greater than 0 in a separate list
    for number in sorted_lst:
        if number > 0:
            final_lst.append(number)

    # If a number minus its previous is not equal to 1 or 0 we return the previous number plus 1 and increase the counter by 1
    for number in final_lst[1:]:
        value = number - final_lst[index]
        if value != 1 or 0:
            print(final_lst[index] + 1)
            change = True
            return final_lst[index] + 1

        index += 1
    
    # If there are no missing positive integers from the list, we return the next integer
    if change == False:
        print(final_lst[-1] + 1)
        return final_lst[-1] + 1
