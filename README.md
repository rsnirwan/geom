# Describe and Render Geometries

## Install

```bash
pip install git+https://github.com/rsnirwan/geom.git
```

or

```bash
git clone https://github.com/rsnirwan/geom.git
cd geom
pip install -e .
#pip install -e ".[dev]" # for dev-dependencies
```

## Usage

```python
from geom.shapes import Circle, Rectangle
import numpy as np
import matplotlib.pyplot as plt

cir = Circle(loc=[0, 1], r=2)
rect = Rectangle(x0=[0, 0], x1=[1, 1])
rect2 = Rectangle(x0=[0, 0], x1=[1, 1])\
            .rotate(phi=np.pi/4)
rect3 = Rectangle(x0=[0, 0], x1=[1, 1])\
            .rotate(phi=np.pi/4)\
            .translate(vec=[-1.5, -1.5])

plt.plot(*cir.to_array().T)
plt.plot(*rect.to_array().T)
plt.plot(*rect2.to_array().T)
plt.plot(*rect3.to_array().T)
plt.show()
```