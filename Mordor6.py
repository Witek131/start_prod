import json
with open('rings.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
data1 = []
for i in data:
    data1.append(i.split())

v = max(data1, key=lambda x: int(x[-1]))
if (len(v[0]) + len(v[1]) + len(v[2]) + int(v[3])) % 2 == 0:
    s = 'visible'
else:
    s = 'invisible'

d = {'title': v[0], 'material': v[1], 'keeper': v[2], 'power': v[3], 'visibility': s}
with open('powerful.json', 'w', encoding='utf-8' ) as file:
    json.dump(d, file)

