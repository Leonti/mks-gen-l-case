$fn = 48;

union() {
	difference() {
		linear_extrude(height = 2) {
			polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [0, 130], [25, 130], [25, 0]]);
		}
		union() {
			translate(v = [12, 10, -1]) {
				cylinder(d = 2.9000000000, h = 4);
			}
			translate(v = [15, 123, -1]) {
				cylinder(d = 2.9000000000, h = 4);
			}
		}
	}
	union() {
		translate(v = [0, 28, 0]) {
			difference() {
				cube(size = [40, 15, 15]);
				translate(v = [-1, 2, 2]) {
					cube(size = [42, 11, 11]);
				}
				translate(v = [30, 7.5000000000, 12]) {
					cylinder(d = 2.9000000000, h = 4);
				}
				translate(v = [30, 7.5000000000, -1]) {
					cylinder(d = 7, h = 4);
				}
			}
		}
		translate(v = [0, 80, 0]) {
			difference() {
				cube(size = [40, 15, 15]);
				translate(v = [-1, 2, 2]) {
					cube(size = [42, 11, 11]);
				}
				translate(v = [30, 7.5000000000, 12]) {
					cylinder(d = 2.9000000000, h = 4);
				}
				translate(v = [30, 7.5000000000, -1]) {
					cylinder(d = 7, h = 4);
				}
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

from solid import *
from solid.utils import *

SEGMENTS = 48

def holder():
    holder_x = 40
    holder_y = 15
    holder_z = 15
    upper_hole = translate([30, holder_y/2, holder_z - 3])(cylinder(d=2.9, h=4))
    bottom_hole = translate([30, holder_y/2, -1 ])(cylinder(d=7, h=4))
    holder_base = cube(size=[holder_x, holder_y, holder_z]) - (translate([-1, 2, 2])(cube(size=[holder_x + 2, holder_y - 4, holder_z - 4])))
    return holder_base - upper_hole - bottom_hole

def stand_base():
    height = 130
    width = 25
    return polygon(points = [[0, 0], [0, height], [width, height], [width, 0]])

def extruded_base():
    shape = stand_base()
    extruded = linear_extrude(height = 2)(shape)
    screw_hole = cylinder(d=2.9, h=4)
    hole_distance = 113
    screw_holes = translate([12,10,-1])(screw_hole) + translate([15,10 + hole_distance, -1])(screw_hole)
    holders = translate([0, 28, 0])(holder()) + translate([0, 80, 0])(holder())
    return (extruded - screw_holes) + holders

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'stand.scad')

    a = extruded_base()

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS) 
 
************************************************/
