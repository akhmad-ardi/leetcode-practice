def isValid(s: str) -> bool:    
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

case1 = "()"
case2 = "()[]{}"
case3 = "(]"
case4 = "([])"

print(isValid(case1))
print(isValid(case2))
print(isValid(case3))
print(isValid(case4))