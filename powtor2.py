# import docxtpl
#
# fail = docxtpl.DocxTemplate('decree_template.docx')
# a = input().split('/')
# d = {
#     'ruler': a[0], 'item': a[1], 'palace': a[2]
# }
# fail.render(d)
# fail.save('order.docx')

# from PIL import Image, ImageDraw
# import random
#
# im = Image.open('winter.png')
# x, y = im.size
# pic = im.load()
# d = []
# for i in range(x):
#     for j in range(y):
#         r, g, b = pic[i, j]
#         if r == g == b and 50 <= r <= 200:
#             d.append((i, j))
#
# random.shuffle(d)
# for i in range(int(len(d)*0.3)):
#     pic[d[i]] = (34,139,34)
# im.save('spring.png')
# import datetime
#
# date = datetime.datetime.strptime(input(), '%d.%m.%Y')
# with open('tumnus_diary.txt', encoding='utf-8') as f:
#     textc = f.read()
#     date1 = textc.split()[-1]
#     date1 = datetime.datetime.strptime(date1, '%d.%m.%Y')
# print('До встречи осталось', (date1 - date).days, 'дней')


# from PIL import Image, ImageDraw
#
# n = int(input())
# a = Image.new('RGB', (n, n), 'red')
# dr = ImageDraw.Draw(a)
# dr.circle((n // 2, n // 2), n // 3, 'yellow')
# dr.circle((n // 2, n // 2), n // 4, 'yellow', 'red', 10)
#
# a.save('emblema.png')

# import os
#
# d = []
# for dirpath, dirnames, filenames in os.walk("narnia_map"):
#     for i in filenames:
#         if i.split('.')[-1] == 'txt':
#             d.append(i)
# if len(d) == 0:
#     print("Карта ещё не создана!")
# else:
#     print(*sorted(d), sep='\n')
#     print('Всего файлов txt:', len(d))

# import random
#
# name = ['Питер', 'Сьюзен', 'Эдмунд', 'Люси', 'Юстэс', 'Джил']
# d = []
# r = 0
# n = int(input())
# while r < n:
#    x = random.sample(name, k = 4)
#    if set(x) not in d:
#        print(*x, sep = ', ')
#        d.append(set(x))
#        r+=1
