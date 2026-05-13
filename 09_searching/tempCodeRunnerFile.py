values = random.sample(range(10,20), 5)
print(f"The list is {values}")
target = int(input("Enter value to search: "))
result = linear_search(values, target) 
