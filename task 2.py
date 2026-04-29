def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # 0+4 = 4, 4+9 = 13, 13+2 = 15, 15+1 = 16
    return total

result = tally([4, 9, 2, 1]) # result = 16

####

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # new_list = [4] , new_list = [4, 9]
    return new_list                    # new_list = [4, 9, 2] , new_list = [4, 9, 2, 1]
    # This loop creates a new list by copying the previous one

result = copy([4, 9, 2, 1]) # new_list = [4, 9, 2, 1]

####

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # new_list = [4+1] = [5] , new_list = [5, 9+1=10] = [5, 10]
    return new_list # new_list = [5, 10, 2+1=3] = [5, 10, 3] , # new_list = [5, 10, 3, 1+1=2]
    # = [5, 10, 3, 2]

result = increment_all([4, 9, 2, 1])