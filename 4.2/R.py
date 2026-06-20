def lmbd(tple):
    for letter in tple[1]:
        if letter.isalpha():
            letter.lower()

lambda tple: (''.join(letter for letter in tple[0].lower() if letter.isalpha()), 
              sum(tple[1]) if isinstance(tple[1], (tuple, list)) else tple[1])
