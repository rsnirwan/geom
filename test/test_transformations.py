import numpy as np

from geom import transformations


def test_rotation_matrix_1():
    m = transformations.rotation_matrix(phi=0.0)
    m2 = transformations.rotation_matrix(phi=2 * np.pi)
    assert np.allclose(m, [[1.0, 0.0], [0.0, 1.0]])
    assert np.allclose(m2, [[1.0, 0.0], [0.0, 1.0]])


def test_rotation_matrix_2():
    m = transformations.rotation_matrix(phi=np.pi / 2)
    assert np.allclose(m, [[0.0, -1.0], [1.0, 0.0]])


def test_rotation_matrix_3():
    m = transformations.rotation_matrix(phi=np.pi)
    assert np.allclose(m, [[-1.0, 0.0], [0.0, -1.0]])


def test_rotation_matrix_4():
    m = transformations.rotation_matrix(phi=np.pi * 1.5)
    assert np.allclose(m, [[0.0, 1.0], [-1.0, 0.0]])


def test_Rotation_forward():
    rot = transformations.Rotation(phi=np.pi / 2)
    assert np.allclose(rot.forward(np.array([1.0, 0.0])), [0.0, 1.0])


def test_Rotation_str():
    rot = transformations.Rotation(phi=np.pi / 2)
    assert "Rotation" in str(rot)


def test_Rotation_call():
    rot = transformations.Rotation(phi=np.pi / 2)
    assert np.allclose(rot(np.array([1.0, 0.0])), [0.0, 1.0])


def test_Rotation_repr():
    rot = transformations.Rotation(phi=np.pi / 2)
    assert "Rotation" in repr(rot)


def test_Translation_forward():
    trans = transformations.Translation(vec=np.array([1.0, -1.0]))
    assert np.allclose(trans.forward(np.array([1.0, 0.0])), [2.0, -1.0])


def test_Translation_str():
    trans = transformations.Translation(vec=np.array([1.0, -1.0]))
    assert "Translation" in str(trans)


def test_Transformations_add():
    t = transformations.Transformations()
    t.add(transformations.Rotation(phi=np.pi))
    t.add(transformations.Translation(vec=np.array([1.0, 1.0])))
    assert len(t.trafos) == 2
    assert type(t.trafos[0]) == transformations.Rotation
    assert type(t.trafos[1]) == transformations.Translation


def test_Transformations_forward():
    t = transformations.Transformations()
    t.add(transformations.Rotation(phi=np.pi / 2))
    t.add(transformations.Translation(vec=np.array([1.0, 1.0])))
    assert np.allclose(t.forward(np.array([1.0, 0.0])), [1.0, 2.0])


def test_Transformations_str():
    t = transformations.Transformations()
    t.add(transformations.Rotation(phi=np.pi / 2))
    t.add(transformations.Translation(vec=np.array([1.0, 1.0])))
    assert "Transformations" in str(t)
    assert "Rotation" in str(t)
    assert "Translation" in str(t)
