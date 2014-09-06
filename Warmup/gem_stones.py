# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

n = int(stdin.readline())
components = set(stdin.readline().rstrip())

for i in range(1, int(n)):
    components = components & set(stdin.readline().rstrip())

print len(components)