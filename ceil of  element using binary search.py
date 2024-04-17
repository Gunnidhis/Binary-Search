# Given a sorted array and a value target, the ceiling of target is the smallest element in 
# an array greater than or equal to target, and the floor is the greatest element smaller 
# than or equal to x.

def Binary_Search(nums,target):
    start = 0
    end = len(nums)-1
    ans= 1e5
    while start <= end:
        mid = start + ( end - start)//2
        if target == nums[mid]:
            return nums[mid]
        if nums[mid] > target:
            ans= min(ans,nums[mid])
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return ans


if __name__=="__main__":
    nums = [1,2,3,4,10,10,11,14]
    target = 9
    res = Binary_Search(nums,target)
    print(res)
