l = int(raw_input())
r = int(raw_input())

print int(str(bin(l ^ r)[2:]).replace('0','1'), 2)