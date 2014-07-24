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

def test_merge_sort():
    test = [[8, 7, 6, 6, 1, 5, 4, 2, 3, 1], [2], 
            [1, 2, 3, 4], [8, 9, 8, 9, 8, 1, 7, 6]]
    expected = [[1, 1,  2, 3, 4, 5, 6, 6, 7, 8], [2],
                [1, 2, 3, 4], [1, 6, 7, 8, 8, 8, 9, 9]]
    
    for idx in range(len(test)):
        failed = 0
        if merge_sort(test[idx]) != expected[idx]:
            failed += 1
            print "test failed for:", test[idx]
            print "computed:", merge_sort(test[idx])
            print "expected:", expected[idx]
            print "--------------------------------"
            
    if failed == 0:
        print "merge_sort: tests passed"
    else:
        print "test failed: review code"

test_merge_sort()        
