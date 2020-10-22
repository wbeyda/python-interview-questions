def rob(nums):
    even = sum(nums[1::2])
    odd = sum(nums[0::2])
    """
    if len(nums) % 2:  # odd number of houses
        #even = sum([i for i in range(len(nums)) if i % 2 == 1])
        even = sum(nums[1::2])
        #odd = sum([i for i in nums[:-1] if i % 2])
        odd = sum(nums[0::2])

    if len(nums) % 2 == 0:  # even number of houses
        #even = sum([i for i in nums if i % 2 == 0])
        even = sum(nums[1::2])
        #odd = sum([i for i in nums if i % 2])
        odd = sum(nums[0::2]) 
    """

    return even if even > odd else odd

if __name__ == '__main__':
    a = [1,2,3,1] #4
    b = [1,2,3,4,5] #9
    c = [1,4,5,7,9,10]

    print(rob(a))
    print(rob(b))
    print(rob(c))
