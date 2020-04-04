"""A module containing an implementation of steady state replacement."""
from typing import Union, List
from numpy import ndarray
from numba import jit
from evolve.population import Chromosome
from .survivor_selector import SurvivorSelector


class SteadyStateSurvivorSelector(SurvivorSelector):
    """A class for selecting survivors using steady state replacement."""

    def __init__(self, size: int):
        """Intanstiate a new steady state selector."""
        if not isinstance(size, (float, int)):
            # size must be a number, but isnt. raise an error
            raise TypeError('size must be of type: float, int')
        self.size = int(size)

    def __repr__(self):
        """Return a string representation of this object."""
        return '{}(size={})'.format(self.__class__.__name__, self.size)

    def select(self,
               population: Union[List[Chromosome], ndarray],
               parents: Union[List[Chromosome], ndarray],
               children: Union[List[Chromosome], ndarray],
               maximize=True) -> List[Chromosome]:
        """Return a population with the children replacing the parents.

        Args:
            population: the population to mutate
            parents: the population of parents that were selected
            children: the population of children that were generated
            maximize: whether to maxmimize the fitness scores

        Returns: A population with the some distribution of replacement
        """
        # sort the population from worst to best fitness score
        population.sort(reverse=maximize)
        # remove the worst individuals
        for _ in range(self.size):
            population.pop()
        # add the children to the population
        population += children
        # return the population
        return population


# explicitly specify exports
__all__ = [
    'SteadyStateSurvivorSelector'
]
