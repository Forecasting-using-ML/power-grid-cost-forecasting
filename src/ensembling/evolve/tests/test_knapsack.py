"""The 0-1 Knapsack Problem (Combinatorial Optimization)
This module solves the knapsack problem using evolutionary components.

## Given

*   a container of maximum capacity $c$
*   a set of items each with:
    *   a weight $w$
    *   a value $v$

## Determine

the subset of items that fits in the container such that the value of the
subset is maximized.
"""
from unittest import TestCase
from evolve import *
import numpy as np
from random import shuffle
from numpy.random import seed


class KnapsackTestCase(TestCase):

    # the number of items in the bag (also the size of the binary chromosome)
    SIZE = 1000
    # the base value for values of objects in the bag
    BASE_VALUE = 100
    # the base weight for generating weights randomly
    BASE_WEIGHT = 1000
    # reduces the bag size to a proportion of the mean value for each object.
    # allow random problems to generate (without this the bag would fit
    # everything)
    BAG_SIZE_FACTOR = 1 / 3
    # the size of the population
    POPULATION_SIZE = 20

    def setUp(self):
        """Setup the problem space."""
        # the value mapping for the objects
        self.VALUES = (np.random.random_sample(size=self.SIZE) * self.BASE_VALUE).astype(int)
        # the weight mapping for the objects
        self.WEIGHTS = (np.random.random_sample(size=self.SIZE) * self.BASE_WEIGHT).astype(int)
        # the sum of all the weights (total weight of all objects)
        self.WEIGHTS_SUM = np.sum(self.WEIGHTS)
        # the size of the bag based on the mean weight, number of items to select from,
        # and the bag size factor
        self.BAG_SIZE = int(self.SIZE * self.WEIGHTS.mean() * self.BAG_SIZE_FACTOR)

        # print('(scores)   V = \n{}'.format(self.VALUES))
        # print('(weights)  W = \n{}'.format(self.WEIGHTS))
        # print('(bag size) c = {}'.format(self.BAG_SIZE))

        factory = ChromosomeFactory(BinaryChromosome, self.SIZE,
                                    evaluate=self.evaluate,
                                    initial_state='random')
        self.population = factory.population(self.POPULATION_SIZE)

        print('initial population')
        print(max([ind.fitness for ind in self.population]))

    def evaluate(self, genes: np.array) -> float:
        """
        Evaluate the genes in a chromosome normalize about bagsize.

        Args:
            genes: the genes to decode and evauate

        Returns: the score. + if scored, - if overweight
        """
        # make sure the chromosome holds the contraint that the total weight is
        # less than the maximum weight
        if np.sum(genes * self.WEIGHTS) > self.BAG_SIZE:
            # use the weight normalized about 1 to weight the bagsize
            return self.BAG_SIZE * (1 - np.sum(genes * self.WEIGHTS) / self.WEIGHTS_SUM)
        # conditions have passed so we can score the items based on their values
        return np.sum(genes * self.VALUES) + self.BAG_SIZE


class test_0_SteadyStateSinglePoint(KnapsackTestCase):
    def test(self):
        seed(10)
        parent_selector = TournamentSelector(size=2, replace=False, individuals_per_tournament=3)
        procreator = NPointCrossoverProcreator(crossovers=1)
        mutator = BinaryMutationProcreator(mutation_rate=0.05)
        survivor_selector = SteadyStateSurvivorSelector(size=parent_selector.size)
        ga = GeneticAlgorithm(parent_selector, procreator, mutator, survivor_selector)
        ga_pop = ga.evolve(self.population, iterations=2000)
        # ga.fitness_metrics().plot().get_figure().savefig('./ssga.png')
        print('steady state population')
        print(max([ind.fitness for ind in ga_pop]))


class test_1_SteadyStateUniform(KnapsackTestCase):
    def test(self):
        seed(10)
        parent_selector = TournamentSelector(size=2, replace=False, individuals_per_tournament=3)
        procreator = UniformCrossoverProcreator()
        mutator = BinaryMutationProcreator(mutation_rate=0.05)
        survivor_selector = SteadyStateSurvivorSelector(size=1)
        ga = GeneticAlgorithm(parent_selector, procreator, mutator, survivor_selector)
        ga_pop = ga.evolve(self.population, iterations=2000)
        # ga.fitness_metrics().plot().get_figure().savefig('./ssga.png')
        print('steady state population')
        print(max([ind.fitness for ind in ga_pop]))


class test_1_Generational(KnapsackTestCase):
    def test(self):
        # generational replacement
        parent_selector = TournamentSelector(size=2, replace=False, individuals_per_tournament=3)
        procreator = NPointCrossoverProcreator(crossovers=1)
        mutator = BinaryMutationProcreator(mutation_rate=0.005)
        survivor_selector = GenerationalSurvivorSelector()
        ga = GeneticAlgorithm(parent_selector, procreator, mutator, survivor_selector)
        ga_pop = ga.evolve(self.population, iterations=2000)
        # ga.fitness_metrics().plot().get_figure().savefig('./gen.png')
        print('generational population')
        print(max([ind.fitness for ind in ga_pop]))
