"""This module contains test code for the real-coded chromosome module."""
from unittest import TestCase
import numpy as np
from ..chromosome import Chromosome
from ..realcoded_chromosome import *


def arb():
    """an arbitrary method that does nothing"""
    pass


#
# MARK: __init__()
#


class init_ShouldBeSubclassOfChromosome(TestCase):
    def test(self):
        self.assertTrue(issubclass(RealCodedChromosome, Chromosome))


class init_ShouldCreateDefaultChromosome(TestCase):
    def test(self):
        self.assertIsInstance(RealCodedChromosome(0, arb), RealCodedChromosome)


class init_ShouldRaiseErrorOnInvalidInitialStateWrongType(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            RealCodedChromosome(0, arb, initial_state=0)


class init_ShouldRaiseErrorOnInvalidInitialState(TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            RealCodedChromosome(0, arb, initial_state='asdf')


class init_ShouldCreateChromosomeWithZeros(TestCase):
    def test(self):
        chrom = RealCodedChromosome(3, arb, initial_state='zeros')
        self.assertEqual(list(chrom.genes), [0, 0, 0])


class init_ShouldCreateChromosomeWithOnes(TestCase):
    def test(self):
        chrom = RealCodedChromosome(3, arb, initial_state='ones')
        self.assertEqual(list(chrom.genes), [1, 1, 1])


class init_ShouldCreateChromosomeWithRandoms(TestCase):
    def test(self):
        chrom = RealCodedChromosome(3, arb, initial_state=(5, 7))
        self.assertEqual(3, len(chrom.genes))
        for gene in chrom.genes:
            self.assertTrue(gene >= 5)
            self.assertTrue(gene <= 7)
