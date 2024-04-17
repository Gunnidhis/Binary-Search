# if you are interest to learn DSA with Hands-on experience please consider me repository....


# The code you provided is a Python implementation of the classic Binary Search algorithm.

# Here's a step-by-step explanation of what's happening in the code:

#                     1. The `Binary_search` function takes two arguments:
#                        - `nums`: a sorted array of numbers
#                        - `search`: the target element to search for in the `nums` array
                    
#                     2. The function initializes two pointers, `start` and `end`, to the beginning 
#                        and end of the `nums` array, respectively.
                    
#                     3. The function then enters a `while` loop that continues as long as `start` 
#                        is less than or equal to `end`. This loop represents the binary search process.
                    
#                     4. Inside the loop, the function calculates the `mid` point of the current search
#                        range using the formula `mid = start + (end - start) // 2`. This formula ensures
#                        that the calculation doesn't overflow, even for very large arrays.
                    
#                     5. The function then checks if the `search` element is equal to the element at the `mid`
#                        index in the `nums` array.
#                        - If they are equal, the function returns the `mid` index, as this is the location of the `search` element.
                    
#                     6. If the `search` element is less than the element at the `mid` index, the function updates
#                        the `end` pointer to `mid - 1`, effectively discarding the right half of the search range.
                    
#                     7. If the `search` element is greater than the element at the `mid` index, the function updates
#                        the `start` pointer to `mid + 1`, effectively discarding the left half of the search range.
                    
#                     8. If the `while` loop completes without finding the `search` element, the function returns `-1`,
#                        indicating that the element was not found in the `nums` array.
                    
#                         In the `if __name__ == "__main__":` block, the code:
#                         1. Creates a sorted array `nums` with the values `[1, 2, 3, 4, 5, 6, 7, 9]`.
#                         2. Defines a `search` element with the value `1`.
#                         3. Calls the `Binary_search` function with the `nums` array and the `search` element.
#                         4. If the `Binary_search` function returns a non-negative value, it prints the index of the `search` element.
#                         5. If the `Binary_search` function returns `-1`, it prints `"element not Find"`.


# This code demonstrates the basic implementation of the Binary Search algorithm, which is a efficient way to search for 
# an element in a sorted array. The time complexity of the Binary Search algorithm is O(log n), where n is the size of 
# the input array.


def Binary_search(nums,search):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = start + (end - start)//2
        if search == nums[mid]:
            return mid
        # if search element is smaller than mid ,ignore right part
        elif search < nums[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,9]
    search = 1
    ans = Binary_search(nums,search)
    if ans != -1:
        print(ans)
    else:
        print("element not Find")
    
