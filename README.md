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
from geom.shapes import Circle, Rectangle, ArcEllipse, Polygon
from geom.container import Container
import numpy as np
import matplotlib.pyplot as plt

c = Container(shapes=[
    Circle(loc=[0, 1], radius=2),
    Rectangle(x0=[0, 0], x1=[1, 1]),
    Rectangle(x0=[0, 0], x1=[1, 1]).rotate(phi=np.pi/4),
    Rectangle(x0=[0, 0], x1=[1, 1]).rotate(phi=np.pi/4).translate(vec=[-1.5, -1.5]),
    ArcEllipse(loc=[0, 1], width=2., hight=1., phi0=1.2*np.pi, phi1=1.7*np.pi)\
        .translate(vec=[0, 0.5]),
    Polygon(locs=[[1, -1], [2, -1], [2, 1]], linestyle="--").rotate(phi=np.pi/5)
])

fig, ax = plt.subplots(1, 1, figsize=(7, 7))
c.draw(ax=ax, color="green", linestyle="-")
#fig, ax = c.draw(color="green", linestyle="dashed")
```