from __future__ import annotations
from typing import Union

import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from geom.shapes import BaseShape
from geom.draw_pyplot import Axes, remove_splines


class Container:
    def __init__(self, shapes: list[BaseShape] = None):
        self.shapes = [] if shapes is None else shapes

    def rotate(self, phi: float) -> Container:
        [shape.rotate(phi) for shape in self.shapes]
        return self

    def translate(self, vec: np.ndarray) -> Container:
        [shape.translate(vec) for shape in self.shapes]
        return self

    def draw(
        self, ax: Axes = None, **kwargs
    ) -> Union[tuple[None, None], tuple[Figure, Axes]]:
        ret = (None, None)
        if ax is None:
            fig, ax = plt.subplots(1, 1, figsize=(6, 6))
            remove_splines(ax)
            ret = (fig, ax)
        [shape.draw(ax=ax, **kwargs) for shape in self.shapes]
        return ret
