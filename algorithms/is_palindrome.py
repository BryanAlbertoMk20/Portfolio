
def isPalindrome(x):

    num = str(x)

    reverse_num = num[::-1]

    if num == reverse_num:
        return True
    else:
        return False


print(isPalindrome(-121))


