from math import gcd
from re import fullmatch
# from sys import set_int_max_str_digits

class Fraction():

    def __new__(self, num: int, den: int):
        if not (isinstance(num, int) and isinstance(den, int)): raise TypeError("Inputs must be integers.")
        if den == 0: raise ZeroDivisionError("Denominator cannot be zero.")
        if num % den == 0: return num // den # No needed Fraction, return a Intager
        return super(Fraction, self).__new__(self)

    def __init__(self, num: int, den: int) -> None:
        div = gcd(num, den)
        self.num , self.den = (num if den > 0 else -num) // div , abs(den // div)

    def __hash__(self): return hash((self.num, self.den))

    def __str__(self) -> str: return f'{self.num}/{self.den}'

    def __repr__(self) -> str: return f'Fraction object: {self.num}/{self.den} = {self.as_string_of_numbers(100)}'

    def __setattr__(self, name: str, value):
        if hasattr(self, name) or name not in ['num','den']:
            if name not in ['num','den']: raise AttributeError(f"'Fraction' object has no attribute '{name}'")
            raise AttributeError(f"attribute '{name}' of 'Fraction' objects is not writable")
        super(Fraction, self).__setattr__(name, value)

    def __delattr__(self, name):
        if hasattr(self, name): raise AttributeError(f"attribute '{name}' of 'Fraction' objects is not writable")
        raise AttributeError(f"'Fraction' object has no attribute '{name}'")

    def __neg__(self): return Fraction(-self.num , self.den)

    def inverse(self): return Fraction(self.den , self.num)

    def __add__(self, other):
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return Fraction(self.num*other.den+other.num*self.den , self.den*other.den)
        if isinstance(other, int): return Fraction(self.num + other * self.den , self.den)
        raise TypeError(f"unsupported operand type(s) for + and -: 'Fraction' and '{other.__class__.__name__}'")

    __radd__ = __add__

    def __sub__(self, other): return self.__add__(-other)

    def __rsub__(self, other): return -self.__add__(-other)

    def __mul__(self, other):
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return Fraction(self.num * other.num , self.den * other.den)
        if isinstance(other, int): return Fraction(self.num * other, self.den)
        raise TypeError(f"unsupported operand type(s) for *: 'Fraction' and '{other.__class__.__name__}'")

    __rmul__ = __mul__

    def __truediv__(self , other):
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return Fraction(self.num * other.den , self.den * other.num)
        if isinstance(other, int): return Fraction(self.num , self.den * other)
        raise TypeError(f"unsupported operand type(s) for /: 'Fraction' and '{other.__class__.__name__}'")

    def __rtruediv__(self , other):
        if isinstance(other, int): return Fraction(self.den * other , self.num)
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        raise TypeError(f"unsupported operand type(s) for /: 'Fraction' and '{other.__class__.__name__}'")

    def __floordiv__(self, other):
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return int((self.num / self.den) // (other.num / other.den))
        if isinstance(other, int): return int((self.num / self.den) // other)
        raise TypeError(f"unsupported operand type(s) for //: 'Fraction' and '{other.__class__.__name__}'")

    def __mod__(self, other):
        # if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return (self.num / self.den) % (other.num / other.den)
        if isinstance(other, int): return int((self.num / self.den) % other)
        raise TypeError(f"unsupported operand type(s) for %: 'Fraction' and '{other.__class__.__name__}'")

    def __pow__(self, other):
        if isinstance(other, int):
            if other >= 0: return Fraction(self.num ** other , self.den ** other)
            return Fraction(self.den ** -other , self.num ** -other)
        raise TypeError(f"unsupported operand type(s) for **: 'Fraction' and '{other.__class__.__name__}'")

    def __abs__(self): return self if self.num > 0 else Fraction(-self.num , self.den)

    def __lt__(self, other):
        if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction):return self.num * other.den < self.den * other.num
        if isinstance(other, int): return self.num < self.den * other
        raise TypeError(f"'<' not supported between instances of 'Fraction' and '{other.__class__.__name__}'")

    def __le__(self, other):
        if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction): return self.num * other.den <= self.den * other.num
        if isinstance(other, int): return self.num <= self.den * other
        raise TypeError(f"'<=' not supported between instances of 'Fraction' and '{other.__class__.__name__}'")

    def __eq__(self, other):
        if isinstance(other, float): other = Fraction.create_from_float(other)
        return (self.num , self.den) == (other.num , other.den) if isinstance(other, Fraction) else False

    def __ge__(self, other):
        if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction):return self.num * other.den > self.den * other.num
        if isinstance(other, int): return self.num >= self.den * other
        raise TypeError(f"'>=' not supported between instances of 'Fraction' and '{other.__class__.__name__}'")

    def __gt__(self, other):
        if isinstance(other, float): other = Fraction.create_from_float(other)
        if isinstance(other, Fraction):return self.num * other.den > self.den * other.num
        if isinstance(other, int): return self.num >= self.den * other
        raise TypeError(f"'>' not supported between instances of 'Fraction' and '{other.__class__.__name__}'")

    def __ne__(self, other): return not self.__eq__(other)

    def __bool__(self) -> bool: return True

    @staticmethod
    def create_from_float(floatNum: float):
        if not isinstance(floatNum, float): raise TypeError("Input must be a float")
        return Fraction(int(floatNum * 10000000000000000), 10000000000000000)
        # den = 1
        # while not floatNum.is_integer(): den , floatNum = 10 * den , 10 * floatNum
        # return Fraction(int(floatNum), den)

    @staticmethod
    def create_from_string(string: str):
        # set_int_max_str_digits(len(string))
        if not isinstance(string, str): raise TypeError("Input must be a string")
        if string.isdigit(): return int(string)
        if fullmatch(r'^\d+.\d*$', string):
            return Fraction(int(string.replace('.','')), 10 ** (len(string) - string.find('.') - 1))
        if fullmatch(r'^\d+.\d*\(\d*\)+', string):
            n1 = string.find('(') - string.find('.') - 1
            n2 = len(string) - string.find('(') - 2
            n3 = int(string.translate(str.maketrans('', '', '().')))
            n4 = int(string.replace('.','')[:string.find('(') - 1])
            return Fraction(n3 - n4, int(f'{"9"*n2}{"0"*n1}'))
        raise TypeError("Not a valid string")

    def as_string_of_numbers(self, nPrec: int = 32) -> str:
        if not isinstance(nPrec , int): raise TypeError
        l_s = [f'{'' if self.num > 0 else '-'}{abs(self.num) // self.den}.']
        rest = abs(self.num) % self.den
        rests_list , count = [] , 0
        while rest and count < nPrec:
            if rest in rests_list:
                index = len(l_s[0]) + rests_list.index(rest)
                return f"{''.join(l_s)[:index]}({''.join(l_s)[index:]})"
            rests_list.append(rest)
            rest *= 10
            l_s.append(f'{rest // self.den}')
            rest %= self.den
            count += 1
        return f'{''.join(l_s)}...' if rest else ''.join(l_s)

    # Metodi non testati !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def __float__(self) -> float: return self.num / self.den

    def __int__ (self) -> int: return int(self.__float__())

    def __len__(self) -> int: return 1

    @staticmethod
    def create_from_float2(floatNum: float):
        if not isinstance(floatNum, float): raise TypeError("Input must be a float")
        return Fraction(*floatNum.as_integer_ratio())

    def improvement_precision_compared_float(self) -> float:
        num_float , den_float = float(self).as_integer_ratio()
        num = self.num * den_float - num_float * self.den
        den = self.den * den_float
        return Fraction(num, den).as_string_of_numbers(1000)

    def asStringOfNumbers2(self) -> str:
        l_s , rest = [f'{self.num // self.den}.'] , self.num % self.den
        while rest:
            rest *= 10
            l_s.append(f'{rest // self.den}')
            rest %= self.den
        return ''.join(l_s)
