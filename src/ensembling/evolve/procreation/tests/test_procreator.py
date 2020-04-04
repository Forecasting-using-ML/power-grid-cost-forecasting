"""This module contains test code for the crossover_procreator module."""
from unittest import TestCase
from evolve.population import BinaryChromosome
from ..procreator import *
# random seed
from numpy.random import seed
seed(10)


#
# MARK: __init__()
#

class ShouldCreateCrossoverProcreator(TestCase):
    def test(self):
        crossover = Procreator()


#
# MARK: repr
#


class ShouldHaveRepr(TestCase):
    def test(self):
        self.assertEqual('Procreator()', repr(Procreator()))


#
# MARK: procreate
#


def arb_eval(genes):
    return 0


class procreate_ShouldRaiseErrorOnMissingParams(TestCase):
    def test(self):
        crossover = Procreator()
        with self.assertRaises(TypeError):
            crossover.procreate()


class procreate_ShouldRaiseErrorOnInvalidParamType(TestCase):
    def test(self):
        crossover = Procreator()
        with self.assertRaises(TypeError):
            crossover.procreate('asdfasdf')


class procreate_ShouldRaiseErrorOnNoParents(TestCase):
    def test(self):
        crossover = Procreator()
        with self.assertRaises(ValueError):
            crossover.procreate([])


class procreate_ShouldRaiseErrorOnTooFewParents(TestCase):
    def test(self):
        crossover = Procreator()
        with self.assertRaises(ValueError):
            crossover.procreate([BinaryChromosome(size=5, evaluate=arb_eval)])


class procreate_ShouldReturnParents(TestCase):
    def test(self):
        crossover = Procreator()
        parents = [
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        ]
        children = crossover.procreate(parents)
        self.assertEqual(parents, children)
