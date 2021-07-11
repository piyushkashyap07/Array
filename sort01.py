from sys import stdin

def sortZeroesAndOne(arr, n) :
    i=0
    j=n-1
    while j>i:
        if arr[i]==0:
            i=i+1
        elif arr[i]==1:
            if arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                i=i+1
                j=j-1
            else:
                j=j-1



















#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1