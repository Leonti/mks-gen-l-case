$fn = 48;

difference() {
	union() {
		cube(size = [90, 100, 2]);
		translate(v = [10, 5, 1]) {
			difference() {
				union() {
					cube(size = [33, 2, 21]);
					translate(v = [0, 2, 0]) {
						cube(size = [2, 3.5000000000, 21]);
					}
					translate(v = [31, 2, 0]) {
						cube(size = [2, 3.5000000000, 21]);
					}
					translate(v = [2, 2, 19]) {
						cube(size = [29, 3.5000000000, 2]);
					}
				}
				translate(v = [4, -15, 2.2000000000]) {
					cube(size = [5.5000000000, 20, 13.5000000000]);
				}
			}
		}
	}
	translate(v = [12, 7, 1]) {
		union() {
			cube(size = [29, 7, 2]);
			translate(v = [12, 3.5000000000, -2]) {
				cube(size = [12, 2, 3]);
			}
		}
	}
	translate(v = [13.7500000000, 20, 0]) {
		union() {
			translate(v = [8.7500000000, 32, -1]) {
				cube(size = [45, 29, 4]);
			}
			translate(v = [0, 0, -1]) {
				cylinder(d = 2.8000000000, h = 10);
			}
			translate(v = [0, 67, -1]) {
				cylinder(d = 2.8000000000, h = 10);
			}
			translate(v = [62.5000000000, 67, -1]) {
				cylinder(d = 2.8000000000, h = 10);
			}
			translate(v = [62.5000000000, 0, -1]) {
				cylinder(d = 2.8000000000, h = 10);
			}
			translate(v = [31.2500000000, 10, -1]) {
				cylinder(d = 12, h = 10);
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

lcd_hole_distance_x = 62.5
lcd_hole_distance_y = 67

lcd_screw_holes = (
  translate([0, 0, -1])(cylinder(d=2.8, h=10)),
  translate([0, lcd_hole_distance_y, -1])(cylinder(d=2.8, h=10)),
  translate([lcd_hole_distance_x, lcd_hole_distance_y, -1])(cylinder(d=2.8, h=10)),
  translate([lcd_hole_distance_x, 0, -1])(cylinder(d=2.8, h=10)) 
)

lcd_window_x = 45
lcd_window = cube(size=[lcd_window_x, 29, 4])

lcd_holes = (
    lcd_screw_holes +
    translate([(lcd_hole_distance_x - lcd_window_x)/2, 32, -1])(lcd_window) +
    translate([31.25, 10, -1])(cylinder(d=12, h=10))
)

sd_card_slot = cube(size=[15, 2, 4])

card_width = 29
card_depth = 19
card_connector_hole = cube(size=[5.5, 20, 13.5])
card_fence_height = 3.5
sd_card_holder = (
    cube(size=[card_width + 4, 2, card_depth + 2]) + 
    translate([0, 2, 0])(cube(size=[2, card_fence_height, card_depth + 2])) +
    translate([card_width + 2, 2, 0])(cube(size=[2, card_fence_height, card_depth + 2])) +
    translate([2, 2, card_depth])(cube(size=[card_width, card_fence_height, 2])) -
    translate([4, -15, 2.2])(card_connector_hole)
)

sd_card_hole = (
    cube(size=[card_width, 7, 2]) +
    translate([12,3.5,-2])(cube(size=[12, 2, 3]))
)

base_plate_dim_x = 90
base_plate_dim_y = 100

card_holder_x = 10
card_holder_y = 5
base_plate_test = (
    cube(size=[base_plate_dim_x, base_plate_dim_y, 2])+
    translate([card_holder_x, card_holder_y, 1])(sd_card_holder) -
    translate([card_holder_x + 2, card_holder_y + 2, 1])(sd_card_hole) -
    translate([(base_plate_dim_x - lcd_hole_distance_x)/2, 20, 0])(lcd_holes)
)

base_plate = (
    cube(size=[80, 80, 2]) - 
    translate([5, 5, -1])(lcd_holes) -
    translate([20, 25, -1])(lcd_window) -
    translate([30, 15, -1])(sd_card_slot) +
    translate([28, 13, 2])(sd_card_holder)
)

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'front_plate.scad')

    a = base_plate_test

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS) 
 
************************************************/
