import math

t = int(raw_input())

for l in range(0, t):
    s = raw_input()

    v1 = s[0:int(math.floor(float(len(s))/2))]
    v2 = s[int(math.ceil(float(len(s))/2)):][::-1]

    print sum([abs(ord(v1[x]) - ord(v2[x])) for x in range(0, len(v1))])