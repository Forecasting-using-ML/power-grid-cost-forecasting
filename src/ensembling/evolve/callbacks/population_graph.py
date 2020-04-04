"""A graphical utility for plotting the progress of a population during a GA."""
import numpy as np
from matplotlib import pyplot as plt
from IPython import display


class PopulationGraph(object):
    """
    A class for graphing the progress of a population.

    Usage:
        # default for Jupyter environment
        graph = PopulationGraph()
        # non jupyter environment
        graph = PopulationGraph(is_jupyter=False)

        # usage in a GA callback
        GeneticAlgorithm(...).evolve(..., callback=graph.update)
    """

    def __init__(self,
        is_jupyter: bool=True,
        xlabel: str='Generation',
        ylabel: str='Fitness'
    ) -> None:
        """
        Initialize a new population graph.

        Args:
            is_jupyter: whether using a jupyter notebook (default True)
            xlabel: the string to display on the x axis (default 'Generation')
            ylabel: the string to display on the y axis (default 'Fitness')

        Returns:
            None

        """
        if not isinstance(is_jupyter, (bool)):
            raise TypeError('is_jupyter must be of type: bool')
        if not isinstance(xlabel, str):
            raise TypeError('xlabel must be of type: str')
        if not isinstance(ylabel, str):
            raise TypeError('ylabel must be of type: str')
        self.is_jupyter = is_jupyter
        self.xlabel = xlabel
        self.ylabel = ylabel
        # initialize the list of fitnesses
        self.fitnesses = []

    def __call__(self, population: list, generation: int) -> None:
        """
        Add the elite individuals fitness to the the plot.

        Args:
            population: the population of individuals representing a generation
            generations: the number of generations that have passed

        Returns:
            None

        """
        # add all the fitnesses to the list
        self.fitnesses.append([ind.fitness for ind in population])
        indexes = list(np.hstack([[index] * len(fv) for index, fv in enumerate(self.fitnesses)]))

        plt.plot(indexes, list(np.hstack(self.fitnesses).reshape(len(indexes), -1)), '.')
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.is_jupyter:
            # clear the jupyter output to animate the plot
            display.clear_output(wait=True)
        plt.show()


# export the classes manually to keep internal garbage from being exported
__all__ = [
    PopulationGraph.__name__
]
