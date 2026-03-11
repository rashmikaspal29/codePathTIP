################################# Problem 2########################

# Write a function that takes in two dictionaries, 
# dict1 and dict2 and finds all keys common to both dictionaries. 
# The function returns a list of common keys.

# def common_keys(dict1, dict2):
# 	pass
# Example Usage:

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)
# Example Output:

# ['b', 'c']

#Understanding:
#  2 dictionaries dict1 and dict2, common_list
# initialize the list then append to it, the keys
#index the keys out from the dict and use for loop too
# Output: list of key (string)

#Planning:
#Step 1: Init result List
#Step 2: Loop dictionary 1
#Step 3: check IF key of dict NOT IN dict 2 
#Step 4: append the key to the resultList

dict1 = {"a": 1, "b": 2, "c": 3, "e":7}
dict2 = {"b": 4, "c": 5, "d": 6, "f":8}
#common_list = common_keys(dict1, dict2)
#print(common_list)

def common_keys(dict1, dict2):
    temp = []
    for element in dict1:
        if element in dict2.keys():
            temp.append(element)
    return temp
        #for diff_element in dict2:

         #   if dict1[element] == dict2[diff_element]:
          #      temp.append
        

common_list = common_keys(dict1, dict2)
print(common_list)