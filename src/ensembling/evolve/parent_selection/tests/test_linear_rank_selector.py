"""This module tests the linear_rank_selector module."""
import unittest
from numpy import array, ndarray
from evolve.population import BinaryChromosome, ChromosomeFactory
from ..parent_selector import ParentSelector
from ..linear_rank_selector import *


def evaluate(genes: ndarray):
    return genes.sum()


#
# MARK: Abstract Base Class
#


class LinearRankSelectorTestCase(unittest.TestCase):
    def setUp(self):
        self.zerofactory = ChromosomeFactory(BinaryChromosome, 5,
                                             evaluate=evaluate,
                                             initial_state='zeros')
        self.onesfactory = ChromosomeFactory(BinaryChromosome, 5,
                                             evaluate=evaluate,
                                             initial_state='ones')
        self.randfactory = ChromosomeFactory(BinaryChromosome, 5,
                                             evaluate=evaluate,
                                             initial_state='random')
        self.zeropopulation = self.zerofactory.population(10)
        self.onespopulation = self.onesfactory.population(10)
        self.randpopulation = self.randfactory.population(10)
        self.one_and_zero = [self.zeropopulation[0], self.onespopulation[1]]


#
# MARK: __init__()
#


class ShouldInstantiateLinearRankSelelctor(LinearRankSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(LinearRankSelector(), ParentSelector))
        self.assertTrue(isinstance(LinearRankSelector(), LinearRankSelector))


#
# MARK: select(population)
#


class ShouldRaiseErrorOnInvalidPopulationWrongType(LinearRankSelectorTestCase):
    def runTest(self):
        sel = LinearRankSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')


class ShouldSelectProportionately(LinearRankSelectorTestCase):
    def runTest(self):
        sel = LinearRankSelector()
        self.assertEqual([0,0,0,0,0], list(sel.select(self.zeropopulation).genes))
        self.assertEqual([1,1,1,1,1], list(sel.select(self.onespopulation).genes))


class ShouldSelectProportionatelySize2(LinearRankSelectorTestCase):
    def runTest(self):
        sel = LinearRankSelector(size=2)
        self.assertEqual([0,0,0,0,0], list(sel.select(self.zeropopulation)[0].genes))
        self.assertEqual([1,1,1,1,1], list(sel.select(self.onespopulation)[0].genes))
