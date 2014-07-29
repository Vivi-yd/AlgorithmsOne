"""
Implementation of basic matrix operation in python. Matrix product is implemented
using both Gaussian and Strassen's Algorithm. 

The Strassen's code works only for matrices of even size. That can be resolved by converting 
odd size matrix into even size which can be done easily and it is what we call "Gadha Mazdoori" in which I am 
not interested :P 
"""
def add_matrices(M1, M2):
    """
    input: M1 and M2 are matrics of same dimension
    output: matrix of the same dimension as M1 and M2
    
    assumption: M1 + M2 is defined
    
    returns matrix addition of the input matrices (M1 + M2)
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
    
    assumption: M1 - M2 is defined
    
    returns matrix subtraction of the input matrices (M1 - M2)
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

    return A, B, C, D    

def product_strassen(X, Y):
    """
    input: X(matrix mxn) ; Y(matrix nxp)
    output: matrix (mxp)
    
    assumption: matrix multiplication of input matrices
    is defined. 
    
    ** X and Y are matrices of even and equal dimensions.
    
    returns matrix product of two input matrices using Gaussian 
    algorithm
    """
    if len(X) and len(Y) <= 2:
        return product_matrices(X, Y)
    else:
        #get components of input matrices
        A, B, C, D = split_matrix(X)
        E, F, G, H = split_matrix(Y)
        
        #get seven products
        p1 = product_strassen(A, subtract_matrices(F, H))
        p2 = product_strassen(add_matrices(A,B), H)
        p3 = product_strassen(add_matrices(C,D), E)
        p4 = product_strassen(D, subtract_matrices(G,E))
        p5 = product_strassen(add_matrices(A,D),add_matrices(E,H))
        p6 = product_strassen(subtract_matrices(B,D),add_matrices(G,H))
        p7 = product_strassen(subtract_matrices(A,C),add_matrices(E,F))
        
        #get four submatrices of input matrix
        x1 = add_matrices(p5,p4)
        x2 = add_matrices(x1, p6)
        S1 = subtract_matrices(x2, p2) #first sub-matrix ; p4+p5+p6-p2
        S2 = add_matrices(p1,p2) #second element
        S3 = add_matrices(p3,p4) #third element
        y1 = add_matrices(p1,p5)
        y2 = subtract_matrices(y1, p3)
        S4 = subtract_matrices(y2, p7)
        
        return merge_matrices(S1, S2, S3, S4)
        
        
    


m3 = [[1,2,3], [3,2,1], [2,1,3]] # 3 x 3
m4 = [[4,5,6], [6,5,4], [4,6,5]] # 3 x 3
m5 = [[101,102,103], [103,104,105], [105, 106, 107]] # 3 x 3
m6 = [[201,202,203], [204,205,206], [207,208,209]] # 3 x 3
m7 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]] # 4 x 4
m8 = [[11,12,13,14], [15,16,17,18], [19,110,111,112], [113,114,115,116]]

print product_matrices(m7, m8)
print product_strassen(m7, m8)

