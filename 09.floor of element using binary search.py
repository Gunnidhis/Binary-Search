# Given a sorted array and a value x, the ceiling of x is the smallest element in
# an array greater than or equal to x, and the floor is the greatest element smaller
# than or equal to x.

# intuition - if we find the array[mid] == x then it will okay and return the ans.
#             array[mid] is greater than x then it will not beneficial for us because 
#             we are searching for greater element smaller than x hence we will move left side
#             but if array[mid] is smaller than x then it might be a answer so we 
#             should store it in a variable and continue for searching in right side beacause
#             array is sorted and we are searching grestest element less than x. 

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

