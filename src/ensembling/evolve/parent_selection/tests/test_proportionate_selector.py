"""This module tests the proportionate_selector module."""
import unittest
from numpy import array, ndarray
from evolve.population import BinaryChromosome, ChromosomeFactory
from ..parent_selector import ParentSelector
from ..proportionate_selector import *


def evaluate(genes: ndarray):
    return genes.sum()


#
# MARK: Abstract Base Class
#


class ProportionateSelectorTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = ChromosomeFactory(BinaryChromosome, 5,
                                        evaluate=evaluate,
                                        initial_state='zeros')
        self.population = self.factory.population(10)


#
# MARK: __init__()
#


class ShouldInstantiateProportionateSelector(ProportionateSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(ProportionateSelector(), ParentSelector))
        self.assertTrue(isinstance(ProportionateSelector(), ProportionateSelector))


#
# MARK: select(population)
#


class ShouldRaiseErrorOnInvalidPopulationWrongType(ProportionateSelectorTestCase):
    def runTest(self):
        sel = ProportionateSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')


class ShouldSelectProportionately(ProportionateSelectorTestCase):
    def runTest(self):
        sel = ProportionateSelector()
        self.assertEqual([0,0,0,0,0], list(sel.select(self.population).genes))


class ShouldSelectProportionatelySize2(ProportionateSelectorTestCase):
    def runTest(self):
        sel = ProportionateSelector(size=2)
        self.assertEqual([0,0,0,0,0], list(sel.select(self.population)[0].genes))
        self.assertEqual([0,0,0,0,0], list(sel.select(self.population)[1].genes))
