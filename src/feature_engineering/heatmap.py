"""A method for generating a heat map from a dataframe."""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def heatmap(
    df: pd.DataFrame,
    fill_value: int=-1,
    figsize: tuple=(6, 6),
    x_rotation: int=270,
    cmap: mpl.colors.LinearSegmentedColormap=mpl.cm.Blues,
) -> mpl.figure.Figure:
    """
    Build a heat-map of the given DataFrame columns.

    Args:
        df: the DataFrame to generate a heat map from
        fill_value: the value to fill in NaN with
        figsize: the size of the figure to render
        x_rotation: the degree to rotate x-axis labels by
        cmap: the matplotlib color map for generating heat

    Returns:
        the generated matplotlib figure

    """
    # create a figure of the given size
    fig = plt.figure(figsize=figsize)
    # set the plot as a heat-map with the correlation coefficient as z-value
    plt.pcolor(df.corr().fillna(fill_value), cmap=cmap)
    # set the x and y ticks to half way between each integer (covers a square)
    plt.yticks(np.arange(0.5, len(df.columns), 1), df.columns)
    plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
    # rotate the x-axis labels to be more readable
    _, labels = plt.xticks()
    plt.setp(labels, rotation=x_rotation)

    return fig


# explicitly define the outward facing API of this module
__all__ = [heatmap.__name__]
