"""This module contains the blend crossover procreator class."""
from typing import List, Union
from numpy import ndarray
from evolve.population import Chromosome
from .procreator import Procreator


class BlendCrossoverProcreator(Procreator):
    """This class performs blend crossover on parents."""

    def procreate(self, parents: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """
        Return a list of new children generated from a list of parents.

        Args:
            parents: the list of parents to select genes from

        Returns: a list of new children
        """
        super(BlendCrossoverProcreator, self).procreate(parents)


# explicitly specify exports
__all__ = [
    'BlendCrossoverProcreator'
]
