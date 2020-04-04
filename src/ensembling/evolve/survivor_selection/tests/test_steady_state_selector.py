"""A module with test code for the mu_mu_selector module."""
from unittest import TestCase
from ..steady_state_selector import *


#
# MARK: init
#


class init_ShouldRaiseErrorOnMissingParameters0(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            SteadyStateSurvivorSelector()


class init_ShouldRaiseErrorOnInvalidParameters0(TestCase):
    def test(self):
        with self.assertRaises(TypeError):
            SteadyStateSurvivorSelector(size='asdf')


class init_ShouldInstantiate(TestCase):
    def test(self):
        SteadyStateSurvivorSelector(size=0)


#
# MARK: select(population, parents, children)
#


class T:
    def __init__(self, fitness):
        self.fitness = fitness
    def __repr__(self):
        return str(self.fitness)
    def __lt__(self, other):
        return self.fitness < other.fitness


class select_ShouldSelect(TestCase):
    def test(self):
        sel = SteadyStateSurvivorSelector(size=1)
        expected = [3, 2, 0]
        p = sel.select([T(1), T(2), T(3)], [T(2), T(3)], [T(0)], True)
        for person, fitness in zip(p, expected):
            self.assertEqual(fitness, person.fitness)
