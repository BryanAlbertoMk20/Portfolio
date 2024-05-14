nums = [1,2,3,4,5,6,7,8,9]

# def linear_search(lst, target_value):
#     for i in range(len(lst)):
#         if lst[i] == target_value:
#             return i


def linear_search(lst, target_value):
    if target_value in lst:
        index = lst.index(target_value)
        return index


def return_value(num_lst,idx):
    return num_lst[idx]




