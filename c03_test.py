import unittest
from c03 import * 

class TestFraction (unittest.TestCase):

    def test___init__(self):
        self.assertEqual(Fraction( 0, 4), 0)
        self.assertEqual(Fraction( 8, 4), 2)
        self.assertEqual(Fraction(-8, 4),-2)
        self.assertEqual(Fraction( 8,-4),-2)
        self.assertEqual(Fraction(-8,-4), 2)
        a = Fraction( 2,10)
        self.assertEqual((a.num , a.den),  ( 1,  5))
        a = Fraction( 3,10)
        self.assertEqual((a.num , a.den),  ( 3, 10))
        a = Fraction(-3,10)
        self.assertEqual((a.num , a.den),  (-3, 10))
        a = Fraction( 3,-8)
        self.assertEqual((a.num , a.den),  (-3,  8))
        a = Fraction(-3,-8)
        self.assertEqual((a.num , a.den),  ( 3,  8))
        with self.assertRaises(TypeError): Fraction(8.,4)
        with self.assertRaises(TypeError): Fraction('8.',4)
        with self.assertRaises(TypeError): Fraction(8,4.)
        with self.assertRaises(TypeError): Fraction(8,"4.")
        with self.assertRaises(TypeError): Fraction(8.,4.)
        with self.assertRaises(TypeError): Fraction('8',"4.")
        with self.assertRaises(ZeroDivisionError): Fraction(8,0)

    def test___str__(self):
        self.assertEqual(Fraction(1,10).__str__(),'1/10')
        self.assertEqual(Fraction(-1,3).__str__(),'-1/3')

    # def test___repr__(self):
    #     self.assertEqual(Fraction(1,10).__repr__(),'Fraction object: 1/10 = 0.1')
    #     self.assertEqual(Fraction(-1,3).__repr__(),'Fraction object: -1/3 = -0.(3)')
    #     self.assertEqual(Fraction(1,10).__len__(),1)

    def test_immutable(self):
        a = Fraction(-4,5)
        with self.assertRaises(ValueError): a.num = 6
        with self.assertRaises(ValueError): a.den = 6
        with self.assertRaises(ValueError): a.denominator = 6

    def test___neg__(self):
        a = Fraction(-4,5)
        b = -a
        self.assertEqual((a.num , a.den), (-4, 5))
        self.assertEqual((b.num , b.den), ( 4, 5))
        a = - Fraction(-7,2)
        self.assertEqual((a.num , a.den), ( 7, 2))

    def test_inverse(self):
        b = Fraction(-4,5)
        a = b.inverse()
        self.assertEqual((a.num,a.den) , (-5, 4))
        self.assertEqual((b.num,b.den) , (-4, 5))

    def test___add__(self):
        a = Fraction( 1,10) + Fraction( 2,10) # float error!! 0.1 + 0.2 -> # 0.30000000000000004
        self.assertEqual((a.num , a.den),  ( 3, 10))
        a = Fraction(-1,10) + Fraction( 2,10)
        self.assertEqual((a.num , a.den),  ( 1, 10))
        a = Fraction(-1,10) + Fraction(-2,10) # float error!! -0.1 + -0.2 -> # -0.30000000000000004
        self.assertEqual((a.num , a.den),  (-3, 10))
        a = Fraction( 1,10) + Fraction(-2,10)
        self.assertEqual((a.num , a.den),  (-1, 10))
        a = Fraction( 2,10) + 1
        self.assertEqual((a.num , a.den),  ( 6,  5))
        a = Fraction( 1,10) + -1
        self.assertEqual((a.num , a.den),  (-9, 10))
        with self.assertRaises(TypeError): Fraction( 1,10) + 'e'

    def test___radd__(self):
        a =  1 + Fraction(1,5)
        self.assertEqual((a.num , a.den), ( 6, 5))
        a = -1 + Fraction(1,5)
        self.assertEqual((a.num , a.den), (-4, 5))

    def test___sub__(self):
        a = Fraction( 1,10) - Fraction( 1, 5)
        self.assertEqual((a.num , a.den),  (-1, 10))
        a = Fraction(-1,10) - Fraction( 1, 5)
        self.assertEqual((a.num , a.den),  (-3, 10))
        a = Fraction(-1,10) - Fraction(-1, 5)
        self.assertEqual((a.num , a.den),  ( 1, 10))
        a = Fraction( 1,10) - Fraction(-1, 5)
        self.assertEqual((a.num , a.den),  ( 3, 10))
        a = Fraction( 2,10) - 1
        self.assertEqual((a.num , a.den),  (-4,  5))
        a = Fraction( 1,10) - -1
        self.assertEqual((a.num , a.den),  (11, 10))

    def test___rsub__(self):
        a =  1 - Fraction(1,5)
        self.assertEqual((a.num , a.den),  ( 4, 5))
        a = -1 - Fraction(1,5)
        self.assertEqual((a.num , a.den),  (-6, 5))

    def test___mul__(self):
        a = Fraction( 1,10) * Fraction( 1, 5)
        self.assertEqual((a.num , a.den),  ( 1, 50))
        a = Fraction(-1,10) * Fraction( 1, 5)
        self.assertEqual((a.num , a.den),  (-1, 50))
        a = Fraction( 1,10) * Fraction(-1, 5)
        self.assertEqual((a.num , a.den),  (-1, 50))
        a = Fraction(-1,10) * Fraction(-1, 5)
        self.assertEqual((a.num , a.den),  ( 1,  50))
        a = Fraction( 7,10) * Fraction( 7,10) # float error!! 0.7*0.7 -> 0.48999999999999994
        self.assertEqual((a.num , a.den),  (49, 100))
        a = Fraction(-1,10) * 3
        self.assertEqual((a.num , a.den),  (-3, 10))
        a = Fraction(-1,10) * 10
        self.assertEqual(a, -1)
        a = Fraction( 2, 3) * Fraction( 9, 2)
        self.assertEqual(a,  3)

    def test___rmul__(self):
        a = 3 * Fraction(-1,10)
        self.assertEqual((a.num , a.den),  (-3, 10))
        a = 10 * Fraction(-1,10)
        self.assertEqual(a, -1)

    def test___truediv__(self):
        a = Fraction( 1,10) / Fraction( 1, 5)
        self.assertEqual((a.num , a.den), ( 1,  2))
        a = Fraction(-1,10) / Fraction( 1, 5)
        self.assertEqual((a.num , a.den), (-1,  2))
        a = Fraction( 1,10) / Fraction(-1, 5)
        self.assertEqual((a.num , a.den), (-1,  2))
        a = Fraction(-1,10) / Fraction(-1, 5)
        self.assertEqual((a.num , a.den), ( 1,  2))
        a = Fraction(12,11) / 2
        self.assertEqual((a.num , a.den), ( 6, 11))
        a = Fraction( 9, 2) / Fraction( 3, 2)
        self.assertEqual(a,  3)

    def test___floordiv__(self):
        a = Fraction(71,2) // Fraction(8,5)
        self.assertEqual(a, 22)

    def test___mod___(self):
        a = Fraction(71,2) % Fraction(8,5)
        self.assertEqual(a, 0.29999999999999805)

    def test__pow__(self):
        a = Fraction(2, 3) **  2
        self.assertEqual((a.num,a.den) , ( 4,  9))
        a = Fraction(7,10) **  2 # float error!! 0.7**2 -> 0.48999999999999994
        self.assertEqual((a.num,a.den) , (49,100))
        a = Fraction(2, 3) ** -2 # float error!! (2/3)**-2 -> 2.2500000000000004
        self.assertEqual((a.num,a.den) , ( 9,  4))
        a = Fraction(2, 3) **  0
        self.assertEqual(a, 1)
        with self.assertRaises(TypeError): Fraction(2,3) ** 2.5

    def test___rtruediv__(self):
        a = 2 / Fraction(12,11)
        self.assertEqual((a.num , a.den),  (11, 6))

    # def test___pos___(self):
    #     self.assertEqual(Fraction(7,2), +Fraction(7,2))

    def test___lt__(self):
        self.assertEqual(Fraction( 9,10) < Fraction(11,10), True)
        self.assertEqual(Fraction( 9,10) < 1, True)
        self.assertEqual(Fraction(11,10) < 1, False)
        self.assertEqual(Fraction( 5, 2) < 2.6, True)
        self.assertEqual(Fraction( 5, 2) < 2.4, False)
        self.assertEqual(1 > Fraction( 9,10), True)
        self.assertEqual(1 > Fraction(11,10), False)
        self.assertEqual(2.6 > Fraction( 5, 2), True)
        self.assertEqual(2.4 > Fraction( 5, 2), False)

    def test___le__(self):
        self.assertEqual(Fraction( 9,10) <= 1, True)
        self.assertEqual(Fraction( 9,10) <= Fraction(11,10), True)
        self.assertEqual(Fraction( 5, 2) <= 2.6, True)
        self.assertEqual(Fraction( 5, 2) <= 2.5, True)
        self.assertEqual(Fraction( 5, 2) <= 2.4, False)
        self.assertEqual(Fraction(11,10) <= 1  , False)
        self.assertEqual(1 >= Fraction( 9,10), True)
        self.assertEqual(2.6 >= Fraction( 5, 2), True)
        self.assertEqual(2.5 >= Fraction( 5, 2), True)
        self.assertEqual(2.4 >= Fraction( 5, 2), False)
        self.assertEqual(1 >= Fraction(11,10), False)

    def test___eq__(self):
        self.assertEqual(Fraction(2,3) == Fraction(2,3), True)
        self.assertEqual(Fraction(7,2) == Fraction(6,2), False)
        self.assertEqual(Fraction(6,2) == Fraction(3,2), False)
        self.assertEqual(Fraction(3,1) == 3, True)
        self.assertEqual(Fraction(6,2) == 3, True)
        self.assertEqual(Fraction(5,2) == 2.5, True)
        self.assertEqual(Fraction(2,3) == "3", False)

    def test___ge__(self):
        self.assertEqual(Fraction( 9,10) >= 1, False)
        self.assertEqual(Fraction( 9,10) >= Fraction(11,10), False)
        self.assertEqual(Fraction( 5, 2) >= 2.6, False)
        self.assertEqual(Fraction( 5, 2) >= 2.5, False)
        self.assertEqual(Fraction( 5, 2) >= 2.4, True)
        self.assertEqual(Fraction(11,10) >= 1  , True)
        self.assertEqual(1 <= Fraction( 9,10), False)
        self.assertEqual(2.6 <= Fraction( 5, 2), False)
        self.assertEqual(2.5 <= Fraction( 5, 2), False)
        self.assertEqual(2.4 <= Fraction( 5, 2), True)
        self.assertEqual(1 <= Fraction(11,10), True)

    def test___gt__(self):
        self.assertEqual(Fraction( 9,10) > Fraction(11,10), False)
        self.assertEqual(Fraction( 9,10) > 1, False)
        self.assertEqual(Fraction(11,10) > 1, True)
        self.assertEqual(Fraction( 5, 2) > 2.6, False)
        self.assertEqual(Fraction( 5, 2) > 2.4, True)
        self.assertEqual(1 < Fraction( 9,10), False)
        self.assertEqual(1 < Fraction(11,10), True)
        self.assertEqual(2.6 < Fraction( 5, 2), False)
        self.assertEqual(2.4 < Fraction( 5, 2), True)

    def test___ne__(self):
        F2 = Fraction(2,5)
        self.assertEqual(F2 != 3, True)
        self.assertEqual(F2 != 2.1, True)
        self.assertEqual(F2 != "3", True)
        self.assertEqual(Fraction(6,2) != Fraction(9,4), True)

    def test___abs__(self):
        a = abs(Fraction( 4,5))
        self.assertEqual((a.num , a.den), (4,5))
        a = abs(Fraction(-4,5))
        self.assertEqual((a.num , a.den), (4,5))

    def test_inverti(self):
        a = Fraction(3,2)
        b = Fraction(2,3).inverse()
        self.assertEqual((a.num,a.den) , (b.num,b.den))
        a = Fraction(-3,2)
        b = Fraction(-2,3).inverse()
        self.assertEqual((a.num,a.den) , (b.num,b.den))

    def test_create_from_float(self):
        a = Fraction.create_from_float(0.3)
        self.assertEqual((a.num,a.den) , ( 3,10))
        a = Fraction.create_from_float(-0.3)
        self.assertEqual((a.num,a.den) , (-3,10))
        a = Fraction.create_from_float(3.1415926535897932384626433832795028841971) # pi
        self.assertEqual((a.num,a.den) , (7853981633974483 , 2500000000000000))
        a = Fraction.create_from_float(2.7182818284590452353602874713526624977572) # e
        self.assertEqual((a.num,a.den) , (6795704571147613 , 2500000000000000))
        with self.assertRaises(TypeError): Fraction.create_from_float("£")

    def test_create_from_string(self):
        with self.assertRaises(TypeError): Fraction.create_from_string("£")
        with self.assertRaises(TypeError): Fraction.create_from_string("0.75 ")
        with self.assertRaises(TypeError): Fraction.create_from_string(" 0.75")
        with self.assertRaises(TypeError): Fraction.create_from_string(" 0.75 ")
        with self.assertRaises(TypeError): Fraction.create_from_string("1(857142)")
        a = Fraction.create_from_string("1")
        self.assertEqual(a , 1)
        a = Fraction.create_from_string("1.")
        self.assertEqual(a , 1)
        a = Fraction.create_from_string("0.75")
        self.assertEqual((a.num , a.den) , (3,4))
        a = Fraction.create_from_string("3.1415926535897932384626433832795028841971")
        self.assertEqual((a.num , a.den) , (31415926535897932384626433832795028841971,10000000000000000000000000000000000000000))
        with self.assertRaises(KeyError): Fraction.create_from_string("1.(857142)")
        with self.assertRaises(KeyError): Fraction.create_from_string("0.58(3)")

    def test_asStringOfNumbers(self):
        self.assertEqual(Fraction(  3, 4).asStringOfNumbers() , '0.75')
        self.assertEqual(Fraction(  3, 4).asStringOfNumbers(2), '0.75')
        self.assertEqual(Fraction(  5, 2).asStringOfNumbers() , '2.5')
        self.assertEqual(Fraction(  3,99).asStringOfNumbers() , '0.(03)')
        self.assertEqual(Fraction( 29,22).asStringOfNumbers() , '1.3(18)')
        self.assertEqual(Fraction(290,22).asStringOfNumbers() , '13.(18)')
        self.assertEqual(Fraction( 13, 7).asStringOfNumbers() , '1.(857142)')
        self.assertEqual(Fraction( 13, 7).asStringOfNumbers(4), '1.8571...')
        self.assertEqual(Fraction(130, 7).asStringOfNumbers() , '18.(571428)')
        self.assertEqual(Fraction( 49,33).asStringOfNumbers() , '1.(48)')
        self.assertEqual(Fraction(  7, 3).asStringOfNumbers() , '2.(3)')
        self.assertEqual(Fraction(  7,12).asStringOfNumbers() , '0.58(3)')

    # def test_errorComparedToFloat(self):
    #     self.assertEqual(Fraction(1,10).errorComparedToFloat(),'-0.0000000000000000055511151231257827021181583404541015625')
    #     self.assertEqual(Fraction(2,10).errorComparedToFloat(),'-0.000000000000000011102230246251565404236316680908203125')
    #     self.assertEqual(Fraction(3,10).errorComparedToFloat(),'0.000000000000000011102230246251565404236316680908203125')

if __name__ == '__main__':
    unittest.main(verbosity=1)
