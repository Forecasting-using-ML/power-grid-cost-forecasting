"""Test cases for the GeneticAlgorithm class."""
from unittest import TestCase
from evolve import *


#
# MARK: init
#


class init_ShouldRaiseErrorOnMissingParameters0(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm()


class init_ShouldRaiseErrorOnMissingParameters1(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(ParentSelector())


class init_ShouldRaiseErrorOnMissingParameters2(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(ParentSelector(),
                             Procreator())


class init_ShouldRaiseErrorOnMissingParameters3(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(ParentSelector(),
                             Procreator(),
                             Mutator(mutation_rate=1))


class init_ShouldInitializeOject(TestCase):
    def test(self):
        GeneticAlgorithm(ParentSelector(),
                         Procreator(),
                         Mutator(mutation_rate=1),
                         SurvivorSelector())


class init_ShouldInitializeOjectWitNoMutator(TestCase):
    def test(self):
        GeneticAlgorithm(ParentSelector(),
                         Procreator(),
                         None,
                         SurvivorSelector())


class init_ShouldRaiseErrorOnInvalidType0(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm('asdf',
                             Procreator(),
                             Mutator(mutation_rate=1),
                             SurvivorSelector())


class init_ShouldRaiseErrorOnInvalidType1(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(ParentSelector(),
                             'asdf',
                             Mutator(mutation_rate=1),
                             SurvivorSelector())


class init_ShouldRaiseErrorOnInvalidType2(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(ParentSelector(),
                             Procreator(),
                             'asdf',
                             SurvivorSelector())


class init_ShouldRaiseErrorOnInvalidType3(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            GeneticAlgorithm(ParentSelector(),
                             Procreator(),
                             Mutator(mutation_rate=1),
                             'asdf')

#
# MARK: evolve
#
