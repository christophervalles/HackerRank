n, t = map(int, raw_input().split())
widths = map(int, raw_input().split())

for c in range(0, t):
    start, end = map(int, raw_input().split())

    print min(widths[start:end + 1])