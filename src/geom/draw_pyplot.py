from matplotlib.axes import Axes
import numpy as np


def draw(array: np.array, ax: Axes, **kwargs) -> None:
    ax.plot(*array.T, **kwargs)


def remove_splines(ax: Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    # ax.spines["bottom"].set_alpha(alpha)
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
