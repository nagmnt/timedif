file = open('./data.txt','r')
INF = 99999999
# threshold. just tmp
t = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, INF]
counter = [0 for i in range(len(t))]

total = 0
number = 0
outliers = []
s = file.readline().replace('\n','')
while s != '':
    num = int(s)
    #print(num)
    for i in range(len(t)):
        if num < t[i]:
            counter[i] += 1
            break
    if num < t[0] or t[-2] <= num:
        outliers.append(num)
    s = file.readline().replace('\n','')
    total += num
    number += 1

print(counter)
print("number ", number)
print("average(all) ", total/number)

for i in range(len(counter)):
    counter[i] = counter[i] / number

print(counter)
number = number - len(outliers)
total = total - sum(outliers)
print("average ", total/number)