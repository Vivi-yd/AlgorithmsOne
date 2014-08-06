#Algorithms: Design and Analysis, Part I

##Introduction to Algorithms

####Moore's Law -:
1. A prediction made in 1965 by Intel co­‐founder Gordon Moore that the *density of transistors in integrated circuits would continue to double every 1 to 2 years*.

####Karatsuba Multiplication -:
1. The Karatsuba algorithm was the first multiplication algorithm *asymptotically faster than the quadratic "grade school" algorithm*.
2. It reduces the multiplication of two n-digit numbers to at most 3n^1.585^ single-digit multiplications.
3. Three multiplications in Karatsuba's basic step involve operands with fewer than n digits. These products can be computed by recursive calls of the Karatsuba algorithm.

###Basic Sorting Alogrithms
####Selection Sort
1. First it finds the smallest element in the array.
2. Exchange that smallest element with the element at the first position.
3. Then find the second smallest element and exchange that element with the element at the second position.
4. This process continues until the complete array is sorted.

####Bubble Sort
1. From the beginning of the list, compare every adjacent pair, swap their position if they are not in the right order.
2. After each iteration, one less element (the last one) is needed to be compared until there are no more elements left to be compared.

####Insertion Sort
1. Traverse the array. Initially, the whole array is treated unsorted.
2. Insert each element into the sorted part of the list where it belongs. This usually involves pushing down the larger elements in the sorted part.










