"""This module contains the unform crossover procreator class."""
from typing import List, Union
from numpy import ndarray, random
from evolve.population import Chromosome
from .procreator import Procreator


class UniformCrossoverProcreator(Procreator):
    """Uniform Crossover crossover on binary parents."""

    def __init__(self, probability=0.5):
        """
        Initialize a new uniform crossover procreator.

        Args:
            probability: the selection probability for the left parent
                         (default 0.5)
                         Note: the right parent will always have
                                P = 1 - probability
        """
        if not isinstance(probability, (int, float)):
            raise TypeError('probability must be of type: float, int')
        if probability < 0 or probability > 1:
            raise ValueError('probability must be in the range: [0, 1]')
        self.probability = probability

    def __repr__(self):
        """Return a string representation of this object."""
        return '{}(probability={})'.format(self.__class__.__name__, self.probability)

    def procreate(self, parents: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """
        Return a list of new children generated using uniform crossover.

        Args:
            parents: the list of parents to select genes from

        Returns: a list of new children
        """
        super(UniformCrossoverProcreator, self).procreate(parents)
        # generate the left index as a series of 1s and 0s with the 1s
        # distributed with probability P = probability
        left_index = random.choice(2, p=[self.probability, 1 - self.probability],
                                   size=len(parents[0].genes))
        # the right index is the inverse (probablity) of the left index
        right_index = 1 - left_index
        # multiplying the indecies 0s out the removed genes from either side
        # then adding these two vectors gives the child 
        return [parents[0].copy(genes=(parents[0].genes * left_index) + (parents[1].genes * right_index))]


# explicitly specify exports
__all__ = [
    'UniformCrossoverProcreator'
]
