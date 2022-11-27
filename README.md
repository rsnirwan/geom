# Describe and Render Geometries

Work in progess. A lot might change in the future.

<img src="https://gist.githubusercontent.com/rsnirwan/466dc8982c06fa48d4855a1fe7a3ace8/raw/34a0b00a9912c1663bea3f50c94c355c3e9c34fe/geom.png" width="300" height="300">


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
#face.py
from geom.shapes import Circle, Rectangle, ArcEllipse, Polygon, Ellipse, ArcCircle
from geom.container import Container
import numpy as np
import matplotlib.pyplot as plt

c = Container(shapes=[
    ArcCircle(loc=[0, 0], radius=2.0, phi0=0.15*np.pi, phi1=1.85*np.pi).rotate(phi=np.pi/2), #face
    Ellipse(loc=[0., 0.], width=0.6, hight=0.3).rotate(-0.05*np.pi).translate(vec=[-0.8, 0.8]), #left eye
    Ellipse(loc=[0., 0.], width=0.6, hight=0.3).rotate(0.05*np.pi).translate(vec=[0.8, 0.8]), #left eye
    Polygon(locs=[[0.0, 0.5], [-0.3, -0.7], [0.3, -0.7]]), #nose
    ArcEllipse(loc=[0.0, -0.8], width=1.3, hight=0.7, phi0=1.2*np.pi, phi1=1.8*np.pi), #mouth
    ArcCircle(loc=[0.5, -1.6], radius=0.6, phi0=0.2*np.pi, phi1=0.8*np.pi), #mouth
    ArcCircle(loc=[-0.5, -1.6], radius=0.6, phi0=0.2*np.pi, phi1=0.8*np.pi), #mouth
    Ellipse(loc=[0.0, 0.0], width=0.3, hight=1.1).translate(vec=[2.3, 0]).rotate(phi=0.08*np.pi), #left ear
    Ellipse(loc=[0.0, 0.0], width=0.3, hight=1.1).translate(vec=[-2.3, 0]).rotate(phi=-0.08*np.pi), #right ear
    Rectangle(x0=[-2., 1.8], x1=[2., 2.2]), #hat
    Rectangle(x0=[-1.7, 2.2], x1=[1.7, 2.7]), #hat
])

#fig, ax = plt.subplots(1, 1, figsize=(7, 7))
#c.draw(ax=ax, color="green", linestyle="-") # provide your own axes

fig, ax = c.draw(color="green")
plt.show()
```