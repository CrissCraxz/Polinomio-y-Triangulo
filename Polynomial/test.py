import math
import unittest
from polinomio import ecuacionSegundoGrado
class   TestPol(unittest.TestCase):
    def test_polinomio(self):
        a = "t"
        b = 5
        c = 6
        #self.assertEqual(ecuacionSegundoGrado(a,b,c),(((-b + math.sqrt(b*b-4*a*(c))) / (2 * a)),((-b - math.sqrt(b*b-4*a*(c))) / (2 * a))))
        #self.assertEqual(ecuacionSegundoGrado(a,b,c),("raices imaginarias"))
        self.assertEqual(ecuacionSegundoGrado(a,b,c),("valor ingresado no numerico"))
if _name_ == "_main_":
    unittest.main()