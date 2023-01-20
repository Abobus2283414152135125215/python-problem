f = open('travels.txt', 'r')
day = ''
sum_weight = 0
value = 0
max_sum = 0
max_day = 0
mas_lipki = 0
sum_distance = 0
n = 0
names_from = {'Сосново':0,'Липки':0,'Орехово':0,'Осинки':0,'Березки':0,'Буково':0,'Дубки':0,'Вязово':0}
names_to = {'Сосново':0,'Липки':0,'Орехово':0,'Осинки':0,'Березки':0,'Буково':0,'Дубки':0,'Вязово':0}
max_gazeline = 0
name_gazeline = []
for i in f:
    mark = i.split()
    #1
    if int(mark[0]) > value:
        if sum_weight >= max_sum:
            max_sum = sum_weight
            max_day = int(mark[0])-1
        value = int(mark[0])
        sum_weight = 0

    if int(mark[0]) == value:
        sum_weight += int(mark[6])
    #2

    if mark[2] == 'Липки':
        mas_lipki += int(mark[6])

    #3

    if mark[0] == '1':
        sum_distance += int(mark[4])

    #4

    if mark[2] in names_to:
        names_from[mark[2]] += int(mark[6])
    #5
    if mark[3] in names_to:
        names_to[mark[3]] += int(mark[6])
    #6
    if int(mark[5]) > max_gazeline:
        max_gazeline = int(mark[5])
        name_gazeline.clear()
        name_gazeline.append( mark[3])
    if int(mark[5])==max_gazeline:
        name_gazeline.append(mark[3])



print(max_day,'октября')
print(max_sum)

print(mas_lipki)

print(sum_distance)

print(names_from)

print(names_to)

print(name_gazeline)
print(max_gazeline)

