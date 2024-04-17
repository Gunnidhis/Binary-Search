#Given an array of integers sorted in ascending order, and a target value, find the element in the array 
#that has minimum absolute difference with the target value.

#intuition - firstly think differnce will be minimum if  we substract the target value with element closest to it
#            i.e. we will try to insert the target value in array.( this is our assumption ) then we will 
#            find its neighbours.
#            conclusion : Only Both neighbours have only minimum difference because smaller elements and larger elements have
#                         large difference with target value

#  we will perform normal Binary Search, if target value is present in array then it have minimum differance with itself
#  every element has minimum differance with itself i.e. '0'( example "3 - 3 ", "5 - 5" , "8 - 8" )
#  if target value is not present then start and end pointer cross each other and give its neighbours' position
#  when 'start' and 'end' cross each other then they are closest differnce neighbour element with given target

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
