from itertools import permutations

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(permutations(a, m))
b = list(set(b))
b.sort()
for x in b:
    print(*x)