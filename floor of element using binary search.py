# Given a sorted array and a value x, the ceiling of x is the smallest element in
# an array greater than or equal to x, and the floor is the greatest element smaller
# than or equal to x.

def Binary_Search(nums,target):
    start = 0 
    end = len(nums) - 1
    ans = -1
    while start <= end:
        mid = start + (end - start)//2
        if target == nums[mid]:
            return target
        if nums[mid]<target:
            ans = max(ans,nums[mid])
            start = mid + 1
        elif nums[mid] > target:
            end = mid -1
    return ans


if __name__=="__main__":
    nums = [1,2,3,4,10,10,11,14]
    target = 5
    res = Binary_Search(nums,target)
    print(res)

