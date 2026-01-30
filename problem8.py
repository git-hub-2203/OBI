import sys
from collections import defaultdict, deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))

    grid = [[None]*C for _ in range(L)]
    row_sum = [0]*L

    # Ler linhas: C variáveis + soma
    for i in range(L):
        for j in range(C):
            grid[i][j] = next(it)
        row_sum[i] = int(next(it))

    col_sum = [int(next(it)) for _ in range(C)]

    # Mapear variáveis para ids (para ordenar e armazenar valores)
    var_names = set()
    for i in range(L):
        for j in range(C):
            var_names.add(grid[i][j])
    var_list = sorted(var_names)  # ordem pedida: aa, ab, ..., zz
    vid = {name: idx for idx, name in enumerate(var_list)}
    nvars = len(var_list)

    # Equações: 0..L-1 são linhas, L..L+C-1 são colunas
    neq = L + C
    coef = [defaultdict(int) for _ in range(neq)]
    rhs = [0]*neq

    # Montar coeficientes das linhas
    for i in range(L):
        rhs[i] = row_sum[i]
        d = coef[i]
        for j in range(C):
            d[vid[grid[i][j]]] += 1

    # Montar coeficientes das colunas
    for j in range(C):
        eq = L + j
        rhs[eq] = col_sum[j]
        d = coef[eq]
        for i in range(L):
            d[vid[grid[i][j]]] += 1

    # Adjacência: para cada variável, quais equações ela aparece
    adj = [[] for _ in range(nvars)]
    for e in range(neq):
        for v, k in coef[e].items():
            adj[v].append(e)

    # unk = quantas variáveis ainda não resolvidas em cada equação
    unk = [len(coef[e]) for e in range(neq)]

    val = [None]*nvars
    q = deque()

    for e in range(neq):
        if unk[e] == 1:
            q.append(e)

    solved_count = 0

    while q:
        e = q.popleft()
        if unk[e] != 1:
            continue  # pode ter mudado

        # Pegar a única variável restante
        (v, k), = coef[e].items()
        # Se já foi resolvida por outra equação, esse e deve virar 0 unk após updates;
        # mas por segurança:
        if val[v] is not None:
            continue

        # Calcular valor
        # Garantido divisível e solução única
        x = rhs[e] // k
        val[v] = x
        solved_count += 1

        # Atualizar todas as equações que contêm v
        for ee in adj[v]:
            if v in coef[ee]:
                kk = coef[ee][v]
                rhs[ee] -= kk * x
                del coef[ee][v]
                unk[ee] -= 1
                if unk[ee] == 1:
                    q.append(ee)

        if solved_count == nvars:
            break

    # Imprimir em ordem alfabética
    out = []
    for name in var_list:
        v = vid[name]
        out.append(f"{name} {val[v]}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
