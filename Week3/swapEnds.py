def swap_ends(my_str):
    first_char = my_str[0]
    last_char = my_str[-1] 
    remain_str = my_str[1:-1]

    new_str = print(f"{last_char}{remain_str}{first_char}")

    print(new_str)

swap_ends("boat")