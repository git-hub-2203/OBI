n = int(input(''))
A = []

for _ in range(n):
    x = int(input())
    if x == 0:
        A.pop()
    else:
        A.append(x)
print(sum(A))
