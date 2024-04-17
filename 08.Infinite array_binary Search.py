# In this topic "Infinite array" we will do the Two questions :

#       1: Position of element in infinite array
#       2: index of first 1 in binary sorted array

# which are not possible to come in coding round  because infinite array is not possible but it is
# the possible that interviewer will ask someone to implement the binary search in infinite array

# 1 Question : Position of  an element in infinite array

# intuition - mid index is always between the start and end indices. 
#             hence first we assume start = 0 and end = 1 
#             update 'end' index to its double (end = end * 2 ) while array[end] index is less than target
#             and simultaneously we update the start to end ( i.e. start = end or low = high or see line 22 ) 
#             in the last we will have the sequence i.e. start ----- mid ----- end
#             now we will have the start and end pointer to implement the Binary Search as usual

def Position_of_element_Binary_Search(nums,key: int)->int:
    start = 0
    end = 1
    while nums[end] < key:
        start = end
        end *= 2
        
    while start <= end:
        mid = start + (end - start)//2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            start = mid + 1
        else:
            end = mid -1
    return -1

     

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    target = 7
    ans = Position_of_element_Binary_Search(nums,target)
    print(ans)

#output : 6


# 2 Question : we have binary sorted array ( binary sorted array is defined as array which will have 
#              only '0' and '1' and array is sorted i.e. all '0' are together and all '1' are together)
#              we have to find the index of first 1 in infinite array


# intuition - this question will be addition of two Questions(first occurance of element + infinite array concept using Binary Search)
#                        1. firstly we adjust our mid according to infinite array concept
#                        2. Apply first occurance concept in it i.e. if array[mid] == target ( in this case  target = 1 )
#                           we will continue our search because it might be a answer ( first occurance ) so store it in avariable and
#                           move left side ( i.e end = mid - 1 )  because first occurance  will be found in left side.




def infinite_Binary_sorted_array(nums,target):
    start = 0
    end = 1
    res = 1e5
    while nums[end] < target:
        start = end
        end *= 2
    
    while start <= end :
        mid = start + (end - start)//2
        if nums[mid] == target:
            res = min(res,mid)
            end = mid - 1
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return res

    
if __name__ == "__main__":
    nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 1
    ans = infinite_Binary_sorted_array(nums,target)
    print(ans)

#output : 50
