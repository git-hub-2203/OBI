n = input()
a, b = n.split(' ')
a = int(a)
b = int(b)
x = min(a, b)
y = max(a, b)
c = 2*x - y

print(c)