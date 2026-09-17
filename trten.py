from logging import INFO


f = open('demo_23.txt').read().split('\n')
n = len(f)
m = len(f)
q = {}
for _ in range(m):
    print(f[_])
    u, v, wt = f[_].split()
    u = int(u)
    v = int(v)
    wt = float(wt)
    if u not in q:
        q[u] = [[v, wt]]
    else:
        q[u].append([v, wt])
    # if v not in q:
    #     q[v] = [[u, wt]]
    # else:
    #     q[v].append([u, wt])
    # ели граф не направленный

start = 1
used = [False for _ in range(0, m + 1)]
dist = [[i, float('inf')] for i in range(0, 1001)]
dist[start][1] = 0
print(dist)
mindist = 0
next = start
while mindist < float('inf'):

    for i in q[next]:
        to = i[0]
        wt = i[1]
        dist[to][1] = min(dist[to][1], dist[next][1] + wt)
    used[next] = True
    mindist = float('inf')
    for i in range(0, n):
        print(dist, i, mindist, i)
        if used[i] == False and dist[i][1] < mindist:
            mindist = dist[i][1]
            next = i
    # print(mindist)

print(dist[100])

'''
7
1 4 7
1 2 4
1 3 3
2 5 1
3 5 2
3 4 1
4 5 6
5
7
1 2 4 
1 4 7
1 3 4
2 5 11
3 5 2
3 4 1
4 5 6
'''
