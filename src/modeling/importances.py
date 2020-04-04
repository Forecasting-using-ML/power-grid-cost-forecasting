"""A method for plotting importances of splits in decision tree ensembles."""
import pandas as pd
import matplotlib.pyplot as plt


def importances(
    model, dataset,
    threshold: float=-0.001,
    figsize: tuple=(7, 7)
):
    """
    Plot the importance rankings for a given classifier

    Args:
        model: the classifier providing a `feature_importances_` attribute
        dataset: the dataset the classifier models
        threshold: the minimum importance ranking to be included on the plot
        figsize: the size of the figure to render as a tuple (W, H)

    Returns:
        a matplotlib figure

    """
    # create a series of importances for the dataset variables
    series = pd.Series(model.feature_importances_, index=dataset.columns)
    # clear out values beneath a certain threshold
    series = series[series > threshold]
    # sort the values in descending order
    series.sort_values(inplace=True, ascending=False)
    # plot the values as a horizontal bar graph (easy to read)
    ax = series.plot(kind='barh', figsize=figsize)
    # setup labels
    ax.set_ylabel('Feature')
    ax.set_xlabel('Importance Ranking')
    # force a tighter layout
    plt.tight_layout()
    # return the figure associated with the axes object
    return ax.get_figure()


__all__ = [importances.__name__]
