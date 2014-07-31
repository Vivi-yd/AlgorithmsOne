from random import randrange

def quicksort(L):
    """
    implementation of quick sort algorithm (randomized)
    this is in-place partition 
    """
    #base case
    if len(L) < 2:
        return L 
    else:
        #pick a random pivot        
        l = randrange(len(L))
        pivot = L[l]
        #swap pivot with the first element
        L[l], L[0] = L[0], L[l]
        #index as boundary between sorted and unsorted part
        i = 1
        # j measures what part has already been scanned
        for j in range(i, len(L)):
            #elements less than pivot are pushed to its left
            if L[j] < pivot:
                L[j] , L[i] = L[i], L[j]
                i += 1
    #pivot element is place at the correct position                
    L[0], L[i-1] = L[i-1], L[0]
    
    #recursion on part left and right of pivot
    return quicksort(L[:i-1]) + [pivot] + quicksort(L[i:])

print quicksort([3,8,2,5,1,4,7,6,8,3,8,1,5])
