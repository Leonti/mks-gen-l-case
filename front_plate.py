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

LCD_PCB_WIDTH = 70
LCD_PCB_HEIGHT = 75

lcd_pcb = color("green")(
    cube([LCD_PCB_WIDTH, LCD_PCB_HEIGHT, 16])
    + translate([25,58,16])(cube([20, 10, 16]))
    + translate([(LCD_PCB_WIDTH - lcd_hole_distance_x)/2, (LCD_PCB_HEIGHT - lcd_hole_distance_y)/2,-3])(lcd_holes) 
    )

base_plate_dim_x = LCD_PCB_WIDTH + 4
base_plate_dim_y = LCD_PCB_HEIGHT + 4 + 11

side = rotate([90,0,90])(linear_extrude(height=2)(
    polygon([[0,0],[LCD_PCB_WIDTH + 20, 0],[LCD_PCB_WIDTH + 20,35],[20,35]])
    ))

skirt = cube([base_plate_dim_x + 10, 50, 4])
back_box = (
    cube([base_plate_dim_x, base_plate_dim_y, 35])
    + translate([-5, 2, -2])(rotate([60,0,0])(skirt))
    - translate([2,2,0])(cube([base_plate_dim_x - 4, base_plate_dim_y - 4, 38]))
    )

cut_box = translate([-10, 0, -2])(
    rotate([60,0,0])(cube([base_plate_dim_x + 20, 100, 100]))
)

cut_box_front = translate([-10,0,-20])(cube([base_plate_dim_x + 20, 100, 20]))

base_plate = (
    cube(size=[base_plate_dim_x, base_plate_dim_y, 2])
     - translate([2,13,2])(lcd_pcb)
     + translate([0,0,0])(back_box)
     - cut_box
     - translate([-10,0,-20])(cube([base_plate_dim_x + 20, 100, 20]))
     - translate([-10,0,35])(cube([base_plate_dim_x + 20, 100, 20]))
#    + translate([0,0,2])(side)
#    + translate([base_plate_dim_x - 2,0,2])(side)
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