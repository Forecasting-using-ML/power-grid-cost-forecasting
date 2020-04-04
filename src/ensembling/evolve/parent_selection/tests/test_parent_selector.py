"""This module tests the parent_selector module."""
import unittest
from numpy import array
from ..parent_selector import *


#
# MARK: Abstract Base Class
#


class ParentSelectorTestCase(unittest.TestCase):
    pass


#
# MARK: __init__()
#


class ShouldInstantiateParentSelector(ParentSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(ParentSelector(), ParentSelector))


class ShouldRaiseErrorOnInvalidSizeType(ParentSelectorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            ParentSelector(size='asdf')


class ShouldRaiseErrorOnInvalidSizeBelowBounds(ParentSelectorTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):
            ParentSelector(size=-1)


class ShouldInstantiateParentSelectorSize0(ParentSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(ParentSelector(size=0), ParentSelector))


class ShouldRaiseErrorOnInvalidReplaceType(ParentSelectorTestCase):
    def runTest(self):
        with self.assertRaises(TypeError):
            ParentSelector(replace='asdf')


class ShouldInstantiateParentSelectorReplaceTrue(ParentSelectorTestCase):
    def runTest(self):
        self.assertTrue(isinstance(ParentSelector(replace=True), ParentSelector))


#
# MARK: select(population)
#


class ShouldRaiseErrorOnInvalidPopulationWrongType(ParentSelectorTestCase):
    def runTest(self):
        sel = ParentSelector()
        with self.assertRaises(TypeError):
            sel.select('asdfasdfasdf')


class ShouldNotRaiseErrorOnValidPopulationList(ParentSelectorTestCase):
    def runTest(self):
        sel = ParentSelector()
        self.assertIsNone(sel.select([]))


class ShouldNotRaiseErrorOnValidPopulationArray(ParentSelectorTestCase):
    def runTest(self):
        sel = ParentSelector()
        self.assertIsNone(sel.select(array([])))
