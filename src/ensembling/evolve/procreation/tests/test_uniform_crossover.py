"""Test cases for the UniformCrossoverProcreator."""
from unittest import TestCase
from evolve.population import BinaryChromosome, RealCodedChromosome
from ..procreator import Procreator
from ..uniform_crossover import UniformCrossoverProcreator


#
# MARK: __init__()
#


class ShouldCreateUniformCrossover(TestCase):
    def test(self):
        proc = UniformCrossoverProcreator()
        self.assertIsInstance(proc, UniformCrossoverProcreator)
        self.assertIsInstance(proc, Procreator)
        self.assertEqual(0.5, proc.probability)


class ShouldRaiseErrorInvalidProbabilityType(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            UniformCrossoverProcreator('asdf')


class ShouldRaiseErrorInvalidProbabilityValueBelowBound(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            UniformCrossoverProcreator(-1)


class ShouldRaiseErrorInvalidProbabilityValueAboveBounds(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            UniformCrossoverProcreator(2)


class ShouldCreateUniformCrossoverWithProbabilityOf0(TestCase):
    def test(self):
        proc = UniformCrossoverProcreator(0)


class ShouldCreateUniformCrossoverWithProbabilityOf1(TestCase):
    def test(self):
        proc = UniformCrossoverProcreator(1)


#
# MARK: repr
#


class ShouldHaveRepr(TestCase):
    def test(self):
        self.assertEqual('UniformCrossoverProcreator(probability=0.5)',
                         repr(UniformCrossoverProcreator()))
        self.assertEqual('UniformCrossoverProcreator(probability=0.3)',
                         repr(UniformCrossoverProcreator(0.3)))


#
# MARK: procreate
#


def arb_eval(genes):
    return 0


class ShouldRaiseErrorOnNoParents(TestCase):
    def test(self):
        crossover = UniformCrossoverProcreator()
        with self.assertRaises(ValueError):
            crossover.procreate([])

class ShouldRaiseErrorOnTooFewParents(TestCase):
    def test(self):
        crossover = UniformCrossoverProcreator()
        with self.assertRaises(ValueError):
            crossover.procreate([BinaryChromosome(size=5, evaluate=arb_eval)])


class ShouldReturnUniformCrossoverProbabilityOf0(TestCase):
    def test(self):
        seed(1)
        zeros = BinaryChromosome(size=5, initial_state='zeros', evaluate=arb_eval)
        ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        crossover = UniformCrossoverProcreator(0)
        children = crossover.procreate([zeros, ones])
        actuals = [0, 0, 0, 0, 0]
        for gene, actual in zip(children[0].genes, actuals):
            self.assertEqual(gene, actual)


class ShouldReturnUniformCrossoverProbabilityOf1(TestCase):
    def test(self):
        seed(1)
        zeros = BinaryChromosome(size=5, initial_state='zeros', evaluate=arb_eval)
        ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        crossover = UniformCrossoverProcreator(1)
        children = crossover.procreate([zeros, ones])
        actuals = [1, 1, 1, 1, 1]
        for gene, actual in zip(children[0].genes, actuals):
            self.assertEqual(gene, actual)


from numpy.random import seed


class ShouldReturnUniformCrossover1(TestCase):
    def test(self):
        seed(1)
        zeros = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        crossover = UniformCrossoverProcreator()
        children = crossover.procreate([zeros, ones])
        actuals = [1, 1, 1, 1, 1]
        for gene, actual in zip(children[0].genes, actuals):
            self.assertEqual(gene, actual)


class ShouldReturnUniformCrossover2(TestCase):
    def test(self):
        seed(1)
        zeros = BinaryChromosome(size=5, initial_state='zeros', evaluate=arb_eval)
        ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)
        crossover = UniformCrossoverProcreator()
        children = crossover.procreate([zeros, ones])
        actuals = [1, 0, 1, 1, 1]
        for gene, actual in zip(children[0].genes, actuals):
            self.assertEqual(gene, actual)
