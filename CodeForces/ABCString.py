def calc(s):
    char_1 = s[0]
    stack = []
    for ele in s:
        if ele == char_1:
            stack.append(ele)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO" 


b = int(input())
for i in range(b):
    s = list(input())
    result = calc(s)
    print(result)
    
           
    