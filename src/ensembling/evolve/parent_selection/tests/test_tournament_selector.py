"""This module tests the tournament_selector module."""
import unittest
from numpy import array, ndarray
from evolve.population import BinaryChromosome, ChromosomeFactory
from ..parent_selector import ParentSelector
from ..tournament_selector import *
from numpy.random import seed


def evaluate(genes: ndarray):
    return genes.sum()


#
# MARK: Abstract Base Class
#


class TournamentSelectorTestCase(unittest.TestCase):
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


class ShouldInstantiateParentSelector(TournamentSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(TournamentSelector(), ParentSelector))
        self.assertTrue(isinstance(TournamentSelector(), TournamentSelector))


class ShouldRaiseErrorOnInvalidIndividualsPerTournyType(TournamentSelectorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            TournamentSelector(individuals_per_tournament='asdf')


class ShouldRaiseErrorOnInvalidIndividualsPerTournyNegative(TournamentSelectorTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            TournamentSelector(individuals_per_tournament=-1)


#
# MARK: select(population)
#


class ShouldRaiseErrorOnInvalidPopulationWrongType(TournamentSelectorTestCase):
    def runTest(self):
        sel = TournamentSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')


class ShouldSelectProportionatelyNoneSize(TournamentSelectorTestCase):
    def runTest(self):
        seed(3000)
        selector = TournamentSelector(individuals_per_tournament=3)
        selection0 = selector.select(self.zeropopulation)
        selection1 = selector.select(self.onespopulation)
        self.assertEqual([0, 0, 0, 0, 0], list(selection0[0].genes))
        self.assertEqual([1, 1, 1, 1, 1], list(selection1[1].genes))


class ShouldSelectProportionatelySize1(TournamentSelectorTestCase):
    def runTest(self):
        seed(3001)
        selector = TournamentSelector(individuals_per_tournament=3, size=1)
        selection = selector.select(self.onespopulation)
        self.assertEqual([1, 1, 1, 1, 1], list(selection[0].genes))


class ShouldSelectProportionatelySize2(TournamentSelectorTestCase):
    def runTest(self):
        seed(3005)
        selector = TournamentSelector(individuals_per_tournament=3, size=2)
        selection = selector.select(self.randpopulation)
        self.assertEqual([1, 1, 1, 1, 0], list(selection[0].genes))
        self.assertEqual([0, 1, 1, 0, 0], list(selection[1].genes))
