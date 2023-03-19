from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path
from .bosl2_mixin import Bosl2Mixin

extra_scad_include(f"{Path(__file__).parent.parent / '../libs/BOSL2/coords.scad'}", use_not_include=False)

class point2d(OpenSCADObject, Bosl2Mixin):
    def __init__(self, p=None, fill=None, **kwargs):
       super().__init__("point2d", {"p" : p, "fill" : fill, **kwargs})

class path2d(OpenSCADObject, Bosl2Mixin):
    def __init__(self, points=None, **kwargs):
       super().__init__("path2d", {"points" : points, **kwargs})

class point3d(OpenSCADObject, Bosl2Mixin):
    def __init__(self, p=None, fill=None, **kwargs):
       super().__init__("point3d", {"p" : p, "fill" : fill, **kwargs})

class path3d(OpenSCADObject, Bosl2Mixin):
    def __init__(self, points=None, fill=None, **kwargs):
       super().__init__("path3d", {"points" : points, "fill" : fill, **kwargs})

class point4d(OpenSCADObject, Bosl2Mixin):
    def __init__(self, p=None, fill=None, **kwargs):
       super().__init__("point4d", {"p" : p, "fill" : fill, **kwargs})

class path4d(OpenSCADObject, Bosl2Mixin):
    def __init__(self, points=None, fill=None, **kwargs):
       super().__init__("path4d", {"points" : points, "fill" : fill, **kwargs})

class polar_to_xy(OpenSCADObject, Bosl2Mixin):
    def __init__(self, r=None, theta=None, **kwargs):
       super().__init__("polar_to_xy", {"r" : r, "theta" : theta, **kwargs})

class xy_to_polar(OpenSCADObject, Bosl2Mixin):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("xy_to_polar", {"x" : x, "y" : y, **kwargs})

class project_plane(OpenSCADObject, Bosl2Mixin):
    def __init__(self, plane=None, p=None, **kwargs):
       super().__init__("project_plane", {"plane" : plane, "p" : p, **kwargs})

class lift_plane(OpenSCADObject, Bosl2Mixin):
    def __init__(self, plane=None, p=None, **kwargs):
       super().__init__("lift_plane", {"plane" : plane, "p" : p, **kwargs})

class cylindrical_to_xyz(OpenSCADObject, Bosl2Mixin):
    def __init__(self, r=None, theta=None, z=None, **kwargs):
       super().__init__("cylindrical_to_xyz", {"r" : r, "theta" : theta, "z" : z, **kwargs})

class xyz_to_cylindrical(OpenSCADObject, Bosl2Mixin):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("xyz_to_cylindrical", {"x" : x, "y" : y, "z" : z, **kwargs})

class spherical_to_xyz(OpenSCADObject, Bosl2Mixin):
    def __init__(self, r=None, theta=None, phi=None, **kwargs):
       super().__init__("spherical_to_xyz", {"r" : r, "theta" : theta, "phi" : phi, **kwargs})

class xyz_to_spherical(OpenSCADObject, Bosl2Mixin):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("xyz_to_spherical", {"x" : x, "y" : y, "z" : z, **kwargs})

class altaz_to_xyz(OpenSCADObject, Bosl2Mixin):
    def __init__(self, alt=None, az=None, r=None, **kwargs):
       super().__init__("altaz_to_xyz", {"alt" : alt, "az" : az, "r" : r, **kwargs})

class xyz_to_altaz(OpenSCADObject, Bosl2Mixin):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("xyz_to_altaz", {"x" : x, "y" : y, "z" : z, **kwargs})
