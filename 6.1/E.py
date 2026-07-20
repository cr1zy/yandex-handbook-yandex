import math

deca = list(map(float, input().split()))
poly = list(map(float, input().split()))
poly_in_deca = [poly[0] * math.cos(poly[1]), poly[0] * math.sin(poly[1])]

print(math.dist((deca[0], deca[1]) ,(poly_in_deca[0], poly_in_deca[1])))