import unittest
from .functions import *


# MARK: Shaffer's F6 Function
#                  sin**2(sqrt(x**2 + y**2)) - 0.5
# f6(x,y) = 0.5 + ---------------------------------
#                   (1.0 + 0.001(x**2 + y**2))**2
# where:
# *   -100 <= x <= 100


class F6TestCase(unittest.TestCase):
    pass


class ShouldNotImportSin(F6TestCase):
    def runTest(self):
        try:
            sin(5)
            self.fail('sin is defined')
        except NameError:
            pass # literally, the test passed


class F6ShouldExist(F6TestCase):
    def runTest(self):
        try:
            f6(1, 1)
        except NameError:
            self.fail('f6 is not defined')


class F6ShouldReturnOrigin(F6TestCase):
    def runTest(self):
        self.assertEqual(0, f6(0, 0))


class F6ShouldReturnFarRight(F6TestCase):
    def runTest(self):
        self.assertAlmostEqual(0.49, f6(100, 100), delta=2)


class F6ShouldReturnFarLeft(F6TestCase):
    def runTest(self):
        self.assertAlmostEqual(0.49, f6(-100, -100), delta=2)
