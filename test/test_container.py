import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from geom import container
from geom import shapes


def test_Container_rotate():
    rect = shapes.Rectangle(x0=[0, 0], x1=[1, 1])
    cont = container.Container(shapes=[shapes.Rectangle(x0=[0, 0], x1=[1, 1])])
    assert np.allclose(
        rect.rotate(phi=np.pi / 2).to_array(),
        cont.rotate(phi=np.pi / 2).shapes[0].to_array(),
    )


def test_Container_translate():
    rect = shapes.Rectangle(x0=[0, 0], x1=[1, 1])
    cont = container.Container(shapes=[shapes.Rectangle(x0=[0, 0], x1=[1, 1])])
    assert np.allclose(
        rect.translate(vec=[1.0, 1.0]).to_array(),
        cont.translate(vec=[1.0, 1.0]).shapes[0].to_array(),
    )


def test_Container_draw_1():
    c = container.Container(
        shapes=[
            shapes.Circle(loc=[0, 1], radius=2),
            shapes.Rectangle(x0=[0, 0], x1=[1, 1]),
        ]
    )
    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    c.draw(ax=ax, color="green", linestyle="-")


def test_Container_draw_2():
    c = container.Container(
        shapes=[
            shapes.Circle(loc=[0, 1], radius=2),
            shapes.Rectangle(x0=[0, 0], x1=[1, 1]),
        ]
    )
    fig, ax = c.draw(color="green", linestyle="-")
    assert isinstance(fig, Figure)
    assert isinstance(ax, Axes)
