"""This module contains test code for the chromosome module."""
import unittest
from ..chromosome import *


#
# MARK: Abstract Base Class
#


class ChromosomeTestCase(unittest.TestCase):
    pass


#
# MARK: __init__()
#


class ShouldRaiseErrorOnNoParameters(ChromosomeTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            Chromosome()


class ShouldRaiseErrorOnMissingEvaluation(ChromosomeTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            Chromosome(0)


class ShouldRaiseErrorOnInvalidEvaluation(ChromosomeTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            Chromosome(0, 0)


def arb(genes):
    return 1


class ShouldRaiseErrorOnMissingSize(ChromosomeTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            Chromosome(None, arb)


class ShouldRaiseErrorOnInvalidSizeWrongType(ChromosomeTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            Chromosome('asdf', arb)


class ShouldRaiseErrorOnInvalidSizeNegative(ChromosomeTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            Chromosome(-1, arb)


class ShouldCreateEmptyChromosome(ChromosomeTestCase):
    def runTest(self):
        try:
            Chromosome(0, arb)
        except Exception:
            self.fail('Chromosome raised unexpected error!')


class ShouldCreateChromosome(ChromosomeTestCase):
    def runTest(self):
        try:
            Chromosome(10, arb)
        except Exception:
            self.fail('Chromosome raised unexpected error!')


#
# MARK: properties
#


class ChromosomePropertyTestCase(ChromosomeTestCase):
    def setUp(self):
        self.arb = Chromosome(10, arb)


class ShouldHaveSize(ChromosomePropertyTestCase):
    def runTest(self):
        try:
            self.assertEqual(10, self.arb.size)
        except:
            self.fail('unexpected exception raised')


class ShouldHaveEvaluate(ChromosomePropertyTestCase):
    def runTest(self):
        try:
            self.assertEqual(arb, self.arb.evaluate)
        except:
            self.fail('unexpected exception raised')


class ShouldHaveFitness(ChromosomePropertyTestCase):
    def runTest(self):
        try:
            self.assertEqual(1, self.arb.fitness)
        except:
            self.fail('unexpected exception raised')
