'''

abba -> 'ab'

'''


import sys

def block_freq(s: str, start: int, k: int):
    f = [0] * 26
    end = start + k
    for i in range(start, end):
        f[ord(s[i]) - 97] += 1
    return tuple(f)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    p = data[1]

    # candidatos k: divisores de n com k <= n//2, em ordem crescente
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
        i += 1

    cand = sorted(k for k in divs if k <= n // 2)

    for k in cand:
        m = n // k
        base = block_freq(p, 0, k)

        ok = True
        for b in range(1, m):
            if block_freq(p, b * k, k) != base:
                ok = False
                break

        if ok:
            print(p[:k])
            return

    print("*")

if __name__ == "__main__":
    main()
