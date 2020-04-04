"""
This module contains a class for tournament parent selection.

*   selection pressure increases and decreases with k
"""
from typing import Union
from numpy import ndarray, random
from .parent_selector import ParentSelector


class TournamentSelector(ParentSelector):
    """A class for performing tournament parent selection."""

    def __init__(self,
                 size: int = None,
                 replace: bool = True,
                 individuals_per_tournament: int = None):
        """
        Initialize a new tournament selector.

        Args:
            size: the size of the sub population to select
            replace: whether to allow replacement when selecting
            individuals_per_tournament: the number of individuals to select
                                        from for each tournment (default None)
        """
        # call super to verify and asssign super parameters
        super(TournamentSelector, self).__init__(size, replace)
        # verify the individuals_per_tournament parameter
        if individuals_per_tournament is None:
            pass
        elif not isinstance(individuals_per_tournament, int):
            raise TypeError('individuals_per_tournament must be of type: None, int')
        elif individuals_per_tournament < 0:
            raise ValueError('individuals_per_tournament must be >= 0')
        # set the individuals_per_tournament to self
        self.individuals_per_tournament = individuals_per_tournament

    def __repr__(self):
        """Return a string representation of this object."""
        return '{}(size={}, replace={}, individuals_per_tournament={})'.format(*[
            self.__class__.__name__,
            self.size,
            self.replace,
            self.individuals_per_tournament
        ])

    def _select_finalists(self, population: Union[list, ndarray], maximize=True):
        """
        Select and return a set of finalists from a population.

        Args:
            population: the population to select finalists from
            maximize: whether to maxmimize or minimize fitness (default True)

        Returns: a subset of the population of size
                 self.individuals_per_tournament sorted by fitness
        """
        if self.individuals_per_tournament is None:
            participants = population
        else:
            participants = random.choice(population,
                                         size=self.individuals_per_tournament,
                                         replace=self.replace)
        return sorted(participants, key=lambda ind: ind.fitness, reverse=maximize)

    def select(self, population: Union[list, ndarray], maximize=True):
        """
        Select a subset of tournament winners from the population.

        Args:
            population: the list of Chromosomes to select from
            maximize: whether to maxmimize or minimize fitness (default True)

        Returns: a subset of the winners of the self.size tournments
        """
        # call super to check the super parameters
        super(TournamentSelector, self).select(population)
        # if the size is 1 or none (all) then no loop necessary
        if self.size is None or self.size == 1:
            return self._select_finalists(population)[:self.size]
        # collect a set of winners of a certain size
        winners = []
        while len(winners) < self.size:
            # select a winner
            winner = self._select_finalists(population, maximize)[0]
            # if replacement is off and the winner is already selected, continu
            if not self.replace and winner in winners:
                continue
            winners.append(winner)
        return winners


# explicitly export classes
__all__ = [
    'TournamentSelector'
]
