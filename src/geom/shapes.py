from __future__ import annotations
from itertools import zip_longest

import numpy as np

from geom.transformations import Transformations, Rotation, Translation
from geom.draw_pyplot import Axes, draw as draw_pyplot


class BaseShape:
    def __init__(self, **kwargs) -> None:
        self.trafos = Transformations()
        self.kwargs = kwargs

    def _f_x(self, t: float) -> float:
        raise NotImplementedError

    def _f_y(self, t: float) -> float:
        raise NotImplementedError

    def evaluate(self, t: float) -> tuple[float, float]:
        return (self._f_x(t), self._f_y(t))

    def to_array(self, n: int = 250, ts: np.ndarray = None) -> np.ndarray:
        if ts is None:
            ts = np.linspace(0, 1, n)
        return self.trafos(np.array([self.evaluate(t) for t in ts]))

    def rotate(self, phi: float) -> BaseShape:
        self.trafos.add(Rotation(phi))
        return self

    def translate(self, vec: np.ndarray) -> BaseShape:
        self.trafos.add(Translation(np.array(vec)))
        return self

    def draw(self, ax: Axes = None, **kwargs) -> None:
        draw_pyplot(self.to_array(), ax=ax, **{**kwargs, **self.kwargs})


class ArcEllipse(BaseShape):
    def __init__(
        self,
        loc: tuple[float, float],
        width: float,
        hight: float,
        phi0: float,
        phi1: float,
        **kwargs: dict,
    ) -> None:
        self.x = loc[0]
        self.y = loc[1]
        self.width = width
        self.hight = hight
        self.phi0 = phi0
        self.phi1 = phi1
        super().__init__(**kwargs)

    def _f_x(self, t: float) -> float:
        phi = self.phi0 + t * (self.phi1 - self.phi0)
        return self.x + self.width * np.cos(phi)

    def _f_y(self, t: float) -> float:
        phi = self.phi0 + t * (self.phi1 - self.phi0)
        return self.y + self.hight * np.sin(phi)


class Ellipse(ArcEllipse):
    def __init__(
        self, loc: tuple[float, float], width: float, hight: float, **kwargs: dict
    ) -> None:
        super().__init__(
            loc=loc, width=width, hight=hight, phi0=0.0, phi1=2 * np.pi, **kwargs
        )


class ArcCircle(ArcEllipse):
    def __init__(
        self,
        loc: tuple[float, float],
        radius: float,
        phi0: float,
        phi1: float,
        **kwargs: dict,
    ) -> None:
        super().__init__(
            loc=loc, width=radius, hight=radius, phi0=phi0, phi1=phi1, **kwargs
        )


class Circle(ArcCircle):
    def __init__(self, loc: tuple[float, float], radius: float, **kwargs: dict) -> None:
        super().__init__(loc=loc, radius=radius, phi0=0.0, phi1=2 * np.pi, **kwargs)


class Polygon(BaseShape):
    def __init__(self, locs: list[tuple[float, float]], **kwargs: dict) -> None:
        self.locs = np.array(locs)

        pairs = zip_longest(self.locs, self.locs[1:], fillvalue=self.locs[0])
        self.segment_ends_in_t = np.cumsum([np.linalg.norm(s - e) for s, e in pairs])
        self.segment_ends_in_t /= self.segment_ends_in_t.max()
        super().__init__(**kwargs)

    def _interpolate(self, t: float, dim: int) -> float:
        ind = np.where(self.segment_ends_in_t >= t)[0][0]
        start_t = 0 if ind == 0 else self.segment_ends_in_t[ind - 1]
        end_t = self.segment_ends_in_t[ind]
        if ind < len(self.segment_ends_in_t) - 1:
            start_loc, end_loc = self.locs[ind : ind + 2, dim]  # +2 excusive
        else:  # last segment combines end point to the first point
            start_loc, end_loc = self.locs[-1, dim], self.locs[0, dim]
        return start_loc + (t - start_t) / (end_t - start_t) * (end_loc - start_loc)

    def _f_x(self, t: float) -> float:
        return self._interpolate(t, dim=0)

    def _f_y(self, t: float) -> float:
        return self._interpolate(t, dim=1)


class Rectangle(Polygon):
    """
    Axis aligned Rectangle defined by its diagonal from `x0` to `x1`.
    """

    def __init__(
        self, x0: tuple[float, float], x1: tuple[float, float], **kwargs: dict
    ) -> None:
        locs = [x0, [x1[0], x0[1]], x1, [x0[0], x1[1]]]
        super().__init__(locs=locs, **kwargs)
