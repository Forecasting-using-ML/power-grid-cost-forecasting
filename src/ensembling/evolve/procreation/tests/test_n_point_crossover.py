"""This module contains test code for the n_point_crossover module."""
from unittest import TestCase
# setup randomness for testing random moving parts (not very TDD, but le fek it)
from numpy.random import seed
seed(10)
from evolve.population import BinaryChromosome
from ..n_point_crossover import *


#
# MARK: __init__()
#


class ShouldRaiseErrorOnInvalidNType(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            crossover = NPointCrossoverProcreator(crossovers='asdf')


class ShouldRaiseErrorOnInvalidNValue(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            crossover = NPointCrossoverProcreator(crossovers=-1)


class ShouldCreateNPointCrossoverWithDefaultN(TestCase):
    def test(self):
        crossover = NPointCrossoverProcreator()
        self.assertEqual(1, crossover.crossovers)


class ShouldCreateNPointCrossoverWithN0(TestCase):
    def test(self):
        crossover = NPointCrossoverProcreator(crossovers=0)
        self.assertEqual(0, crossover.crossovers)


class ShouldCreateNPointCrossoverWithN3(TestCase):
    def test(self):
        crossover = NPointCrossoverProcreator(crossovers=3)
        self.assertEqual(3, crossover.crossovers)


#
# MARK: repr
#


class ShouldHaveRepr(TestCase):
    def test(self):
        self.assertEqual('NPointCrossoverProcreator(crossovers=1)',
                         repr(NPointCrossoverProcreator()))
        self.assertEqual('NPointCrossoverProcreator(crossovers=2)',
                         repr(NPointCrossoverProcreator(2)))


#
# MARK: procreate
#


def arb_eval(genes):
    return 0


zeros = BinaryChromosome(size=5, initial_state='zeros', evaluate=arb_eval)
ones = BinaryChromosome(size=5, initial_state='ones', evaluate=arb_eval)


class ShouldRaiseErrorOnNoParents(TestCase):
    def test(self):
        crossover = NPointCrossoverProcreator()
        with self.assertRaises(ValueError):
            crossover.procreate([])

class ShouldRaiseErrorOnTooFewParents(TestCase):
    def test(self):
        crossover = NPointCrossoverProcreator()
        with self.assertRaises(ValueError):
            crossover.procreate([ones])


class ShouldPerform0PointCrossover(TestCase):
    def test(self):
        crossover = NPointCrossoverProcreator(crossovers=0)
        children = crossover.procreate([ones, zeros])
        self.assertEqual([1,1,1,1,1], list(children[0].genes))
        self.assertEqual([0,0,0,0,0], list(children[1].genes))


class ShouldPerform1PointCrossover(TestCase):
    def test(self):
        seed(1000)
        crossover = NPointCrossoverProcreator(crossovers=1)
        children = crossover.procreate([ones, zeros])
        self.assertEqual([1,1,1,0,0], list(children[0].genes))
        self.assertEqual([0,0,0,1,1], list(children[1].genes))


class ShouldPerform2PointCrossover(TestCase):
    def test(self):
        seed(1001)
        crossover = NPointCrossoverProcreator(crossovers=2)
        children = crossover.procreate([ones, zeros])
        self.assertEqual([1,0,0,1,1], list(children[0].genes))
        self.assertEqual([0,1,1,0,0], list(children[1].genes))


class ShouldPerform3PointCrossover(TestCase):
    def test(self):
        seed(1002)
        crossover = NPointCrossoverProcreator(crossovers=3)
        children = crossover.procreate([ones, zeros])
        self.assertEqual([1,0,1,0,0], list(children[0].genes))
        self.assertEqual([0,1,0,1,1], list(children[1].genes))


class ShouldPerform4PointCrossover(TestCase):
    def test(self):
        crossover = NPointCrossoverProcreator(crossovers=4)
        children = crossover.procreate([ones, zeros])
        self.assertEqual([1,0,1,0,1], list(children[0].genes))
        self.assertEqual([0,1,0,1,0], list(children[1].genes))


class ShouldRaiseErrorOn5PointCrossover(TestCase):
    def test(self):
        crossover = NPointCrossoverProcreator(crossovers=5)
        with self.assertRaises(ValueError):
            crossover.procreate([ones, zeros])
