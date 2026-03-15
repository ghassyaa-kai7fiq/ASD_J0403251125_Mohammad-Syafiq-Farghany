def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ']})':
            if not stack or stack.pop()!= pairs[char]:
                return False
    
    return not(stack)


print(is_balanced("(2+3)*{4-5}"))  
print(is_balanced("(1+2)*(4-5)"))