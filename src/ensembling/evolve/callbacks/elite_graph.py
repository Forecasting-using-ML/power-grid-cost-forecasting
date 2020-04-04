"""A graph utility for showing the progress of an elite during a GA."""
from matplotlib import pyplot as plt
from IPython import display


class EliteGraph(object):
    """
    A class for graphing the progress of the elites in a population.

    Usage:
        # default for Jupyter environment
        graph = EliteGraph()
        # non jupyter environment
        graph = EliteGraph(is_jupyter=False)
        # minimize instead of maximize (can use mean, max, etc.)
        graph = EliteGraph(optimal=min)

        # usage in a GA callback
        GeneticAlgorithm(...).evolve(..., callback=graph.update)
    """

    def __init__(self,
        is_jupyter: bool=True,
        xlabel: str='Generation',
        ylabel: str='Fitness',
        optimal=max
    ) -> None:
        """
        Initialize a new elite graph.

        Args:
            is_jupyter: whether using a jupyter notebook (default True)
            xlabel: the string to display on the x axis (default 'Generation')
            ylabel: the string to display on the y axis (default 'Fitness')
            optimal: the function to determine optimal scores (default max)

        Returns:
            None

        """
        if not isinstance(is_jupyter, (bool)):
            raise TypeError('is_jupyter must be of type: bool')
        if not isinstance(xlabel, str):
            raise TypeError('xlabel must be of type: str')
        if not isinstance(ylabel, str):
            raise TypeError('ylabel must be of type: str')
        # make sure optimal accepts the right signature
        try:
            optimal([0, 1])
        except Exception:
            raise TypeError('optimal must be a method with signature: optimal(arr: Union[list, np.ndarray])')
        self.is_jupyter = is_jupyter
        self.fitnesses = []
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.optimal = optimal

    def __call__(self, population: list, generation: int) -> None:
        """
        Add the elite individuals fitness to the the plot.

        Args:
            population: the population of individuals representing a generation
            generations: the number of generations that have passed

        Returns:
            None

        """
        # add the best fitness to the list
        self.fitnesses.append(self.optimal([ind.fitness for ind in population]))
        # update the plot with the fitnesses
        plt.plot(self.fitnesses)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.is_jupyter:
            # clear the jupyter output to animate the plot
            display.clear_output(wait=True)
        plt.show()


# explicitly define the outward facing API of this module
__all__ = [
    EliteGraph.__name__
]
