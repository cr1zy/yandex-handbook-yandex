from itertools import combinations
def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in list(combinations(ls, k)) if sum(i) <= t)
    except:
        return None
print(choose_best_sum(100, 2, []))

