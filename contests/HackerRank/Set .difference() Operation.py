# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
engSubscribed = set(input().split())

french = int(input())
frenchSubscribed = set(input().split())

engOnly = len(engSubscribed - frenchSubscribed)
print(engOnly)