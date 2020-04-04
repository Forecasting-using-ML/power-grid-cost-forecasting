"""Test cases for the RealCodedMutationProcreator class."""
from unittest import TestCase
from evolve.population import RealCodedChromosome
from ..realcoded_mutation_procreator import *
# setup reproducable randomness for testing random moving parts
from numpy.random import seed
seed(10)


#
# MARK: __init__()
#


class init_ShouldRaiseErrorOnMissingParameters(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            mutator = RealCodedMutationProcreator()


class init_ShouldCreateMutationProcreator(TestCase):
    def test(self):
        mutator = RealCodedMutationProcreator(mutation_rate=0.01)


#
# MARK: mutate
#


class mutate_ShouldRaiseErrorOnInvalidMutateParameters(TestCase):
    def runTest(self):
        mutator = RealCodedMutationProcreator(mutation_rate=0)
        with self.assertRaises(TypeError):
            mutator.mutate('asdf')


def arb_eval(genes):
    """an arbitrary evaluation for creating chromosomes"""
    return 0


class mutate_ShouldNotMutate(TestCase):
    def runTest(self):
        mutator = RealCodedMutationProcreator(mutation_rate=0)
        mutated = mutator.mutate(RealCodedChromosome(size=5,
                                                    evaluate=arb_eval,
                                                    initial_state='zeros'))
        self.assertEqual([0,0,0,0,0], list(mutated.genes))


class mutate_ShouldNotMutateList(TestCase):
    def runTest(self):
        mutator = RealCodedMutationProcreator(mutation_rate=0)
        choms = [
            RealCodedChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            RealCodedChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        ]
        mutated = mutator.mutate(choms)
        self.assertEqual([0,0,0,0,0], list(mutated[0].genes))
        self.assertEqual([0,0,0,0,0], list(mutated[1].genes))


class mutate_ShouldMutateAll(TestCase):
    def runTest(self):
        mutator = RealCodedMutationProcreator(mutation_rate=1)
        mutated = mutator.mutate(RealCodedChromosome(size=5,
                                                    evaluate=arb_eval,
                                                    initial_state='zeros'))
        expected = [
            0.035645217728072498,
            0.36092494757777704,
            0.78684060294525748,
            0.19489478127792192,
            0.82462008610850868
        ]
        self.assertEqual(expected, list(mutated.genes))


class mutate_ShouldMutateAllRange(TestCase):
    def runTest(self):
        mutator = RealCodedMutationProcreator(mutation_rate=1, random_state=(5, 6))
        mutated = mutator.mutate(RealCodedChromosome(size=5,
                                                    evaluate=arb_eval,
                                                    initial_state='zeros'))
        for gene in mutated.genes:
            self.assertTrue(gene >= 5)
            self.assertTrue(gene <= 6)


class mutate_ShouldMutateAllList(TestCase):
    def runTest(self):
        mutator = RealCodedMutationProcreator(mutation_rate=1)
        choms = [
            RealCodedChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            RealCodedChromosome(size=5, evaluate=arb_eval, initial_state='zeros')
        ]
        mutated = mutator.mutate(choms)
        self.assertIsInstance(mutated, list)
        c0 = [
            0.30832661028386366,
            0.88044022543339817,
            0.46543856301041264,
            0.98869229439494866,
            0.60293320750348567
        ]
        self.assertEqual(c0, list(mutated[0].genes))
        c1 = [
            0.026083263963949999,
            0.84022433810931996,
            0.94752328271635278,
            0.90267393734810486,
            0.73721915166454299
        ]
        self.assertEqual(c1, list(mutated[1].genes))


class mutate_ShouldMutateHalf(TestCase):
    def runTest(self):
        seed(2222)
        mutator = RealCodedMutationProcreator(mutation_rate=0.5)
        chroms = [
            RealCodedChromosome(size=5, evaluate=arb_eval, initial_state='zeros'),
            RealCodedChromosome(size=5, evaluate=arb_eval, initial_state='ones'),
            RealCodedChromosome(size=5, evaluate=arb_eval, initial_state='ones')
        ]
        mutated = mutator.mutate(chroms)
        c0 = [0.0, 0.63031517659402647, 0.0, 0.0, 0.87853488435848204]
        self.assertEqual(c0, list(mutated[0].genes))
        c1 = [
            1.0,
            1.0,
            0.65607322932247725,
            0.79059298145077039,
            0.39962985333928835
        ]
        self.assertEqual(c1, list(mutated[1].genes))
        c2 = [1.0, 0.36963020168002036, 0.83432897192878341, 1.0, 1.0]
        self.assertEqual(c2, list(mutated[2].genes))
