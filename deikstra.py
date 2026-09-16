from logging import INFO

n = int(input())
m = int(input())
q = {}
for  _ in range(n+1):
    u , v, wt= map(int, input().split())
    if u not in q:
        q[u] = [v, wt]
    else:
        q[u]
    # ели граф не направленный

used = [False for _ in range(n + 1)]
dist = [(i, float('inf')) for i in range(n + 1)]
dist[0] = 0
mindist = 0
next = 0
while True:
     pass