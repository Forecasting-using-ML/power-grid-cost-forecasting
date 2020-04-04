"""This module contains test cases for the ChromosomeFactory class."""
import unittest
from ..chromosome import Chromosome
from ..binary_chromosome import *
from ..realcoded_chromosome import *
from ..chromosome_factory import *


def arb_eval(genes):
    return 1


#
# MARK: Abstract Base Class
#


class ChromosomeFactoryTestCase(unittest.TestCase):
    pass

#
# MARK: __init__()
#

class ShouldRaiseErrorOnNoParameters(ChromosomeFactoryTestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory()


class ShouldRaiseErrorOnMissingChromosomeSize(ChromosomeFactoryTestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(Chromosome)


class ShouldRaiseErrorOnMissingEvaluation(ChromosomeFactoryTestCase):
    def test(self):
        with self.assertRaises(TypeError):
            ChromosomeFactory(Chromosome, 10)


class ShouldCreateChromosomeFactory(ChromosomeFactoryTestCase):
    def test(self):
        ChromosomeFactory(Chromosome, 10, arb_eval)


#
# MARK: next_individual
#


class ShouldCreateChromosomeFromFactory(ChromosomeFactoryTestCase):
    def test(self):
        factory = ChromosomeFactory(Chromosome, 10, arb_eval)
        self.assertTrue(isinstance(factory.next_individual, Chromosome))


class ShouldCreateBinaryChromosomeFromFactory(ChromosomeFactoryTestCase):
    def test(self):
        factory = ChromosomeFactory(BinaryChromosome, 5, arb_eval, 'zeros')
        self.assertTrue(isinstance(factory.next_individual, BinaryChromosome))
        self.assertEqual(list(factory.next_individual.genes), [0,0,0,0,0])


class ShouldCreateRealCodedChromosomeFromFactory(ChromosomeFactoryTestCase):
    def test(self):
        factory = ChromosomeFactory(RealCodedChromosome, 5, arb_eval, (1, 2))
        self.assertTrue(isinstance(factory.next_individual, RealCodedChromosome))
        for gene in factory.next_individual.genes:
            self.assertTrue(gene >= 1)
            self.assertTrue(gene <= 2)


#
# MARK: population
#


class ShouldCreateChromosomePopulationFromFactory(ChromosomeFactoryTestCase):
    def test(self):
        factory = ChromosomeFactory(Chromosome, 10, arb_eval)
        pop = factory.population(10)
        self.assertTrue(isinstance(pop, list))
        self.assertTrue(isinstance(pop[0], Chromosome))
        self.assertTrue(isinstance(pop[9], Chromosome))


class ShouldCreateBinaryChromosomePopulationFromFactory(ChromosomeFactoryTestCase):
    def test(self):
        factory = ChromosomeFactory(BinaryChromosome, 5, arb_eval, 'ones')
        pop = factory.population(10)
        self.assertTrue(isinstance(pop, list))
        self.assertTrue(isinstance(pop[0], BinaryChromosome))
        self.assertTrue(isinstance(pop[9], BinaryChromosome))
        self.assertEqual(list(pop[0].genes), [1,1,1,1,1])
