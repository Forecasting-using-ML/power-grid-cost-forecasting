"""Test cases for the MidpointCrossoverProcreator."""
from unittest import TestCase
from evolve.population import BinaryChromosome, RealCodedChromosome
from ..procreator import Procreator
from ..midpoint_crossover import MidpointCrossoverProcreator


#
# MARK: __init__()
#


class ShouldCreateUniformCrossover(TestCase):
    def test(self):
        proc = MidpointCrossoverProcreator()
        self.assertIsInstance(proc, MidpointCrossoverProcreator)
        self.assertIsInstance(proc, Procreator)


#
# MARK: procreate
#


def arb_eval(genes):
    return 0


class ShouldReturnMidpointCrossover1(TestCase):
    def test(self):
        zeros = BinaryChromosome(size=5, initial_state='zeros', evaluate=arb_eval)
        ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        crossover = MidpointCrossoverProcreator()
        children = crossover.procreate([zeros, ones])
        actuals = [0.5, 0.5, 0.5, 0.5, 0.5]
        for gene, actual in zip(children[0].genes, actuals):
            self.assertEqual(gene, actual)


class ShouldReturnMidpointCrossover2(TestCase):
    def test(self):
        zeros = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        crossover = MidpointCrossoverProcreator()
        children = crossover.procreate([zeros, ones])
        actuals = [1, 1, 1, 1, 1]
        for gene, actual in zip(children[0].genes, actuals):
            self.assertEqual(gene, actual)
