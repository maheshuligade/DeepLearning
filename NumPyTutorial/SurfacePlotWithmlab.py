from numpy import mgrid
from scipy import special
from math import sqrt
x,y = mgrid[-25:25:100j,-25:25:100j]
mgrid[-25:25:100j,-25:25:100j]
r = sqrt(x**2 + y**2)
s = special.j0(r)*25
from mayavi import mlab
