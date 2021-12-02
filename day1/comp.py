import sys

d = [ int(line.rstrip()) for line in sys.stdin ]

print(sum([sum(d[i:i+3]) < sum(d[i+1:i+4]) for i in range(0, len(d)-3)]))
