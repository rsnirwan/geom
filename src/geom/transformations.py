from __future__ import annotations

import numpy as np


def rotation_matrix(phi: float) -> np.ndarray:
    return np.array([[c := np.cos(phi), s := -np.sin(phi)], [-s, c]])


class Transformation:
    def __init__(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return str(self)

    def __call__(self, vec: np.ndarray) -> np.ndarray:
        return self.forward(vec)

    def forward(self) -> np.ndarray:
        raise NotImplementedError


class Transformations(Transformation):
    def __init__(self, trafos: list[Transformation] = None) -> None:
        self.trafos = [] if trafos is None else trafos

    def __str__(self):
        return f"Transformations(trafos={str(self.trafos)})"

    def add(self, trafo: Transformation) -> None:
        self.trafos.append(trafo)

    def forward(self, vec: np.ndarray) -> np.ndarray:
        v = vec.copy()
        for t in self.trafos:
            v = t.forward(v)
        return v


class Rotation(Transformation):
    def __init__(self, phi: float) -> None:
        self.phi = phi

    def __str__(self):
        return f"Rotation(phi={self.phi})"

    def forward(self, vec: np.ndarray) -> np.ndarray:
        return np.matmul(rotation_matrix(self.phi), vec.T).T


class Translation(Transformation):
    def __init__(self, vec: np.ndarray) -> None:
        self.vec = np.array(vec).reshape(1, -1)

    def __str__(self):
        return f"Translation(vec={self.vec})"

    def forward(self, vec: np.ndarray) -> np.ndarray:
        return vec + self.vec
