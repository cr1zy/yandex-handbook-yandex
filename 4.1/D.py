def take_small(money):
    result = [i for i in money if i < 100]
    return(result)
print(take_small([0.01, 0.01, 500, 2000, 5000, 0.05, 1, 200, 0.1, 2000, 1000, 10, 25, 0.05, 10, 2000, 500, 5000, 0.01, 200, 2, 1000, 0.5, 5000, 10, 0.5, 5, 1]))