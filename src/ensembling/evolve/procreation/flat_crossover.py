"""BLX-0.0 (Flat, Radcliffe's) Crossover Procreator."""
from typing import List, Union
from numpy import ndarray, random
from evolve.population import Chromosome
from .procreator import Procreator


class FlatCrossoverProcreator(Procreator):
    """BLX-0.0 (Flat, Radcliffe's) Crossover Procreator."""

    def procreate(self, parents: Union[List[Chromosome], ndarray]) -> List[Chromosome]:
        """
        Return a list of new children generated using flat crossover.
        Note: flat crossover replaces each gene with a random number between
              the values of that gene in the parents

        Args:
            parents: the list of parents to select genes from

        Returns: a list of new children
        """
        super(FlatCrossoverProcreator, self).procreate(parents)
        return [parents[0].copy(genes=random.uniform(parents[0].genes, parents[1].genes))]


# explicitly specify exports
__all__ = [
    'FlatCrossoverProcreator'
]
