from math import gcd
from re import compile, fullmatch

class Fraction():

    def __new__(self, num : int, den : int):
        if not (isinstance(num, int) and isinstance(den, int)): raise TypeError("Inputs must be integers.")
        if den == 0: raise ZeroDivisionError("Denominator cannot be zero.")
        if num % den == 0: return num // den # No needed Fraction, return a Intager
        return super(Fraction, self).__new__(self)

    def __init__(self, num : int, den : int) -> None:
        div = gcd(num, den)
        self.num , self.den = (num if den > 0 else -num) // div , abs(den // div)

    def __hash__(self): return hash((self.num, self.den))

    def __str__(self) -> str: return f'{self.num}/{self.den}'

    def __setattr__(self, name : str, value):
        if hasattr(self, name) or name not in ['num','den']:
            raise ValueError(f"cannot assign to field '{name}'")
        super(Fraction, self).__setattr__(name, value)

    def __neg__(self): return Fraction(-self.num , self.den)

    def inverse(self): return Fraction(self.den , self.num)

    def __add__(self, other):
        if isinstance(other, int): return Fraction(self.num + other * self.den , self.den)
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return Fraction(self.num*other.den+other.num*self.den , self.den*other.den)
        raise TypeError

    __radd__ = __add__

    def __sub__(self, other): return self.__add__(-other)

    def __rsub__(self, other): return -self.__radd__(-other)

    def __mul__(self, other):
        if isinstance(other, int): return Fraction(self.num * other, self.den)
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return Fraction(self.num * other.num , self.den * other.den)
        raise TypeError

    __rmul__ = __mul__

    def __truediv__(self , other):
        if isinstance(other, int): return Fraction(self.num , self.den * other)
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return Fraction(self.num * other.den , self.den * other.num)
        raise TypeError

    def __rtruediv__(self , other):
        if isinstance(other, int): return Fraction(self.den * other , self.num)
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        raise TypeError

    def __floordiv__(self, other):
        if isinstance(other, int): return int((self.num / self.den) // other)
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return int((self.num / self.den) // (other.num / other.den))
        raise TypeError

    def __mod__(self, other):
        if isinstance(other, int): return int((self.num / self.den) % other)
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return (self.num / self.den) % (other.num / other.den)
        raise TypeError

    def __pow__(self, other):
        if isinstance(other, int):
            if other >= 0: return Fraction(self.num ** other , self.den ** other)
            return Fraction(self.den ** -other , self.num ** -other)
        raise TypeError

    def __abs__(self): return self if self.num > 0 else Fraction(-self.num , self.den)

    def __lt__(self, other):
        if isinstance(other, int): return self.num < self.den * other
        if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction):return self.num * other.den < self.den * other.num
        raise TypeError

    def __le__(self, other):
        if isinstance(other, int): return self.num <= self.den * other
        if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return self.num * other.den <= self.den * other.num
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, float): other = Fraction.create_from_float(other)
        return (self.num , self.den) == (other.num , other.den) if isinstance(other, Fraction) else False

    def __ge__(self, other):
        if isinstance(other, int): return self.num >= self.den * other
        if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction):return self.num * other.den > self.den * other.num
        raise TypeError

    def __gt__(self, other):
        if isinstance(other, int): return self.num >= self.den * other
        if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction):return self.num * other.den > self.den * other.num
        raise TypeError

    def __ne__(self, other): return not self.__eq__(other)

    def __bool__(self) -> bool: return True

    @staticmethod
    def create_from_float(floatNum : float):
        if not isinstance(floatNum, float): raise TypeError("Input must be a float")
        # den = 1
        # while not floatNum.is_integer(): den , floatNum = 10 * den , 10 * floatNum
        # return Fraction(int(floatNum), den)
        return Fraction(int(floatNum * 10000000000000000), 10000000000000000)

    @staticmethod
    def create_from_string(string : str):
        if not isinstance(string, str): raise TypeError("Input must be a string")
        if fullmatch(compile(r'^\d+$'), string): return int(string)
        if fullmatch(compile(r'^\d+.$'), string): return int(string[:-1])
        if fullmatch(compile(r'^\d+.\d+$'), string):
            index_dot = string.find('.')
            string_len = len(string)
            return Fraction(int(string.replace('.','')), 10 ** (string_len - index_dot - 1))
        if fullmatch(compile(r'^\d+.\d*\(\d*\)$'), string):
            n1 = string.find('(') - string.find('.') - 1
            n2 = len(string) - string.find('(') - 2
            n3 = int(string.translate(str.maketrans('', '', '().')))
            n4 = int(string.replace('.','')[:string.find('(')-1])
            return Fraction(n3 - n4, int(f'{"9"*n2}{"0"*n1}'))
        raise TypeError

    def as_string_of_numbers(self, nPrec: int = 32) -> str:
        if not isinstance(nPrec , int): return TypeError
        l_s , rest= [f'{self.num // self.den}.'] , self.num % self.den
        rests_list , count = [] , 0
        while rest != 0 and count < nPrec:
            if rest in rests_list:
                index = len(l_s[0]) + rests_list.index(rest)
                return f"{''.join(l_s)[:index]}({''.join(l_s)[index:]})"
            rests_list.append(rest)
            rest *= 10
            l_s.append(str(rest // self.den))
            rest %= self.den
            count += 1
        return f'{''.join(l_s)}...' if rest != 0 else ''.join(l_s)

    # Metodi non testati !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def __float__(self) -> float: return self.num / self.den

    def __int__ (self) -> int: return int(self.__float__())
