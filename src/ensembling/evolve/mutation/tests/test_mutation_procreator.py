"""This module contains test code for the mutation_procreator module."""
import unittest
from evolve.population import BinaryChromosome
from ..mutator import *


#
# MARK: Abstract Base Class
#


class MutationProcreatorTestCase(unittest.TestCase):
    pass


#
# MARK: __init__()
#


class ShouldRaiseErrorOnMissingParameters(MutationProcreatorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            mutator = Mutator()


class ShouldRaiseErrorOnInvalidMutationRateWrongType(MutationProcreatorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            mutator = Mutator('asdf')


class ShouldRaiseErrorOnNegativeMutationRate(MutationProcreatorTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            mutator = Mutator(-0.01)


class ShouldRaiseErrorOnAboveOneMutationRate(MutationProcreatorTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            mutator = Mutator(1.01)


class ShouldCreateMutationProcreatorRate0(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0)


class ShouldCreateMutationProcreatorRate1(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=1)


class ShouldCreateMutationProcreatorRateArb(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)


#
# MARK: mutate
#


class mutate_ShouldRaiseErrorOnMissingParameters(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)
        with self.assertRaises(TypeError):
            mutator.mutate()


class mutate_ShouldRaiseErrorOnInvalidParamWrongType(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)
        with self.assertRaises(TypeError):
            mutator.mutate('asdf')


def arb_eval(genes):
    return 0


class mutate_ShouldNotMutateRate0(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0)
        mutated = mutator.mutate(BinaryChromosome(size=5,
                                                  evaluate=arb_eval,
                                                  initial_state='zeros'))
        self.assertEqual([0,0,0,0,0], list(mutated.genes))


class mutate_ShouldNotMutateRate0List(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0)
        chroms = [
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        ]
        mutated = mutator.mutate(chroms)
        self.assertEqual([0,0,0,0,0], list(mutated[0].genes))
        self.assertEqual([0,0,0,0,0], list(mutated[1].genes))


class mutate_ShouldNotMutateRate1(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=1)
        mutated = mutator.mutate(BinaryChromosome(size=5,
                                                  evaluate=arb_eval,
                                                  initial_state='zeros'))
        self.assertEqual([0,0,0,0,0], list(mutated.genes))


class mutate_ShouldRaiseErrorOnInvalidInPlaceWrongType(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)
        chrom = BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        with self.assertRaises(TypeError):
            mutator.mutate(chrom, 'asdf')


class mutate_ShouldMutateInPlace(MutationProcreatorTestCase):
    def runTest(self):
        mutator = Mutator(mutation_rate=0.01)
        chrom = BinaryChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        mutator.mutate(chrom, True)
