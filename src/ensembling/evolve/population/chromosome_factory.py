"""This module contains a class for generating chromosome populations."""
from typing import Callable
from .chromosome import Chromosome


class ChromosomeFactory:
    """A class for generating new chromosomes."""

    def __init__(self,
                 chromosome_class: Chromosome,
                 chromosome_size: int,
                 evaluate: Callable,
                 initial_state: str = 'random'):
        """
        Initialize a new chromosome factory.

        Args:
            chromosome_class: the class of the chromosomes to create
            chromosome_size: the size of the chromsome
            initial_state: the initial state of the chromosomes
                           (default 'random')
            evaluate: the evaluation function for the chromosomes
                      (default None)
        """
        if not issubclass(chromosome_class, Chromosome):
            raise ValueError('chromosome_class must be a type of Chromosome')
        self.chromosome_class = chromosome_class
        if not isinstance(chromosome_size, (float, int)):
            raise ValueError('chromosome_size must be a numeric: float, int')
        self.chromosome_size = chromosome_size
        if not isinstance(initial_state, (str, tuple)):
            raise ValueError('initial_state must be of type: str, tuple')
        self.initial_state = initial_state
        if not isinstance(evaluate, Callable):
            raise ValueError('evaluate must be a callable method')
        self.evaluate = evaluate

    @property
    def next_individual(self):
        """Create and return a new individual."""
        return self.chromosome_class(size=self.chromosome_size,
                                     initial_state=self.initial_state,
                                     evaluate=self.evaluate)

    def population(self, size: int):
        """Return a population of new chromosomes a given size.

        Args:
            size: the number of individuals to generate
        """
        if not isinstance(size, (int, float)) or size < 0:
            raise ValueError('size must be a positive number')
        return [self.next_individual for i in range(0, size)]


# explicitly export the classes
__all__ = [
    'ChromosomeFactory'
]
