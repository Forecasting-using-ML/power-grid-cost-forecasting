"""This module contains the realcoded mutation procreator class."""
from numpy import array
from numpy.random import random_sample
from .mutator import Mutator


class RealCodedMutationProcreator(Mutator):
    """This class performs realcoded mutation on parents."""

    def __init__(self, mutation_rate: float, random_state=(0, 1)):
        """
        Intanstiate a new real coded mutation procreator.

        Args:
            mutation_rate: the mutation rate for the procreator
            random_state: the range of random states to generate numbers in
        """
        super(RealCodedMutationProcreator, self).__init__(mutation_rate)
        if not isinstance (random_state, tuple) or len(random_state) < 2:
            raise TypeError('random_state should be a tuple of lowe and upper bounds. i.e. (0, 1)')
        self.low = random_state[0]
        self.high = random_state[1]

    def __repr__(self):
        """Return a string representation of this object."""
        template = '{}(mutation_rate={}, random_state=({}, {}))'
        return template.format(self.__class__.__name__,
                               self.mutation_rate,
                               self.low, self.high)

    @property
    def range(self):
        """Return the randomness range for the values"""
        return self.high - self.low

    def mutate(self, individual, inplace=False):
        """Return a mutated copy of the individual."""
        # super type checks individual and inplace
        super(RealCodedMutationProcreator, self).mutate(individual, inplace)
        # if it's a list or array, iterate over all the items
        if isinstance(individual, list):
            return [self.mutate(_ind, inplace=inplace) for _ind in individual]
        # create a copy if not in place
        if not inplace:
            individual = individual.copy()
        # get the indexes of genes to randomize
        randomize = array([random_sample() < self.mutation_rate for _ in range(individual.size)])
        # randomize the genes accordingly, use the sum of booleans to determine
        # random outputs to calculate
        individual.genes[randomize] = self.low + random_sample(randomize.sum()) * self.range
        return individual


# explicitly specify exports
__all__ = [
    'RealCodedMutationProcreator'
]
