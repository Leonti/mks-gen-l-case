$fn = 48;

difference() {
	union() {
		difference() {
			cube(size = [142, 100, 22]);
			translate(v = [2, 2, 2]) {
				cube(size = [138, 96, 22]);
			}
		}
		translate(v = [33.8500000000, 6.4500000000, 2]) {
			union() {
				translate(v = [0, 0, -1]) {
					cylinder(d = 7.5000000000, h = 3);
				}
				translate(v = [0, 76, -1]) {
					cylinder(d = 7.5000000000, h = 3);
				}
				translate(v = [102, 76, -1]) {
					cylinder(d = 7.5000000000, h = 3);
				}
				translate(v = [102, 0, -1]) {
					cylinder(d = 7.5000000000, h = 3);
				}
			}
		}
	}
	union() {
		translate(v = [33.8500000000, 6.4500000000, 0]) {
			translate(v = [0, 0, -1]) {
				cylinder(d = 2.8000000000, h = 10);
			}
			translate(v = [0, 76, -1]) {
				cylinder(d = 2.8000000000, h = 10);
			}
			translate(v = [102, 76, -1]) {
				cylinder(d = 2.8000000000, h = 10);
			}
			translate(v = [102, 0, -1]) {
				cylinder(d = 2.8000000000, h = 10);
			}
		}
		translate(v = [52.3000000000, -1, 7]) {
			cube(size = [11, 4, 9]);
		}
		translate(v = [45, 91, -1]) {
			cube(size = [15, 7, 4]);
		}
		translate(v = [85, 91, -1]) {
			cube(size = [15, 7, 4]);
		}
		translate(v = [3, 10, 7]) {
			rotate(a = [0, -90, 0]) {
				cylinder(d = 8, h = 4);
			}
		}
		translate(v = [3, 20, 7]) {
			rotate(a = [0, -90, 0]) {
				cylinder(d = 8, h = 4);
			}
		}
		translate(v = [3, 15, 15]) {
			rotate(a = [0, -90, 0]) {
				cylinder(d = 8, h = 4);
			}
		}
		translate(v = [13, 40, -1]) {
			translate(v = [0, 0, 0]) {
				cylinder(d = 2.8000000000, h = 10);
			}
			translate(v = [0, 50, 0]) {
				cylinder(d = 2.8000000000, h = 10);
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

stand_diameter = 7.5
stand_height = 3

mks_stands = (
    translate([0, 0,-1])(cylinder(d = stand_diameter, h = stand_height)) + 
    translate([0, 76, -1])(cylinder(d = stand_diameter, h = stand_height)) + 
    translate([102, 76, -1])(cylinder(d = stand_diameter, h = stand_height)) + 
    translate([102, 0, -1])(cylinder(d = stand_diameter, h = stand_height))
)

stand_holes = (
  translate([0, 0,-1])(cylinder(d=2.8, h=10)),
  translate([0, 76, -1])(cylinder(d=2.8, h=10)),
  translate([102, 76, -1])(cylinder(d=2.8, h=10)),
  translate([102, 0, -1])(cylinder(d=2.8, h=10)) 
)

fan_holes = (
  translate([0, 0, 0])(cylinder(d=2.8, h=10)),
  translate([0, 50, 0])(cylinder(d=2.8, h=10))
)

box_x = 142
box_y = 100
box_z = 22 # 47 min
wall_width = 2

usb_hole = cube(size = [11, wall_width + 2, 9])
stepper_hole = cube(size = [15, 7, wall_width + 2])
power_hole = rotate([0, -90, 0])(cylinder(d=8, h=wall_width + 2))

holes = (
  translate([30.1 + stand_diameter/2, 2.7 + stand_diameter / 2, 0])(stand_holes) +
  translate([30.1 + 22.2, -1, wall_width + stand_height + 2])(usb_hole) +
  translate([45, box_y - wall_width - 7, -1])(stepper_hole) +
  translate([85, box_y - wall_width - 7, -1])(stepper_hole) +
  translate([wall_width + 1, 10, wall_width + stand_height + 2])(power_hole) +
  translate([wall_width + 1, 20, wall_width + stand_height + 2])(power_hole) +
  translate([wall_width + 1, 15, wall_width + stand_height + 10])(power_hole) +
  translate([13, 40, -1])(fan_holes)
)

box_base = cube(size = [box_x, box_y, box_z]) - translate([wall_width, wall_width, wall_width])( 
        cube(size = [
          box_x - wall_width * 2, 
          box_y - wall_width * 2, 
          box_z
        ]))

box_with_stands = box_base + translate([30.1 + stand_diameter/2, 2.7 + stand_diameter / 2, wall_width])(mks_stands)

box = box_with_stands - holes

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'case.scad')

    a = box

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS) 
 
************************************************/
