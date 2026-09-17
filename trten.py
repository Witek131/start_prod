

f = open('demo_23.txt').read().split('\n')
n = len(f)
m = len(f)
q = {}
dist = {}
for _ in range(m):
    u, v, wt = f[_].split()
    u = int(u)
    v = int(v)
    wt = float(wt)
    if u not in q:
        q[u] = [[v, wt]]
    else:
        q[u].append([v, wt])
    dist[u] = float('inf')
    dist[v] = float('inf')

    # if v not in q:
    #     q[v] = [[u, wt]]
    # else:
    #     q[v].append([u, wt])
    # ели граф не направленный
dist[1] = 0
start = 1
used = dict((_, False) for _ in dist)
mindist = 0
next = start
print(q)
while mindist < float('inf'):
    if next in q:
        for i in q[next]:
            to = i[0]
            wt = i[1]

            dist[to] = min(dist[to], dist[next] + wt)
    used[next] = True
    mindist = float('inf')
    for i in dist:
        if used[i] == False and dist[i] < mindist:
            mindist = dist[i]
            next = i
    if mindist == float('inf'):
        break
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
