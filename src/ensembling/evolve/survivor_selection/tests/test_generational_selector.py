"""A module with test code for the generational_selector module."""
from unittest import TestCase
from ..generational_selector import *


#
# MARK: init
#


class init_ShouldInstantiate(TestCase):
    def test(self):
        GenerationalSurvivorSelector()


#
# MARK: select(population, parents, children)
#
