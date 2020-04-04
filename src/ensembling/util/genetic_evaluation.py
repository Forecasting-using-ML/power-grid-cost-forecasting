"""A method for evaluating a set of genes representing neural net weights."""
from typing import Callable
from .model_analysis import flattened_weight_indecies
from .model_validation import validate


def build_evaluation(
    build_model: Callable,
    X: 'np.ndarray',
    y: 'np.ndarray',
    **kwargs: dict
) -> Callable:
    """
    Build and return an evaluation method for the given data and parameters.

    Args:
        build_model: a method that builds and returns a new Keras model
        X: the x values to fit
        y: the y values to fit
        **kwargs: additional keyword arguments for the validation method

    Returns:
        a callable evaluation method for a given model

    """
    # build the vector mapping for the weights
    vector_mapping = flattened_weight_indecies(build_model())
    # build the evaluation method

    def evaluate(genes: list) -> float:
        """
        Evaluate a set of weights for a neural model.

        Args:
            genes: the vector of weights to evaluate

        Returns:
            the fitness of the gene set based on the validation score

        """
        # build a new model to evaluate the genes
        model = build_model()
        # extract the layers that have weights
        layers = [l for l in model.layers if len(l.get_weights()) > 0]
        # iterate over the layers to adjust the weights
        for index, layer in enumerate(layers):
            # set the weights for the layer based on the vector mapping
            layer.set_weights([
                genes[vector_mapping[0][2 * index][0]:vector_mapping[0][2 * index][1]].reshape(vector_mapping[1][2 * index]),
                genes[vector_mapping[0][2 * index + 1][0]:vector_mapping[0][2 * index + 1][1]].reshape(vector_mapping[1][2 * index + 1])
            ])
        # return the validation
        return validate(model, X, y, **kwargs)

    return evaluate


# explicitly define the outward facing API of this module
__all__ = [build_evaluation.__name__]
