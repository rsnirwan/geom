from functools import partial
from math import isclose
from unittest import mock

import numpy as np

from geom import shapes

close_to = partial(isclose, abs_tol=1e-10)


def test_BaseShape_evaluate():
    # test through Circle
    c = shapes.Circle([0.0, 0.0], 1.0)
    assert np.allclose(c.evaluate(t=0.0), [1.0, 0.0])
    assert np.allclose(c.evaluate(t=0.25), [0.0, 1.0])
    assert np.allclose(c.evaluate(t=0.5), [-1.0, 0.0])


def test_BaseShape_rotate():
    # test through Circle
    phi = mock.Mock()
    c = shapes.Circle([0.0, 0.0], 1.0)
    c.rotate(phi)
    assert len(c.trafos.trafos) == 1


def test_BaseShape_translate():
    # test through Circle
    phi = mock.Mock()
    c = shapes.Circle([0.0, 0.0], 1.0)
    c.translate(phi)
    assert len(c.trafos.trafos) == 1


def test_BaseShape_to_array():
    # test through Circle
    c = shapes.Circle([0.0, 0.0], 1.0)
    ts = np.array([0.0, 0.25, 1.0])
    assert c.to_array(n=20).shape == (20, 2)
    assert c.to_array(ts=ts).shape == (3, 2)


def test_ArcEllipse_f_x():
    c = shapes.ArcEllipse([1.0, 0.0], width=1.0, hight=1.0, phi0=0.0, phi1=2 * np.pi)
    assert close_to(c._f_x(t=0.0), 2.0)
    assert close_to(c._f_x(t=0.25), 1.0)
    assert close_to(c._f_x(t=0.50), 0.0)
    assert close_to(c._f_x(t=0.75), 1.0)
    assert close_to(c._f_x(t=1.0), 2.0)


def test_ArcEllipse_f_y():
    c = shapes.ArcEllipse([1.0, 0.0], width=1.0, hight=2.0, phi0=0.0, phi1=2 * np.pi)
    assert close_to(c._f_y(t=0.0), 0.0)
    assert close_to(c._f_y(t=0.25), 2.0)
    assert close_to(c._f_y(t=0.50), 0.0)
    assert close_to(c._f_y(t=0.75), -2.0)
    assert close_to(c._f_y(t=1.0), 0.0)


def test_Circle_init():
    c = shapes.Circle(loc=[0.0, 1.0], radius=2.0)
    assert c.x == 0.0
    assert c.y == 1.0
    assert c.width == 2.0
    assert c.hight == 2.0
    assert c.phi0 == 0.0
    assert c.phi1 == 2 * np.pi


def test_Ellipse_init():
    c = shapes.Ellipse(loc=[0.0, 1.0], width=2.0, hight=3.0)
    assert c.x == 0.0
    assert c.y == 1.0
    assert c.width == 2.0
    assert c.hight == 3.0
    assert c.phi0 == 0.0
    assert c.phi1 == 2 * np.pi


def test_ArcCircle_init():
    c = shapes.ArcCircle(loc=[0.0, 1.0], radius=3.0, phi0=1.0, phi1=2.0)
    assert c.x == 0.0
    assert c.y == 1.0
    assert c.width == 3.0
    assert c.hight == 3.0
    assert c.phi0 == 1.0
    assert c.phi1 == 2.0


def test_Rectangle_init():
    r = shapes.Rectangle([1.0, 1.0], [2.0, 2.0])
    assert np.allclose(r.x0, [1.0, 1.0])
    assert np.allclose(r.x1, [2.0, 2.0])


def test_Rectangle_f_x():
    c = shapes.Rectangle([1.0, 1.0], [2.0, 2.0])
    assert close_to(c._f_x(t=0.0), 1.0)
    assert close_to(c._f_x(t=0.25), 2.0)
    assert close_to(c._f_x(t=0.50), 2.0)
    assert close_to(c._f_x(t=0.75), 1.0)
    assert close_to(c._f_x(t=1.0), 1.0)


def test_Rectangle_f_y():
    c = shapes.Rectangle([1.0, 1.0], [2.0, 2.0])
    assert close_to(c._f_y(t=0.0), 1.0)
    assert close_to(c._f_y(t=0.25), 1.0)
    assert close_to(c._f_y(t=0.50), 2.0)
    assert close_to(c._f_y(t=0.75), 2.0)
    assert close_to(c._f_y(t=1.0), 1.0)
