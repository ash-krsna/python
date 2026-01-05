# given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#example: nums = [0,1,0,3,12] => [1,3,12,0,0]
def move_zeroes(nums):
    """
    Move all 0's in the list nums to the end while maintaining the order of non-zero elements.
    
    Args:
    nums (List[int]): List of integers to be modified in place.
    
    Returns:
    None: The function modifies the list in place.
    """
    # Initialize a pointer for the position of the next non-zero element
    non_zero_index = 0
    
    # Iterate through the list
    for i in range(len(nums)):
        # If the current element is not zero, place it at the non_zero_index and increment the index
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    
    # After all non-zero elements have been moved, fill the rest of the list with zeros
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
# Example usage:
nums = [0, 1, 0, 3, 12]