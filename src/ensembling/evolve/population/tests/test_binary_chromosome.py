"""This module contains test code for the binary chromosome module."""
import unittest
import numpy as np
from ..chromosome import Chromosome
from ..binary_chromosome import *


def arb():
    """an arbitrary method that does nothing"""
    pass


#
# MARK: Abstract Base Class
#


class BinaryChromosomeTestCase(unittest.TestCase):
    """An abstract base test for binary chromosomes."""
    pass


#
# MARK: __init__()
#


class ShouldBeSubclassOfChromosome(BinaryChromosomeTestCase):
    def runTest(self):
        self.assertTrue(issubclass(BinaryChromosome, Chromosome))


class ShouldCreateDefaultChromosome(BinaryChromosomeTestCase):
    def runTest(self):
        try:
            BinaryChromosome(0, arb)
        except:
            self.fail('raised unexpected error!')


class ShouldRaiseErrorOnInvalidInitialStateWrongType(BinaryChromosomeTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            BinaryChromosome(0, arb, initial_state=0)


class ShouldRaiseErrorOnInvalidInitialState(BinaryChromosomeTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            BinaryChromosome(0, arb, initial_state='asdf')


class ShouldCreateChromosomeWithZeros(BinaryChromosomeTestCase):
    def runTest(self):
        try:
            chrom = BinaryChromosome(3, arb, initial_state='zeros')
            self.assertEqual(list(chrom.genes), [0, 0, 0])
        except:
            self.fail('raised unexpected error!')


class ShouldCreateChromosomeWithOnes(BinaryChromosomeTestCase):
    def runTest(self):
        try:
            chrom = BinaryChromosome(3, arb, initial_state='ones')
            self.assertEqual(list(chrom.genes), [1, 1, 1])
        except:
            self.fail('raised unexpected error!')


class ShouldCreateChromosomeWithRandoms(BinaryChromosomeTestCase):
    def runTest(self):
        try:
            chrom = BinaryChromosome(3, arb, initial_state='random')
            self.assertEqual(3, len(chrom.genes))
        except:
            self.fail('raised unexpected error!')


#
# MARK: Fitness
#


def real_evaluate(genes: np.array):
    """A real evaluation function for testing purposes"""
    weights = np.array([
        10,
        5,
        2
    ])
    return np.multiply(genes, weights).sum()


class ShouldReturnCalculatedFitnessOnes(BinaryChromosomeTestCase):
    def runTest(self):
        chrom = BinaryChromosome(3, real_evaluate, initial_state='ones')
        self.assertEqual(17, chrom.fitness)


class ShouldReturnCalculatedFitnessZeros(BinaryChromosomeTestCase):
    def runTest(self):
        chrom = BinaryChromosome(3, real_evaluate, initial_state='zeros')
        self.assertEqual(0, chrom.fitness)


class ShouldReturnCalculatedFitnessRandom(BinaryChromosomeTestCase):
    def runTest(self):
        chrom = BinaryChromosome(3, real_evaluate, initial_state='random')
        self.assertTrue(0 <= chrom.fitness)
        self.assertTrue(chrom.fitness <= 17)
