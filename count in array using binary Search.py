# Given a sorted array arr[] and a number x, write a function that counts 
# the occurrences of x in arr[]. Expected time complexity is O(Logn) 



# This Python code implements a solution to find the count of a specific element in a sorted array.

#          Here's a brief explanation of what the code does:

#          1.)count_element(nums, x) is the main function that takes an array nums and an element x to search for.
#          It returns the count of the occurrences of x in the nums array.
                                                                                                  
#          2.)first_occurance_element(nums, x) is a helper function that uses binary search to find the index of
#             the first occurrence of x in the nums array. It initializes first to a large value (1e5) and updates it
#             to the minimum index where x is found.

#          3.)last_occurance_element(nums, x) is another helper function that uses binary search to find the index 
#             of the last occurrence of x in the nums array. It initializes last to a small value (-1e5) and updates 
#             it to the maximum index where x is found.
  
#          4.)The count_element(nums, x) function calls the first_occurance_element(nums, x) and 
#             last_occurance_element(nums, x) functions to find the first and last occurrences of x in the nums array. 
#             It then calculates the count of x by subtracting the first occurrence index from the last occurrence index and adding 1.

#          5.)In the if __name__ == "__main__": block, the code creates a sample nums array and a target element Search (which is 10).
#            It then calls the count_element(nums, Search) function and prints the result.


def count_element(nums,x):
    first = first_occurance_element(nums,x)
    last = last_occurance_element(nums,x)
    count = last - first + 1
    return count

def first_occurance_element(nums,x):
    start = 0
    end = len(nums)-1
    first=1e5
    while start <= end:
        mid = start + (end - start)//2
        if x == nums[mid]:
            first = min(first,mid)
            end = mid-1 
        elif x < nums[mid]:
            end = mid-1
        else:
            start = mid + 1
    return first

def last_occurance_element(nums,x):
    start = 0
    end = len(nums)-1
    last=-1e5
    while start <= end:
        mid = start + (end - start)//2
        if x == nums[mid]:
            last = max (last,mid)
            start = mid + 1
        elif x < nums[mid]:
            end = mid-1
        else:
            start = mid + 1
    return last
if __name__ == "__main__":
    nums = [7,8,9,10,10,10,10,10,10,11,12,13]
    Search = 10
    ans = count_element(nums,Search)
    print(ans)
