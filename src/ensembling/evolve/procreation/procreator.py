"""This module contains the crossover procreator abstract base class."""
from typing import List, Union
from abc import abstractmethod
from numpy import ndarray
from evolve.population import Chromosome


class Procreator:
    """This class is an abstract base class for crossover procreators."""

    def __repr__(self):
        """Return a string representation of this object."""
        return '{}()'.format(self.__class__.__name__)

    @abstractmethod
    def procreate(self, parents: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """
        Return a list of new children generated from a list of parents.

        Args:
            parents: the list of parents to select genes from

        Returns: a list of new children
        """
        # make sure the parents collection is the right type
        if not isinstance(parents, (list, ndarray)):
            raise TypeError('parents should be in datastructure: list, ndarray')
        # verify that there are at least 2 parents
        if len(parents) < 2:
            raise ValueError('crossovers must have at least 2 parents')
        # return the input, this is abstract
        return parents


# explicitly specify exports
__all__ = [
    'Procreator'
]
