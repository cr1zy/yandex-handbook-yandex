def make_matrix(size, arg=0):
    if type(size) == tuple:
        m, n = size
    else:
        m = n = size
    lst = [[arg for i in range(m)] for i in range(n)]
    return lst
print(make_matrix((4, 2), 1))