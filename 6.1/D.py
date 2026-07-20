import math
import sys

for row in sys.stdin:
    res = list(map(float, row.split()))
    print(pow(math.prod(res), 1 / len(res)))