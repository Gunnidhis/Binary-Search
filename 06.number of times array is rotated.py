# Given an array arr[] of size N having distinct numbers sorted in increasing order and
# the array has been right rotated(i.e, the last element will be cyclically shifted to 
# the starting position of the array) k number of times, the task is to find the value
# of k.

#intuition - The key idea behind this algorithm is find the index of the minimum element
#            in a rotated sorted array.because *** (very important conclusion :) index of
#            minimum element will give us how many times array has been  rotated***.


#            This algorithm has a time complexity of O(log n), where n is the length of the 
#            input array.

def rotated_sorted_array(nums):
    n=len(nums)
    start = 0
    end = n - 1
    while start <= end:
        mid = start + ((end - start)//2)
        
        prev = (mid + n -1) % n
        next = (mid + 1) % n
        if nums[start]<= nums[end]:
            return start

        if nums[prev] > nums[mid]  and nums[mid] <= nums[next]:
            return mid
        # if left part is sorted then search in right part of array
        elif nums[mid] >= nums[start]:
            start = mid + 1
        # if right part is sorted then search in left part of array
        elif nums[mid] <= nums[end]:
            end = mid - 1
 

if __name__ == "__main__":
    nums = [11,12,15,18,2,5,6,8]
    ans = rotated_sorted_array(nums)
    print(ans)
