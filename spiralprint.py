from sys import stdin

def spiralPrint(mat, nRows, mCols):
    rs=0
    ce=mCols-1
    re=nRows-1
    cs=0
    count=1
    while count<=mCols*nRows:
        for i in range(cs,ce+1):
            print(mat[rs][i],end=" ")
            count+=1
        rs+=1
        for i in range(rs,re+1):
            print(mat[i][ce],end=" ")
            count+=1
        ce-=1
        for i in range (ce,cs-1,-1):
            print(mat[re][i],end=" ")
            count+=1
        re-=1
        for i in range(re,rs-1,-1):
            print(mat[i][cs],end=" ")
            count+=1
        cs+=1




























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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1