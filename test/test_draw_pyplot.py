import numpy as np
import matplotlib.pyplot as plt

from geom import draw_pyplot


def test_draw():
    _, ax = plt.subplots(1, 1, figsize=(5, 5))
    draw_pyplot.draw(np.array([[0, 1], [1, 2]]), ax=ax, color="green", linestyle="--")


def test_remove_splines():
    _, ax = plt.subplots(1, 1, figsize=(5, 5))
    draw_pyplot.remove_splines(ax=ax)
