#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

from solid import *
from solid.utils import *

SEGMENTS = 48

def holder():
    return cube(size=[20, 15, 15]) - (translate([-1, 2, 2])(cube(size=[22, 11, 11])))

def stand_base():
    height = 130
    width = 25
    return polygon(points = [[0, 0], [0, height], [width, height], [width, 0]])

def extruded_base():
    shape = stand_base()
    extruded = linear_extrude(height = 2)(shape)
    screw_hole = cylinder(r=2.9, h=4)
    hole_distance = 113
    screw_holes = translate([12,10,-1])(screw_hole) + translate([15,10 + hole_distance, -1])(screw_hole)
    holders = holder()
    return (extruded - screw_holes) + holders

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'basic_geometry.scad')

    a = extruded_base()

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS)