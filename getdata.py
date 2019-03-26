import re

file = open('/root/.bitcoin/testnet3/debug.log','r')
# e.g. 2019-02-18T09:31:10Z date='2012-05-25T17:14:55Z'

def iso_to_sec(s1, s2):
    # s1 is a local time(real time)
    # s2 is a miner's network time(strictly, it is a timestamp of a block)
    s1 = [s1[:10], s1[11:-1]]
    s2 = [s2[6:16], s2[17:-2]]
    if s1[0] != s2[0]:
        return False
    
    s1 = s1[1].split(":")
    s1 = list(map(int, s1))
    s2 = s2[1].split(":")
    s2 = list(map(int, s2))

    time1 = s1[0]*60*60 + s1[1]*60 + s1[2]
    time2 = s2[0]*60*60 + s2[1]*60 + s2[2]
    return time2 - time1

for i in range(1484170):
    line = file.readline()

# height=1480000 is line:1484171
height = 1480000 - 1
while height < 1486000:
    line = file.readline().split()
    if len(line) >= 9:
        if line[4][:6] == "height":
            if int(line[4][7:]) == height + 1:
                dif = iso_to_sec(line[0], line[8])
                height = height + 1
                print(dif)