"""A regressor to combine multiple regressors together."""
import numpy as np


class BaggingRegressor(object):
    """An ensemble to combine several component learners together."""

    def __init__(self, regressors: list) -> None:
        """
        Initialize a new bagging ensemble with a set of regressors.

        Args:
            regressors: the estimators to combine into an ensemble

        Returns:
            None

        """
        if not isinstance(regressors, list):
            raise TypeError('regressors must be of type: list')
        self._regressors = regressors

    def __repr__(self) -> str:
        """Return an executable Python string of this object."""
        return '{}(regressors={})'.format(
            self.__class__.__name__,
            self._regressors,
        )

    @property
    def regressors(self):
        """Return the regressors used by this estimator."""
        return self._regressors

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'BaggingRegressor':
        """
        Fit the regressor with data.

        Args:
            X: The real-valued X values to fit
            y: The real-valued y value to fit

        Returns:
            this instance

        """
        for regressor in self.regressors:
            regressor.fit(X, y)

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict the value of a given input vector.

        Args:
            X: The real-valued X values to predict

        Returns:
            the predicted value for each feature vector in X

        """
        predictions = np.array([r.predict(X) for r in self.regressors])
        return np.mean(predictions, axis=0)


# explicitly define the outward facing API of this module
__all__ = [BaggingRegressor.__name__]
