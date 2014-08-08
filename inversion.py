def inversion_brute(lst):
    """
    input: a list
    output: an integer
    
    returns number of inversions in the list L using brute
    force algorithm
    """
    count_inversion = 0
    #if element on the right is less than element on the left
    #it is one inversion
    for idx in range(len(lst)):
        for jdx in range(idx + 1, len(lst)):
            if lst[jdx] < lst[idx]:
                count_inversion += 1

    return count_inversion


def merge_and_count(L1, L2):
    """
    input: L1 and L2 are sorted lists
    output: tuple of a list and an integer
    
    returns a merged list which is sorted in ascending order
    and number of split inversions with respect to two elements
    """
    #indices for both lists
    idx = 0 #for L1
    jdx = 0 #for L2
    #ans list to return
    ans = []
    count = 0 #for couting number of split inversion

    while idx < len(L1) and jdx < len(L2):
        if L1[idx] > L2[jdx]:
            #case of inversion, step to the next element in L2
            ans.append(L2[jdx])
            jdx += 1
            #increment inversion count
            count += len(L1) - idx
        else:
            ans.append(L1[idx])
            idx += 1
        
        #print ans

    #extend the list
    ans.extend(L1[idx: ])
    ans.extend(L2[jdx: ])
    
    return ans, count


def test_merge_and_count():
    """
    test for merge and count
    """
    f = merge_and_count
    failed = 0
    test = [[[1,3,5], [2,4,6]], [[1], [8,9,11]],
            [[1,5,6], [2,3,4]]]
    expected = [3,0,6]
    expected_lst = [[1,2,3,4,5,6], [1,8,9,11], [1,2,3,4,5,6]]
    
    for idx in range(len(test)):
        lst, x = f(test[idx][0], test[idx][1])
        if x != expected[idx] or lst != expected_lst[idx]:
            failed += 1
            print "test failed for:", test[idx]
            print "computed:" , lst, x
            print "expected:", expected_lst[idx], expected[idx]

    if failed == 0:
        print "merge_and_count: tests passed"
    else:
        print "merge_and_count: tests failed; review code" 
        
    
test_merge_and_count()
        
def sort_and_count(lst):
    """
    input: an unsorted list
    output: a tuple of a sorted list and an integer

    sorts a list using merge sort algorithm in ascending order and returns the list
    and number of split inversions between the first half and last half of the input list
    """
    if len(lst) < 2:
        return lst, 0
    else:
        #parts of the list and recursive call on them
        lst1, x = sort_and_count(lst[: len(lst)/2]) 
        lst2, y = sort_and_count(lst[len(lst)/2 : ])
        #merge the list ; splits is split inversions between the two halves of the list
        merged, splits = merge_and_count(lst1, lst2) 

        return merged, splits


def inversion_and_sort(lst):
    """
    input: a list
    output: sorted list and integer
    
    returns the sorted version of the input list and number of inversions in the
    list using divide and conquer
    """
    #base case
    if len(lst) < 2:
        return lst, 0
    #recursive case
    else:
        #x, y are counts of inversions within the two halves
        lst_left, x = inversion_and_sort(lst[:len(lst)/2])
        lst_right, y = inversion_and_sort(lst[len(lst)/2: ])
        #z is the count of split inversion between the two halves
        result_lst, z = merge_and_count(lst_left, lst_right)
        
        return result_lst, x+y+z

def test_inversion_and_sort():
    """
    test of inversion_and_sort method
    """
    f = inversion_and_sort
    failed = 0
    test = [[], [1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1],
            [1, 3, 5, 2, 4, 6]]
    expected_lst = [[], [1], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 
                    [1, 2, 3, 4, 5, 6]]
    expected = [0,0,0,15,3]
    
    for idx in range(len(test)):
        lst, x = f(test[idx])
        if lst != expected_lst[idx] or x != expected[idx]:
            failed += 1
            print "test failed for:", test[idx]
            print "exected:", str(expected_lst[idx]), str(expected[idx])
            print "computed:", f(test[idx])
            
    if failed == 0:
        print "inversion_and_sort: tests passed"
    else:
        print "inversion_and_sort: tests failed; review code"
    
test_inversion_and_sort()    
