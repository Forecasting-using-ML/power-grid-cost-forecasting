"""This module contains test code for the binary_mutation_procreator module."""
from unittest import TestCase
from evolve.population import BinaryChromosome
from ..binary_mutation_procreator import *
# setup reproducable randomness for testing random moving parts
from numpy.random import seed
seed(10)


#
# MARK: __init__()
#


class init_ShouldRaiseErrorOnMissingParameters(TestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            mutator = BinaryMutationProcreator()


class init_ShouldCreateMutationProcreator(TestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=0.01)


#
# MARK: mutate
#


class mutate_ShouldRaiseErrorOnInvalidMutateParameters(TestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=0)
        with self.assertRaises(TypeError):
            mutator.mutate('asdf')


def arb_eval(genes):
    """an arbitrary evaluation for creating chromosomes"""
    return 0


class mutate_ShouldNotMutate(TestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=0)
        mutated = mutator.mutate(BinaryChromosome(size=5,
                                                  evaluate=arb_eval,
                                                  initial_state='zeros'))
        self.assertEqual([0,0,0,0,0], list(mutated.genes))


class mutate_ShouldNotMutateList(TestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=0)
        choms = [
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        ]
        mutated = mutator.mutate(choms)
        self.assertEqual([0,0,0,0,0], list(mutated[0].genes))
        self.assertEqual([0,0,0,0,0], list(mutated[1].genes))


class mutate_ShouldMutateAll(TestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=1)
        mutated = mutator.mutate(BinaryChromosome(size=5,
                                                  evaluate=arb_eval,
                                                  initial_state='zeros'))
        self.assertEqual([1,1,1,1,1], list(mutated.genes))


class mutate_ShouldMutateAllList(TestCase):
    def runTest(self):
        mutator = BinaryMutationProcreator(mutation_rate=1)
        choms = [
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        ]
        mutated = mutator.mutate(choms)
        self.assertEqual([1,1,1,1,1], list(mutated[0].genes))
        self.assertEqual([1,1,1,1,1], list(mutated[1].genes))


class mutate_ShouldMutateHalf(TestCase):
    def runTest(self):
        seed(2222)
        mutator = BinaryMutationProcreator(mutation_rate=0.5)
        chroms = [
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='ones'),
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='random')
        ]
        mutated = mutator.mutate(chroms)
        self.assertEqual([0,0,0,0,1], list(mutated[0].genes))
        self.assertEqual([1,1,0,0,0], list(mutated[1].genes))
        self.assertEqual([0,1,1,0,1], list(mutated[2].genes))
