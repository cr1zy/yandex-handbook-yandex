class Fraction:

    def __init__(self, numerator, denominator=None):
        if isinstance(numerator, str):
            self.num, self.denum = map(int, numerator.split('/'))
        else:
            self.num = numerator 
            self.denum = denominator
        self.__reduction()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.num, self.denum)
        self.num = self.num // gcd
        self.denum = self.denum // gcd
        return self

    def numerator(self, number=None):
        if number:
            self.num = number
            self.__reduction()
        return self.num 
    
    def denominator(self, number=None):
        if number:
            self.denum = number
            self.__reduction()
        return self.denum

    def __str__(self):
        return f'{self.num}/{self.denum}'
    
    def __repr__(self):
        return f'Fraction{self.num, self.denum}'