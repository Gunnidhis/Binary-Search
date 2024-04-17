if you are interest to learn DSA with Hands-on experience please consider me repository....


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
    
