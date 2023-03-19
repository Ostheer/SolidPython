from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path
from .bosl2_mixin import Bosl2Mixin

extra_scad_include(f"{Path(__file__).parent.parent / '../libs/BOSL2/wiring.scad'}", use_not_include=False)

class wire_bundle(OpenSCADObject, Bosl2Mixin):
    def __init__(self, path=None, wires=None, wirediam=None, rounding=None, wirenum=None, corner_steps=None, **kwargs):
       super().__init__("wire_bundle", {"path" : path, "wires" : wires, "wirediam" : wirediam, "rounding" : rounding, "wirenum" : wirenum, "corner_steps" : corner_steps, **kwargs})

class _hex_offset_ring(OpenSCADObject, Bosl2Mixin):
    def __init__(self, d=None, lev=None, **kwargs):
       super().__init__("_hex_offset_ring", {"d" : d, "lev" : lev, **kwargs})

class _hex_offsets(OpenSCADObject, Bosl2Mixin):
    def __init__(self, n=None, d=None, lev=None, arr=None, **kwargs):
       super().__init__("_hex_offsets", {"n" : n, "d" : d, "lev" : lev, "arr" : arr, **kwargs})
