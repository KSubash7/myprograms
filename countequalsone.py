def single_number(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1 
    
    for num, freq in count.items():
        if freq == 1:
            return num  

# Test cases
print(single_number([2,2,1]))  # Output: 1
print(single_number([4,1,2,1,2]))  # Output: 4
print(single_number([1]))  # Output: 1
