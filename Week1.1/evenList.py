
def get_evens(lst):
    evenList = []
    
    for num in lst:

        if num % 2 == 0:
            evenList.append(num)
    return evenList

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)