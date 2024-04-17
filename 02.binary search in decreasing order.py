#search for an element x in a reverse-sorted (descending order) array nums.


# intuition - because array is sorted in decreasing order so if array[mid] == x then return 
#             it's index but if x is smaller than array[mid] then we will search in right side( bcz 
#             array is sorted in decreasing order so smaller element will found in right side of array)
#             similarly if x is greater then array[mid] then we will move to left part (reason is same
#             descriebed in above : array is sorted in decreasing order).


# funtioning of code :

# It initializes start and end pointers to the beginning and end of the nums array, respectively.
# It enters a while loop that continues as long as start is less than or equal to end.
# Inside the loop, it calculates the mid point of the current search range.
# It then compares the target element x with the element at the mid index:
# If they are equal, it returns the mid index.
# If x is greater than the element at mid, it updates end to mid - 1 (since the array is in reverse order).
# If x is less than the element at mid, it updates start to mid + 1 (since the array is in reverse order).
# If the while loop completes without finding x, it returns -1 to indicate that the element was not found.

def reverse_sorted_ie_decending_order(nums,x):
    start=0
    end = len(nums)-1
    while start <= end:
        mid = start + (end - start)//2
        if x == nums[mid]:
            return mid
        elif x > nums[mid]:
           end = mid - 1
        else:
           start = mid + 1
    return -1

if __name__== "__main__":
    nums = [10,9,8,7,6,5,4,3,2,1]
    Search = 7
    ans = reverse_sorted_ie_decending_order(nums,Search)
    print(ans)
