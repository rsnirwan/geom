from __future__ import annotations

import numpy as np

from geom.transformations import Transformations, Rotation, Translation


class BaseShape:
    def __init__(self, **kwargs) -> None:
        self.trafos = Transformations()

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


class Rectangle(BaseShape):
    """
    Axis aligned Rectangle defined by its diagonal from `x0` to `x1`.
    """

    def __init__(
        self, x0: tuple[float, float], x1: tuple[float, float], **kwargs: dict
    ) -> None:
        self.x0 = np.array(x0)
        self.x1 = np.array(x1)
        super().__init__(**kwargs)

    def _f_x(self, t: float) -> float:
        start, end = self.x0[0], self.x1[0]
        if t < 0.25:
            return start + 4 * t * (end - start)
        elif t < 0.5:
            return end
        elif t < 0.75:
            return end - 4 * (t - 0.5) * (end - start)
        else:
            return start

    def _f_y(self, t: float) -> float:
        start, end = self.x0[1], self.x1[1]
        if t < 0.25:
            return start
        elif t < 0.5:
            return start + 4 * (t - 0.25) * (end - start)
        elif t < 0.75:
            return end
        else:
            return end - 4 * (t - 0.75) * (end - start)
