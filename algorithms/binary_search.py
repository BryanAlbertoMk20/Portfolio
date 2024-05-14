# Return the index of the key
def binary_search(lt, key):
    left = 0
    right = len(lt) - 1
    while left <= right:
        middle = (left + right) // 2

        if lt[middle] == key:
            return middle
        if lt[middle] > key:
            right = middle - 1
        if lt[middle] < key:
            left = middle + 1
    return -1


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(binary_search(lst, 10))

# Check if the item is in the list
def find_item(lit, item):
    # Returns True if the item is in the list, False if not.

    if len(lst) == 0:
        return False

    # Is the item in the center of the list?
    middle = len(lst) // 2

    if lst[middle] == item:
        return True

    # Is the item in the first half of the list?
    if item < lst[middle]:
        # Call the function with the first half of the list
        print("First half of list")
        return find_item(lst[:middle], item)
    else:
        # Call the function with the second half of the list
        print("Second half of list")
        return find_item(lst[middle + 1:], item)


list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]
list_of_names.sort()

print(find_item(list_of_names, "Alex"))  # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False
