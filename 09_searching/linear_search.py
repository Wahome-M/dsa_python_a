import random
from xml.etree.ElementTree import _Target

def linear_search(values, target):
    for index in range(len(values)):
        print(f"Comparing {target} vs {values[index]}")
        if target == values[index]:
            return index
    
    return -1

values = random.sample(range(10,20), 5)
print(f"The list is {values}")
target = int(input("Enter value to search: "))
result = linear_search(values, target) 
