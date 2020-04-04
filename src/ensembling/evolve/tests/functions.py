"""This module contains functions for testing evolutionary algorithms."""
from math import sin


# MARK: Shaffer's F6 Function
#                  sin**2(sqrt(x**2 + y**2)) - 0.5
# f6(x,y) = 0.5 + ---------------------------------
#                   (1.0 + 0.001(x**2 + y**2))**2
# where:
# *   -100 <= x <= 100


def _f6_numerator(x: float, y: float) -> float:
    """Return the numerator of the f6 function for an x,y pairing."""
    return sin((x**2 + y**2)**(0.5))**2 - 0.5


def _f6_denominator(x: float, y: float) -> float:
    """Return the denominator of the f6 function fo an x,y pairing."""
    return (1.0 + 0.001 * (x**2 + y**2))**2


def f6(x: float, y: float) -> float:
    """Return the f6 function for an x,y pairing."""
    if isinstance(x, list) and isinstance(y, list):
        return [f6(_x, _y) for _x, _y in zip(x, y)]
    return 0.5 + (_f6_numerator(x, y) / _f6_denominator(x, y))


# MARK: Exports
# export the appropriate functions
__all__ = [
    f6.__name__
]
