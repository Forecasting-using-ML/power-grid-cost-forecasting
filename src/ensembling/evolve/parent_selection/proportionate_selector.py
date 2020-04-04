"""
This module contains a class for proportionate parent selection.

The proportionate selector is susceptible to:
*   the super individual problem
*   loss of selection pressure as the algorithm converges
"""
from typing import Union
from numpy import ndarray, sum, random
from .parent_selector import ParentSelector


class ProportionateSelector(ParentSelector):
    """A class for performing proportionate parent selection."""

    def select(self, population: Union[list, ndarray], maximize=True):
        """
        Select a subset from the population.

        Args:
            population: the list of Chromosomes to select from
            maximize: whether to maxmimize or minimize fitness (default True)
        """
        # call super to check the super parameters
        super(ProportionateSelector, self).select(population)
        # score every individual in the population
        scores = [individual.fitness for individual in population]
        # if the score is 0, they have equal chances
        if sum(scores) == 0:
            return random.choice(population, size=self.size, replace=self.replace)
        # generate probabilities as the proportion of score to total score
        probablities = scores / sum(scores)
        # if we're minimizing we can just invert the probabilities about 1
        if not maximize:
            probablities = 1 - probablities
        # if the probabilities have converged such that there is a 1, numpy will
        # raise an error. instead use random choice, TODO: assess the proper
        # move here. error? return?
        if 1 in probablities:
            return random.choice(population, size=self.size, replace=self.replace)
        # return the results from the numpy choice function
        return random.choice(population, size=self.size, replace=self.replace, p=probablities)


# explicitly export classes
__all__ = [
    'ProportionateSelector'
]
