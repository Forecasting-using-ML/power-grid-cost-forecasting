"""A method to return the number of weights in a keras model."""


def shapes_of_weights_in(model) -> int:
    """
    Return the shapes of weights in a keras model.

    Args:
        model: the model to count weights in

    Returns: a list of the weight matrix shape tuples in the model
    """
    shapes = []
    # iterate over all the layers in the model
    for layer in model.layers:
        # get the shapes of the weights and biases
        for weights in layer.get_weights():
            shapes.append(weights.shape)
    return shapes


def number_of_weights_in(model) -> int:
    """
    Return the total number of weights in a keras model.

    Args:
        model: the model to count weights in

    Returns: an integer count of the number of weights in the model
    """
    total_weights = 0
    # iterate over the tuple (output weights, biases)
    for shape in shapes_of_weights_in(model):
        # if there is one item in the shape, use just that
        if len(shape) == 1:
            total_weights += shape[0]
        # otherwise multiply the items together (total number in a matrix)
        else:
            total_weights += shape[0] * shape[1]
    return total_weights


def flattened_weight_indecies(model) -> tuple:
    """
    Return a mapping of a vector to a neural net's weight model

    Args:
        model: the keras model to design a mapping for

    Returns: a tuple with the indexes and shapes
    """
    base = 0
    indexes = []
    shapes = shapes_of_weights_in(model)
    for shape in shapes_of_weights_in(model):
        if len(shape) == 1:
            indexes.append((base, base + shape[0]))
            base += shape[0]
        else:
            indexes.append((base, base + shape[0] * shape[1]))
            base += shape[0] * shape[1]
    return indexes, shapes
