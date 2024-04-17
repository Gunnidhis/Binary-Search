
# Given a sorted array arr containing n elements with possibly some duplicate,
# the task is to find the first and last occurrences of an element x in the 
# given array.


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
    ans = first_occurance_element(nums,10)
    res = last_occurance_element(nums,10)
    print(ans,res)
    
