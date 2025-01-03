def isPolindrome(x: int):
    # if x < 0:
    #     return False
    return str(x) == str(x)[::-1]

print(isPolindrome(121)) # True
print(isPolindrome(-121)) # False
print(isPolindrome(10)) # False