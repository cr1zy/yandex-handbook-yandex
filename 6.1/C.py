import math
import sys

for row in sys.stdin:
    res = list(map(int, row.split()))
    all = math.comb(res[0], res[1])
    vac = math.comb(res[0] - 1, res[1] - 1)
    print(f"{vac} {all}")