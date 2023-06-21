import math

MAX = 9999.99

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pontos = []

def minimum(p1, p2):
    if p1 < p2:
        return p1
    return p2

def distance(p1, p2):
    dist = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return dist

def closestPair(p1, p2):
    if p1 == p2:
        return MAX + 1.0
    elif p2 - p1 == 1:
        return distance(pontos[p2], pontos[p1])
    else:
        esq = closestPair(p1, (p1 + p2) // 2)
        dir = closestPair((p1 + p2) // 2 + 1, p2)
        dist = minimum(esq, dir)
        meio = (p1 + p2) // 2
        mediana = pontos[meio].x

        k = (p1 + p2) // 2 + 1
        while k <= p2 and mediana - pontos[k].x < dist:
            esq = distance(pontos[k], pontos[meio])
            dist = minimum(dist, esq)
            k += 1

        meio -= 1
        while meio >= p1 and mediana - pontos[meio].x < dist:
            k = (p1 + p2) // 2 + 1
            while k <= p2 and mediana - pontos[k].x < dist:
                esq = distance(pontos[k], pontos[meio])
                dist = minimum(dist, esq)
                k += 1
            meio -= 1

        return dist

def compare(p1, p2):
    if p1.x > p2.x:
        return 1
    elif p1.x < p2.x:
        return -1
    else:
        if p1.y > p2.y:
            return 1
        else:
            return -1

while True:
    N = int(input())
    if N == 0:
        break

    pontos = []
    for _ in range(N):
        x, y = map(float, input().split())
        pontos.append(Ponto(x, y))

    pontos.sort(key=lambda ponto: (ponto.x, ponto.y))

    dist = closestPair(0, N - 1)

    if dist > MAX:
        print("INFINITY")
    else:
        print("{:.4f}".format(dist))
