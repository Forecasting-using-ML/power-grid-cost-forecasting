"""This module contains a class representing an abstract chromosome."""
from typing import Callable
import numpy as np


class Chromosome:
    """
    This class represents a chromosome in a genetic optimization.

    Once created, the evaluation function and size of the chromosome are
    immutable. This is to ensure that chromosomes aren't mutated to an illegal
    state accidentally by the external api. _size and _evaluate should not be
    accessed, or updated by external code.
    """

    def __init__(self, size: int, evaluate: Callable, **kwargs):
        """
        Initialize a new chromosome of a given size.

        Args:
            size: the size of the chromosome (default 0)
            evaluate: the evaluation function for the fitness (default None)
            kwargs: keyword arguments that subclasses might use
        """
        # check the validity of the size parameter
        if not isinstance(size, (int, float)):
            raise ValueError('size should be a numeric value like: int, float')
        elif size < 0:
            raise ValueError('cannot create chromosome with a negative size')
        self._size = size
        # validate the evaluation function
        if not callable(evaluate):
            raise ValueError('evaluate must be a callable (method/function)')
        self._evaluate = evaluate
        # setup the genes instance variable
        self.genes = None
        # setup the cache
        self._cached_fitness = None

    def __lt__(self, other):
        """
        Compare this instance to another to see if it is less than the other.

        Args:
            other: the other chromosome to compare against

        Returns: true if this chromosome has a lesser fitness than other
        """
        return self.fitness < other.fitness

    @property
    def size(self) -> int:
        """Return the size of the chromosome."""
        return self._size

    @property
    def evaluate(self) -> Callable[[np.array], float]:
        """Return the evaluation function for the chromosome."""
        return self._evaluate

    @property
    def fitness(self) -> float:
        """Return the fitness of the gene from the evaluation function."""
        if self._cached_fitness is None:
            self._cached_fitness = self._evaluate(self.genes)
        return self._cached_fitness
        return self._evaluate(self.genes)

    def copy(self):
        """Return a copy of this chromosome."""
        return Chromosome(size=self.size, evaluate=self.evaluate)


# explicitly export the classes
__all__ = [
    'Chromosome'
]
