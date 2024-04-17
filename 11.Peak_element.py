#question : A peak element is an element that is strictly greater than its neighbors.
#           Given a 0-indexed integer array nums, find a peak element, and return its index. 
#           If the array contains multiple peaks, return the index to any of the peaks.
    
#           You must write an algorithm that runs in O(log n) time.

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
