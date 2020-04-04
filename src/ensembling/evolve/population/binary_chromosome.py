"""This module contains a class representing a binary chromosome."""
from typing import Callable
from numpy import ones, zeros, array
from numpy.random import randint
from .chromosome import Chromosome


class BinaryChromosome(Chromosome):
    """This class represents a binary encoded chromosome."""

    # the valid initial state options for how to initialize the chromosome
    INITIAL_STATES = ['zeros', 'ones', 'random']

    def __init__(self, size: int, evaluate: Callable, initial_state: str='random'):
        """Initialize a new chromosome of a given size.

        Args:
            size: the size of the chromosome (default 0)
            intial_state: the initial state of the chromosome (default 'random')
                * can be 'zeros', 'ones', or 'random'
        """
        super(BinaryChromosome, self).__init__(size, evaluate)
        # setup the initial state of the chromosome
        if initial_state == self.INITIAL_STATES[0]:
            # initialize with all 0s
            self.genes = zeros(size).astype(int)
        elif initial_state == self.INITIAL_STATES[1]:
            # intializw with all 1s
            self.genes = ones(size).astype(int)
        elif initial_state == self.INITIAL_STATES[2]:
            # initialize with random values in {0, 1}
            self.genes = randint(low=0, high=2, size=size).astype(int)
        # invalid initial state, raise error
        else:
            raise ValueError('initial_state must be one of: {}'.format(self.INITIAL_STATES))

    def __repr__(self) -> str:
        """Return a string represtation of this object"""
        return str(self.genes)

    def copy(self, genes='self'):
        """
        Return a copy of this chromosome.

        Args:
            genes: the new genes for the copy if any. (default 'self') i.e.
                   this chromosomes current genes

        Returns: a copy of this chromosome with possibly new genes (child)
        """
        _copy = BinaryChromosome(size=self.size,
                                 evaluate=self.evaluate,
                                 initial_state='zeros')
        # if it's self, us this chromosomes genes (default)
        if isinstance(genes, str) and genes == 'self':
            _copy.genes = self.genes
        # if none, do nothing (i.e. use zeros)
        elif genes is None:
            pass
        # make sure the genes are good to use
        elif len(genes) != _copy.size:
            raise ValueError('passed genes of incorrect size')
        # otherwise copy the genes
        else:
            _copy.genes = array(genes)
        return _copy


# explicitly export the classes
__all__ = [
    'BinaryChromosome'
]
