"""Test cases for the FlatCrossoverProcreator."""
from unittest import TestCase
from evolve.population import BinaryChromosome, RealCodedChromosome
from ..procreator import Procreator
from ..flat_crossover import FlatCrossoverProcreator


#
# MARK: __init__()
#


class ShouldCreateFlatCrossover(TestCase):
    def test(self):
        self.assertIsInstance(FlatCrossoverProcreator(), FlatCrossoverProcreator)
        self.assertIsInstance(FlatCrossoverProcreator(), Procreator)


#
# MARK: repr
#


class ShouldHaveRepr(TestCase):
    def test(self):
        self.assertEqual('FlatCrossoverProcreator()', repr(FlatCrossoverProcreator()))


#
# MARK: procreate
#


def arb_eval(genes):
    return 0


class ShouldRaiseErrorOnNoParents(TestCase):
    def test(self):
        crossover = FlatCrossoverProcreator()
        with self.assertRaises(ValueError):
            crossover.procreate([])

class ShouldRaiseErrorOnTooFewParents(TestCase):
    def test(self):
        crossover = FlatCrossoverProcreator()
        with self.assertRaises(ValueError):
            crossover.procreate([BinaryChromosome(size=5, evaluate=arb_eval)])


from numpy.random import seed


# TODO: doesnt really make sense that this is using binary chromosomes though
# error handling would add too over head to the binary chromosome
class ShouldReturnBLXCrossover1(TestCase):
    def test(self):
        seed(1)
        zeros = BinaryChromosome(size=5, initial_state='zeros', evaluate=arb_eval)
        ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        crossover = FlatCrossoverProcreator()
        children = crossover.procreate([zeros, ones])
        actuals = [0.417022004702574, 0.7203244934421581, 0.00011437481734488664, 0.30233257263183977, 0.14675589081711304]
        for gene, actual in zip(children[0].genes, actuals):
            self.assertEqual(gene, actual)


class ShouldReturnBLXCrossover2(TestCase):
    def test(self):
        seed(2)
        c1 = RealCodedChromosome(size=5, initial_state=(0, 1), evaluate=arb_eval)
        c2 = RealCodedChromosome(size=5, initial_state=(0, 1), evaluate=arb_eval)
        crossover = FlatCrossoverProcreator()
        children = crossover.procreate([c1, c2])
        actuals = [0.37036585097396263, 0.1204957780274882, 0.55903038445280817, 0.36564642040673451, 0.39204880791908869]
        for gene, actual in zip(children[0].genes, actuals):
            self.assertEqual(gene, actual)
