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


def selection_sort(L):
    """
    implementation of selection sort algorithm
    """
    for i in range(len(L)):

        #find the smallest element in the unsorted part
        smallest_index = i
        for j in range(i+1, len(L)):
            if L[smallest_index] > L[j]:
                smallest_index = j

        #swap smallest element with the first element in the
        #unsorted part
        L[i], L[smallest_index] = L[smallest_index], L[i]
    
    return L

def bubble_sort(L):
    """
    implementation of bubble sort algorithm
    """
    end = len(L)
    while end > 0:
        for i in range(end-1):
            #if element on right is less than one on the left
            if L[i] > L[i+1]:
                #swap the elements
                L[i], L[i+1] = L[i+1], L[i]
        
        end -= 1

    return L        
    

def insertion_sort(L):
    """
    implementation of insertion sort algorithm
    """
    for i in range(1, len(L)):
        #consider part of the list upto the element
        for j in range(i, 0, -1):
            if L[j] < L[j-1]:
                #swap the elements if left element is greater
                L[j-1], L[j] = L[j], L[j-1]

            else:
                break
                
            
    return L                 


def test_sorting():
    """
    test for sorting methods using randomly created list
    """
    functions = [selection_sort, bubble_sort, insertion_sort]
    for f in functions:
        failed = 0
        #testing for 100 random cases
        for i in range(100):
            #select list length randomly
            length = randrange(1, 21)
            #create list with random numbers
            lst = [randrange(1, 10) for i in range(length)]
            #lists created by algorithm and python internal implementation
            lst1 = f(lst)
            if not(is_sorted(lst1)):
                failed += 1
                print "test failed for:" , lst
                print "computed:", lst1
    
        if failed == 0:
            print "test passed for" , str(f)

test_sorting()    
