from django.test import TestCase
import unittest

def calcular_imc(peso, altura):
    imc = peso/(altura*altura)
    return  imc
        


class TestIMC(unittest.TestCase):
    def test_imc_normal(self):
        self.assertAlmostEqual(calcular_imc(70, 1.7), 24.22, places=2)
    
    def test_imc_abaixo(self):
        self.assertLess(calcular_imc(50, 1.7), 18.5)
    
    def test_imc_acima(self):
        self.assertGreater(calcular_imc(90, 1.7), 25)

if __name__ == '__main__':
    unittest.main()