def doubled(lst):
    new_lst = []
    for num in lst:
        new_lst.append(num* -1)

    return new_lst

lst = [1,-5,1,2]

print(doubled(lst))
