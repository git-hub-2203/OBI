import sys

def min_contractions_to_palindrome(a):
    n = len(a)
    i, j = 0, n - 1
    ops = 0

    left = a[i]
    right = a[j]

    while i < j:
        if left == right:
            i += 1
            j -= 1
            if i < j:
                left = a[i]
                right = a[j]
        elif left < right:
            # contrai do lado esquerdo: soma com o próximo
            i += 1
            left += a[i]
            ops += 1
        else:
            # contrai do lado direito: soma com o anterior
            j -= 1
            right += a[j]
            ops += 1

    return ops

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    print(min_contractions_to_palindrome(a))

if __name__ == "__main__":
    main()
