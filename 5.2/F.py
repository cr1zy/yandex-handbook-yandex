class Fraction:

    def __init__(self, numerator, denominator=None):
        if isinstance(numerator, str):
            self.num, self.denum = map(int, numerator.split('/'))
        else:
            self.num = numerator 
            self.denum = denominator
        self.__reduction()

    def __sing(self):
        return -1 if self.num < 0 else 1

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.num, self.denum)
        self.num = self.num // gcd
        self.denum = self.denum // gcd

        if self.denum < 0:
            self.num = -self.num 
            self.denum = -self.denum
        return self

    def numerator(self, number=None):
        if number is not None:
            self.num = number * self.__sing()
            self.__reduction()
        return abs(self.num) 
    
    def denominator(self, number=None):
        if number is not None:
            self.denum = number
            self.__reduction()
        return abs(self.denum)

    def __str__(self):
        return f'{self.num}/{self.denum}'
    
    def __repr__(self):
        return f"Fraction('{self.num}/{self.denum}')"
    
    def __neg__(self):
        return Fraction(-self.num, self.denum)
    
    def __add__(self, other):
        gcd = self.__gcd(self.denum, other.denum)
        lcm = abs(self.denum * other.denum) // gcd  # left_denum, right_denum 
        left_num = (lcm // self.denum) * self.num
        right_num = (lcm // other.denum) * other.num
        return Fraction(left_num + right_num, lcm)
    
    def __sub__(self, other):
        gcd = self.__gcd(self.denum, other.denum)
        lcm = abs(self.denum * other.denum) // gcd  # left_denum, right_denum 
        left_num = (lcm // self.denum) * self.num
        right_num = (lcm // other.denum) * other.num
        return Fraction(left_num - right_num, lcm)
    
    def __iadd__(self, other):
        gcd = self.__gcd(self.denum, other.denum)
        lcm = abs(self.denum * other.denum) // gcd  # left_denum, right_denum 
        left_num = (lcm // self.denum) * self.num
        right_num = (lcm // other.denum) * other.num
        self.num = left_num + right_num
        self.denum = lcm
        self.__reduction()
        return self

    def __isub__(self, other):
        gcd = self.__gcd(self.denum, other.denum)
        lcm = abs(self.denum * other.denum) // gcd  # left_denum, right_denum 
        left_num = (lcm // self.denum) * self.num
        right_num = (lcm // other.denum) * other.num
        self.num = left_num - right_num
        self.denum = lcm
        self.__reduction()
        return self