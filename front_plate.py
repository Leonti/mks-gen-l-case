#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

from solid import *
from solid.utils import *

SEGMENTS = 48

lcd_hole_distance_x = 70
lcd_hole_distance_y = 70

lcd_holes = (
  translate([0, 0, -1])(cylinder(d=2.8, h=10)),
  translate([0, lcd_hole_distance_y, -1])(cylinder(d=2.8, h=10)),
  translate([lcd_hole_distance_x, lcd_hole_distance_y, -1])(cylinder(d=2.8, h=10)),
  translate([lcd_hole_distance_x, 0, -1])(cylinder(d=2.8, h=10)) 
)

lcd_window = cube(size=[40, 30, 4])

sd_card_slot = cube(size=[15, 2, 4])

sd_card_holder = (
    cube(size=[19, 2, 20]) + 
    translate([0, 2, 0])(cube(size=[2, 3, 20])) +
    translate([17, 2, 0])(cube(size=[2, 3, 20])) +
    translate([0, 2, 18])(cube(size=[19, 3, 2]))
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

    a = base_plate

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS)