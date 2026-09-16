a = {}

n = int(input())# количество ребер
for i in range(1, n + 1):
    u, v, wt = map(int, input().split())
    if u not in a:
        a[u] = [[v, wt]]
    else:
        a[u].append([v, wt])
    if v not in a:
        a[v] = [[u, wt]]
    else:
        a[v].append([u, wt])
print(a)




'''
7
1 4 7
1 2 4
1 3 3
2 5 1
3 5 2
3 4 1
4 5 6
'''