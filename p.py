f = open('Perepis.txt', 'r')
d1 = int(input())
d2 = int(input())
n = 0
surname = []
for i in f:
    mark = i.split()
    year = mark[3].split('.')
    if int(year[2])<1978:
        n+=1
        surname.append(mark[0])
print(surname)
print(n)
