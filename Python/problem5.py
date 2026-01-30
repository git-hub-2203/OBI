s = int(input())
a = int(input())
b = int(input())
f = []
qtd = 0

for i in range(a, b+1):
    i = str(i)
    for j in i:
        j = int(j)
        f.append(j)
    if sum(f) == s:
        qtd+=1
    f.clear()

print(qtd)