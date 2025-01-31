n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)
print("Array elements:", arr)
for num in arr:
    print(num)
