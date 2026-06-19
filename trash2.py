def product(*args, **kwargs):
    final_list = []
    for arg in args:
        lst_of_numbers = []
        letters = list(set(arg))
        for letter in letters:
            lst_of_numbers.append(kwargs.get(letter, 1))
        temp_numb = 1
        for i in lst_of_numbers:
            temp_numb *= i
        if temp_numb != 1:
            final_list.append(temp_numb)

    return final_list
print(product("Ann", "Bob", "Chuck", a=9, n=5, u=3, c=2, A=5))
