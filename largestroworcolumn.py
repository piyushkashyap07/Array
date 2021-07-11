from sys import stdin

def findLargest(arr, nRows, mCols):
    sumCol, indexCol = funcCol(arr, nRows, mCols)
    sumRow, indexRow = funcRow(arr, nRows, mCols)
    
    if(sumCol == -1 and sumRow == -1):
        print("row 0 -2147483648")
    elif(sumCol > sumRow):
        print("column", end=" ")
        print(indexCol, end=" ")
        print(sumCol)
    else:
        print("row", end=" ")
        print(indexRow, end=" ")
        print(sumRow)

def funcCol(arr, nRows, mCols):
    max_sum=-1
    max_col_index=-1
    for j in range(mCols):
        sum=0
        for i in range (nRows):
            sum+=arr[i][j]
            if sum > max_sum:
                max_col_index=j
                max_sum = sum
    return max_sum, max_col_index
def funcRow(arr, nRows, mCols):
    max_sum=-1
    max_row_index=-1
    for i in range(nRows):
        sum=0
        for j in range (mCols):
            sum+=arr[i][j]
            if sum>max_sum:
                max_row_index=i
                max_sum = sum
    return max_sum, max_row_index


























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1