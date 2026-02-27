 
    #nums = [8, 2, 13, 11, 4, 10, 14]
    #threshold = 10
    # output = [13, 11, 14]

def above_threshold(nums, threshold):
    final_list = []

    for num in nums:
        if (num > threshold):
            final_list.append(num)


    return final_list

print("Test run", above_threshold([8, 2, 13, 11, 4, 10, 14], 10))