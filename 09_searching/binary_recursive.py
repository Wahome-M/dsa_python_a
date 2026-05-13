import random

def binary_recursive(values, target, low ,high):
    if low>high:
        return -1
    
    mid = (low+high)//2
    if target == values(mid):
        return mid
    elif target>values[mid]:
        return binary_recursive()



values = random.sample(range(10,20), 5)
print(f"The list is {values}")
target = int(input("Enter value to search: "))
result = binary_recursive(values, target) 
