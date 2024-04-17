# Given a sorted array and a value target, the ceiling of target is the smallest element in 
# an array greater than or equal to target, and the floor is the greatest element smaller 
# than or equal to x.


# intuition - if we find the array[mid] == x then it will okay and return the ans.
#             array[mid] is less than x then it will not beneficial for us because 
#             we are searching for smallest element greater than x hence we will move right side
#             but if array[mid] is greater than x then it might be a answer so we 
#             should store it in a variable and continue for searching in left side beacause
#             array is sorted and we are searching smallest element greater than x


            # The code you provided is an implementation of a modified Binary Search algorithm that
            # finds the smallest element greater than or equal to the target element in a sorted array.
            
            # Let's go through the code step by step:
            
            # 1. The `Binary_Search` function takes two arguments:
            #    - `nums`: a sorted array of numbers
            #    - `target`: the target element to search for in the `nums` array
            
            # 2. The function initializes two pointers, `start` and `end`, to the beginning and
            # end of the `nums` array, respectively. It also initializes a variable `ans` to a 
            # very large value (1e5).
            
            # 3. The function then enters a `while` loop that continues as long as `start` is 
            # less than or equal to `end`. This loop represents the binary search process.
            
            # 4. Inside the loop, the function calculates the `mid` point of the current search
            # range using the formula `mid = start + (end - start) // 2`. This formula ensures 
            # that the calculation doesn't overflow, even for very large arrays.
            
            # 5. The function then checks if the `target` element is equal to the element at 
            # the `mid` index in the `nums` array.
            #    - If they are equal, the function returns the element at the `mid` index.
            
            # 6. If the `target` element is greater than the element at the `mid` index, the 
            # function updates the `start` pointer to `mid + 1`, effectively discarding the left 
            # half of the search range.
            
            # 7. If the `target` element is less than the element at the `mid` index, the function
            # updates the `ans` variable to the minimum of the current `ans` and the element at the 
            # `mid` index. It then updates the `end` pointer to `mid - 1`, effectively discarding the
            # right half of the search range.
            
            # 8. If the `while` loop completes without finding an exact match for the `target` element,
            # the function returns the `ans` variable, which will be the smallest element greater than 
            # or equal to the `target` element in the `nums` array.
            
            # In the `if __name__ == "__main__":` block, the code:
            # 1. Creates a sorted array `nums` with the values `[1, 2, 3, 4, 10, 10, 11, 14]`.
            # 2. Defines a `target` element with the value `9`.
            # 3. Calls the `Binary_Search` function with the `nums` array and the `target` element.
            # 4. Prints the result of the `Binary_Search` function, which in this case will be `10`,
            # as it is the smallest element in the `nums` array that is greater than or equal to the
            # `target` element of `9`.
            
            # This modified Binary Search algorithm is useful when you need to find the smallest element 
            # in a sorted array that is greater than or equal to a given target element. The time complexity
            # of this algorithm is still O(log n), where n is the size of the input array.

def Binary_Search(nums,target):
    start = 0
    end = len(nums)-1
    ans= 1e5
    while start <= end:
        mid = start + ( end - start)//2
        if target == nums[mid]:
            return nums[mid]
        if nums[mid] > target:
            ans= min(ans,nums[mid])
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return ans


if __name__=="__main__":
    nums = [1,2,3,4,10,10,11,14]
    target = 9
    res = Binary_Search(nums,target)
    print(res)
