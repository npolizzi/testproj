# -*- coding: utf-8 -*-
"""Test Module for sphinx_rtd_theme."""

__all__ = ['func33', 'func32']

from random import uniform


def func33(a, b):
    """This function adds a and b. It
    can be used like so::

        ans = func23(1, 2)
        print(ans)

    :param a: a number
    :param b: a number

    """
    return uniform(a, b)


def func32(c, d):
    """This is unlike :func:`~.test2.func23` but
    not unlike it too.

    Parameters
    ----------
    c : int, float
        something about c here
    d : int, float
        something about d

    Returns
    -------
    int, float
        sum of c and d
    """
    a = c + d
    return a
