# Given a sorted and rotated array arr[] of size N and a key, the task is to find the key in the array.
#Note: Find the element in O(logN) time and assume that all the elements are distinct.

#intuition - firstly we will find the minimum element of array then array is divided into two sorted array 
#                     1 : first array will be from start to minimum element index - 1
#                     2 : second array will be from minimum element index to end
#            so we fill implement the Binary Search independently in both the arrays


def BinarySearch(start,end,nums,target):
    while start <= end:
        mid= start + (end - start)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1 
    return -1

def findMin(nums,n):
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start)//2
        prev = (mid + n - 1) % n
        next = (mid + 1) % n
        if nums[start] <= nums[end]:
            return start
        if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
            return mid
        elif nums[mid] <= nums[end]:
            end = mid - 1
        else:
            start = mid + 1

if __name__ == "__main__":
    nums=[11,12,15,18,2,5,6,8]
    target = 2
    min_element_index = findMin(nums,len(nums))
    first_call = BinarySearch(0,min_element_index-1,nums,target)
    second_call = BinarySearch(min_element_index,len(nums)-1,nums,target)
    print(first_call)
    if first_call == -1 and second_call == -1:
        print(-1)
    print(first_call if first_call >= 0 else second_call)
