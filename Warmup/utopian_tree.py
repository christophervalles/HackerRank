# Cycle Height Formula
# 0     1      2^1-1
# 1     2      2^2-2
# 2     3      2^2-1
# 3     6      2^3-2
# 4     7      2^3-1
# 5     14     2^4-2
# 6     15     2^4-1
# 7     30     2^5-2
# 8     31     2^5-1
# 9     62     2^((9+1)/2+1)-2 <-- Expanded based on cycle number
# 10    63     2^(10/2+1)-1 <-- Expanded based on cycle number

# Final Formula
# 2 ^ ((cycle + cycle % 2) / 2 + 1)) - (1 + cycle % 2)


from sys import stdin
n = int(stdin.readline())

for i in range(0, int(n)):
    cycles = int(stdin.readline())
    print pow(2, ((cycles + cycles % 2) / 2 + 1)) - (1 + cycles % 2)