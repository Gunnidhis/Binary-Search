#Given an array of integers sorted in ascending order, and a target value, find the element in the array 
#that has minimum absolute difference with the target value.

def Binary_search(nums,target):
    start = 0
    end = len(nums)-1
    ans= 1e5
    while start <= end:
        mid = start + (end- start)//2
        if nums[mid] == key:
            return key
        elif nums[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    # when 'start' and 'end' cross each other then they are closest differnce neighbour element with given target
    print(start,end) 
    ans = min(ans,abs(nums[start]-key),abs(nums[end]-key))
    return ans


if __name__ == "__main__":
    nums = [1,3,8,10,15]
    target = 12
    ans = Binary_search(nums,key)
    print(ans)
