m1 = [[1,2,3], [4,5,6]]
m2 = [[1,2], [3,4], [5,6]]
m3 = [[1,2,3], [3,2,1], [2,1,3]]
m4 = [[4,5,6], [6,5,4], [4,6,5]]
m5 = [[101,102,103], [103,104,105], [105, 106, 107]]
m6 = [[201,202,203], [204,205,206], [207,208,209]]

def mat_add(M1, M2):
    """
    input: M1 and M2 are matrics of same dimension
    output: matrix of the same dimension as M1 and M2
    assumption: M1 + M2 is defined
    
    returns matrix addition of the input matrices
    """
    #get row and col of input matrices
    row = len(M1)
    col = len(M1[0])
    
    ans = [[0] * col] * row
    #set elements
    for i in range(row):
        present_row = []
        for j in range(col):
            present_row.append(M1[i][j] + M2[i][j])
        #set the rows one by one
        ans[i] = present_row

    return ans 

def mat_sub(M1, M2):
    """
    input: M1 and M2 are matrics of same dimension
    output: matrix of the same dimension as M1 and M2
    assumption: M1 + M2 is defined
    
    returns matrix subtraction of the input matrices
    """
    #get row and col of input matrices
    row = len(M1)
    col = len(M1[0])
    
    ans = [[0] * col] * row
    #set elements
    for i in range(row):
        present_row = []
        for j in range(col):
            present_row.append(M1[i][j] - M2[i][j])
        #set the rows one by one
        ans[i] = present_row

    return ans 

def mat_merge(A, B, C, D):
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
            if i < row_a and j < row_a:
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
                
print mat_merge(m3, m4, m5, m6)                                       
                
                
    

def mat_mul(M1, M2):
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
    ans = [[0]* p] * m
    #now set values in the ans matrix
    for i in range(m):
        #list to hold values for scalar product in each row
        row = []
        for j in range(p):
            #each element is obtained as scalar product in input matrices
            scal_product = 0
            for k in range(n):
                scal_product += M1[i][k] * M2[k][j]
            #append to the row
            row.append(scal_product)
        
        #set the row in ans list to be equal to this row
        ans[i] = row
    
    return ans


def test_matrix_multiply(f):
    expected = [[[22, 28], [49, 64]], [[28, 33, 29], [28, 31, 31], [26, 33, 31]]]
    if f(m1, m2) == expected[0] and f(m3,m4) == expected[1]:
        print str(f), ": tests passed"
    else:
        print str(f), ": tests failed; review code"

test_matrix_multiply(mat_mul)

def mat_strass(M1, M2):
    """
    input: m1(matrix mxn) ; m2(matrix nxp)
    output: matrix (mxp)
    assumption: matrix multiplication of input matrices
    is defined
    
    returns matrix product of two input matrices using Strassen's
    algorithm
    """
    if len(M1) <=2 and len(M2) <= 2:
        return mat_mul(M1, M2)
    else:
        #get A,B,C,D and E,F,G,H

