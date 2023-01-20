f = open('Perepis.txt', 'r')
d1 = int(input())
d2 = int(input())
n = 0
surname = []
for i in f:
    mark = i.split()
    year = mark[3].split('.')
    if int(year[2]) >=d1 and int(year[2])<=d2:
        print(mark[:3])



