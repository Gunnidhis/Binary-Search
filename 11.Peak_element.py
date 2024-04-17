#question : A peak element is an element that is strictly greater than its neighbors.
#           Given a 0-indexed integer array nums, find a peak element, and return its index. 
#           If the array contains multiple peaks, return the index to any of the peaks.
    
#           You must write an algorithm that runs in O(log n) time.


# intuition - array is some-how sorted in increasing and decreasing order so we should think about Binary Search.
#             peak element is element which is greater element with it's neighbours i.e. array[mid] > array[mid+1]
#             and array[mid] > array[mid -1] then return its index

#             lets consider an array = [2,3,6,5] if start = 0 and end = 3 then mid = 0 + 3 // 2, mid = 1 which is 
#             array[1] = 3, 3 is greater than 2 but smaller than 6 hence we can say 2 can never be a peak element because
#             greater element 3 is already present and 3 is not a peak element due to the 6 so 6 might be a peak element
#             because we know 6 is greater then 3 so there is possibility of 6 to be peak element if it will be greater 
#             than its neighbour to right.

#             ***Very Important Conclusion : we will move in that direction due to which our element got fail for becominig
#              peak element. if next element is greater than array[mid] we will move to righti.e. start = mid + 1 if prev
#              element is greater than array[mid] we will move to left side i.e. end = mid - 1***

# we should also take care of edge-Cases if mid == 0 and mid == n - 1 so it will have only one neighbour i.e. 1 and n-2
# index respectivily

def peak_element(nums):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if mid > 0 and mid < end:
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid + 1] > nums[mid]:
                start = mid + 1
            elif nums[mid - 1] > nums[mid]:
                end = mid - 1
        elif mid == 0:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        elif mid == end:
            if nums[end] > nums[end - 1]:
                return end
            else:
                return end - 1


if __name__ == "__main__":
    nums = [5, 10, 15, 17, 12, 13, 6]
    index_of_peak_element = peak_element(nums)
    print(index_of_peak_element)
