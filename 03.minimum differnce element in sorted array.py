#Given an array of integers sorted in ascending order, and a target value, find the element in the array 
#that has minimum absolute difference with the target value.

#intuition - firstly think differnce will be minimum if  we substract the target value with element closest to it
#            i.e. we will try to insert the target value in array.( this is our assumption ) then we will 
#            find its neighbours.
#            conclusion : Only Both neighbours have minimum difference because small element and larger element have
#                         last difference.

def Binary_search(nums,target):
    start = 0
    end = len(nums)-1
    ans= 1e5
    while start <= end:
        mid = start + (end- start)//2
        if nums[mid] == target:
            return key
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    # when 'start' and 'end' cross each other then they are closest differnce neighbour element with given target
    print(start,end) 
    ans = min(ans,abs(nums[start]-target),abs(nums[end]-target))
    return ans


if __name__ == "__main__":
    nums = [1,3,8,10,15]
    target = 12
    ans = Binary_search(nums,target)
    print(ans)
