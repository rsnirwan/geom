import numpy as np


class BaseShape:
    def __init__(self) -> None:
        raise NotImplementedError

    def _f_x(self, t: float) -> float:
        raise NotImplementedError

    def _f_y(self, t: float) -> float:
        raise NotImplementedError

    def evaluate(self, t: float) -> tuple[float, float]:
        return (self._f_x(t), self._f_y(t))

    def to_array(self, n: int = 100, ts: np.ndarray = None) -> np.ndarray:
        if ts is None:
            ts = np.linspace(0, 1, n)
        return np.array([self.evaluate(t) for t in ts])


class Circle(BaseShape):
    def __init__(self, loc: tuple[float, float], r: float) -> None:
        self.x = loc[0]
        self.y = loc[1]
        self.r = r

    def _f_x(self, t: float) -> float:
        return self.x + self.r * np.cos(2 * np.pi * t)

    def _f_y(self, t: float) -> float:
        return self.y + self.r * np.sin(2 * np.pi * t)


class Rectangle(BaseShape):
    """
    Axis aligned Rectangle defined by its diagonal from `x0` to `x1`.
    """

    def __init__(self, x0: tuple[float, float], x1: tuple[float, float]) -> None:
        self.x0 = np.array(x0)
        self.x1 = np.array(x1)

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
