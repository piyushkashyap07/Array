## Read input as specified in the question.
## Print output as specified in the question.
# n=int(input())
# l=[]
# for i in range(n):
#     l.append(int(input()))
# sum1=sum(l)
# print(sum)

n = int(input())
l=[int(x) for x in input().split()]
print(sum(l))