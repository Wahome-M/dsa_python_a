def head_recursion(n):
    if n<1:
        return n
    
    head_recursion(n-1)
    print(n)
    
head_recursion(5)

### does the recursion at the start of the code