def to_string(*data, sep=' ', end='\n'):
    return sep.join(str(i) for i in data) + end