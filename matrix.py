def add_matrices(M1, M2):
    """
    input: M1 and M2 are matrics of same dimension
    output: matrix of the same dimension as M1 and M2
    assumption: M1 + M2 is defined
    
    returns matrix addition of the input matrices
    """
    #get row and col of input matrices
    row = len(M1)
    col = len(M1[0])
    
    ans = [[0 for j in range(col)] for i in range(row)]
    #set elements
    for i in range(row):
        for j in range(col):
            ans[i][j] = M1[i][j] + M2[i][j]

    return ans 

def subtract_matrices(M1, M2):
    """
    input: M1 and M2 are matrics of same dimension
    output: matrix of the same dimension as M1 and M2
    assumption: M1 + M2 is defined
    
    returns matrix subtraction of the input matrices;
    M1 - M2
    """
    #get row and col of input matrices
    row = len(M1)
    col = len(M1[0])
    
    ans = [[0 for j in range(col)] for i in range(row)]
    #set elements
    for i in range(row):
        for j in range(col):
            ans[i][j] = M1[i][j] - M2[i][j]

    return ans 

def product_matrices(M1, M2):
    """
    input: m1(matrix mxn) ; m2(matrix nxp)
    output: matrix (mxp)
    assumption: matrix multiplication of input matrices
    is defined
    
    returns matrix product of two input matrices using Gaussian 
    algorithm
    """
    #get m,n,p
    m = len(M1)
    n = len(M1[0]) #length of first element of the grid
    p = len(M2[0])
    #initialize ans list it should be mxp matrix
    ans = [[0 for j in range(p)] for i in range(m)]
    #now set values in the ans matrix
    for i in range(m):
        for j in range(p):
            #each element is obtained as scalar product in input matrices
            scal_product = 0
            for k in range(n):
                scal_product += M1[i][k] * M2[k][j]
            ans[i][j] = scal_product                
    
    return ans

def merge_matrices(A, B, C, D):
    """
    input: A, B, C, D are all matrices. 
    output: a matrix
    
    assumptions:
        1. A and B have equal number of rows
        2. C and D have equal number of rows
        3. A and C have equal number of columns
        4. B and D have equal number of columns
    
    returns a matrix [[A, B], [C, D]]
    """
    #get dimesion of the ans matrix
    row = len(A) + len(C)
    col = len(A[0]) + len(B[0])
    #get dimension of matrix A
    row_a = len(A)
    col_a = len(A[0])
    
    ans = [[0] * col] * row
    #set elements
    for i in range(row):
        present_row = []
        for j in range(col):
            if i < row_a and j < col_a:
                present_row.append(A[i][j])
            elif i < row_a and j>= col_a:
                present_row.append(B[i][j - col_a])
            elif i >= row_a and j < col_a:
                present_row.append(C[i-col_a][j])
            else:
                present_row.append(D[i-col_a][j-row_a])

        #add the row into the ans
        ans[i] = present_row

    return ans        

def split_list(L, n):
    """
    input: L is a list and n is an integer
    output: a tuple of two lists

    splits the list into two parts. First part is of length n
    """
    return L[:n], L[n:]

#print split_list([1,2,3,4,5,6], 3)

def split_matrix(X):
    """
    input: X is a matrix
    output: a list of four matrices
    
    returns a tuple of four matrices which form big matrix X
    """
    #get dimensions of X
    row = len(X)
    col = len(X[0])
    #get dimensions of top-left matrix
    row_a = row/2
    col_a = col/2
    #initialize sub-matrices
    A, B, C, D = [], [], [], []
    #set rows to sub-matrices
    for i in range(row):
        if i < row_a:
            A.append(X[i][:col_a])
            B.append(X[i][col_a:])
        else:
            C.append(X[i][:col_a])
            D.append(X[i][col_a:])

    print "A:", A
    print "B:", B
    print "C:", C
    print "D:", D

    return A, B, C, D    


m3 = [[1,2,3], [3,2,1], [2,1,3]] # 3 x 3
m4 = [[4,5,6], [6,5,4], [4,6,5]] # 3 x 3
m5 = [[101,102,103], [103,104,105], [105, 106, 107]] # 3 x 3
m6 = [[201,202,203], [204,205,206], [207,208,209]] # 3 x 3
m7 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

print split_matrix(m7)



