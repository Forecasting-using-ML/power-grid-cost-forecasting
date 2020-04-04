"""Methods for validating neural models in keras."""


def validate(
    model: 'keras.Model',
    X: 'np.ndarray',
    y: 'np.ndarray',
    is_fitting: bool=False,
    epochs: int=100,
    batch_size: int=100
) -> float:
    """
    Validate the model on a dataset.

    Args:
        model:
        X: the x values to fit the model with
        y: the y values to fit the model with
        is_fitting: whether the model should fit data i.e. train with back prop
            (default False) this will slow things down significantly, but
            increase accuracy
        epochs: the number of neural training epochs if fitting (default 100)
        batch_size: the training batch size if fitting (default 100)

    Returns:
        the validation accuracy of the given model

    """
    if is_fitting:
        # fit the model with the appropriate data
        model.fit(X, y,
            epochs=epochs,
            batch_size=batch_size,
            callbacks=None,
            verbose=False,
        )
    # evaluate the model's accuracy
    return model.evaluate(X, y, verbose=0)[1]


# explicitly define the outward facing API of this module
__all__ = [
    validate.__name__,
]
