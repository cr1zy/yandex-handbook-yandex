from itertools import combinations
def choose_best_sum(t, k, ls):
    if len(ls) == 0:
        return(None)
    value = sorted(sum(i) for i in list(combinations(ls, k)) if sum(i) <= t)
    if value != []:
        return(value[-1])
    else:
        return(None)
print(choose_best_sum(100, 2, []))