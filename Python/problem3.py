from collections import defaultdict

n = int(input().strip())

total = defaultdict(int)       # soma dos tempos de resposta por amigo
recebida_em = {}               # amigo -> tempo em que a última msg foi recebida e ainda não respondida
amigos = set()

tempo_atual = 0
gap = 1
primeiro_evento = True

for _ in range(n):
    tipo, x_str = input().split()
    x = int(x_str)

    if tipo == 'T':
        gap = x
        continue

    # tipo é R ou E: é evento
    if primeiro_evento:
        primeiro_evento = False
    else:
        tempo_atual += gap

    gap = 1  # volta ao padrão após usar o gap

    if tipo == 'R':
        amigos.add(x)
        recebida_em[x] = tempo_atual
    else:  # 'E'
        amigos.add(x)
        total[x] += tempo_atual - recebida_em[x]
        del recebida_em[x]

for a in sorted(amigos):
    if a in recebida_em:
        print(a, -1)
    else:
        print(a, total[a])
