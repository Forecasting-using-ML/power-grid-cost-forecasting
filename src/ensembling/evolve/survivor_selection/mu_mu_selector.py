"""A module containing an implementation of Mu Mu replacement."""
from typing import Union, List
from numpy import ndarray
from evolve.population import Chromosome
from .survivor_selector import SurvivorSelector


class MuMuSurvivorSelector(SurvivorSelector):
    """A class for selecting survivors using (u,u) replacement."""

    def __init__(self, mu: int):
        """Intanstiate a new (mu, mu) selector."""
        raise NotImplementedError('not implemented yet!')
        if not isinstance(mu, (float, int)):
            raise TypeError('mu must be of type: float, int')
        self.mu = int(mu)

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
        population.sort(key=lambda ind: ind.fitness, reverse=maximize)
        # TODO: was mistakenly doing steady state here, this needs fixed
        # for _ in range(self.mu):
        #     population.pop()
        # population += children


# explicitly specify exports
__all__ = [
    'MuMuSurvivorSelector'
]
