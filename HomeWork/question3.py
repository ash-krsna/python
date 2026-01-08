#given an array nums containg n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
input: [3,0,1]
output: 2  
nums = [3,0,1]
n = len(nums)
total = n * (n + 1) // 2n  asdfj
sum_of_nums = sum(nums)
missing_number = total - sum_of_nums
print(missing_number)