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

def test_inversion_brute():
    """
    test method for inversion_brute
    """
    failed = 0
    
    test = [[], [1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1],
            [1, 3, 5, 2, 4, 6]]
    expected = [0, 0, 0, 15, 3]
    
    for idx in range(len(test)):
        #test for each list one by one
        if inversion_brute(test[idx]) != expected[idx]:
            failed += 1
            print "test failed for:" , test[idx]
            print "computed:", inversion_brute(test[idx])
            print "expected:", expected[idx]
            print "---------------------------"

    if failed == 0:
        print "inversion_brute: tests passed"
    else:
        print "inversion_brute: tests failed; review code"

test_inversion_brute()        
