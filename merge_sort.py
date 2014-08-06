from random import randrange

def is_sorted(L):
    """
    returns True if the list is sorted in ascending order.
    False otherwise.
    """
    for i in range(1, len(L)):
        if L[i] < L[i-1]:
            return False

    return True            


def merge(L1, L2):
    """
    input: L1 and L2 are lists (sorted)
    output: List
    merges two lists and returns a sorted List
    """
    merged = []
    #indices for iterating over L1 and L2
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            #append L1[0] to merged and remove from L1
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    
    #now extend the list
    merged.extend(L1[i:])
    merged.extend(L2[j:])
    
    return merged


def merge_sort(L):
    """
    sorts a list using merge sort algorithm in ascending order
    """
    if len(L) < 2:
        return L
    else:
        #parts of the list and recursive call on them
        L1 = merge_sort(L[: len(L)/2])
        L2 = merge_sort(L[len(L)/2 : ])
        
        return merge(L1, L2)

def test_sorting():
    """
    test for merge sort using randomly created list
    """
    failed = 0
    #testing for 100 random cases
    for i in range(100):
        #create random list
        length = randrange(1, 21)
        lst = [randrange(1, 10) for i in range(length)]
        #lists created by algorithm and python internal implementation
        lst1 = merge_sort(lst)
        if not(is_sorted(lst1)):
            failed += 1
            print "test failed for:" , lst
            print "computed:", lst1
    
    if failed == 0:
        print "test passed for merge sort" 

test_sorting()    
