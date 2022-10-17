# Single Number:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Example 1:

# Input: nums = [2,2,1]
# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:

# Input: nums = [1]
# Output: 1


# listn = input("Enter the Number list: ")

def singleNumber(nums) -> int:
    counts = {}
    for n in nums :
        if n in counts:
            counts[n]+=1
        else:
            counts[n]=1
    
    for n in nums:
        if counts[n] ==1:
            return n



n1 = singleNumber([4,1,2,1,2])
print (n1)




