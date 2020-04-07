#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

from solid import *
from solid.utils import *
nuts_n_bolts = import_scad('/home/leonti/3d/openscad_libraries/nutsnbolts')

SEGMENTS = 48

# display top
# 75 width
# 60 depth

# lcd wire hole
# 25 width
# 15 depth
# 40 y
# 10 x

# rpi
# 23 y
# 25 x

DEPTH = 142
WIDTH = 110
CASE_WALL_WIDTH = 2.1
SKIRT_HEIGHT = 3.5
WALL_WIDTH = 2

top_lid = cube([DEPTH, WIDTH, WALL_WIDTH])

sd_card_hole_height = 1.9
sd_card_hole_width = 17
sd_card_hole = cube([WALL_WIDTH, sd_card_hole_width, sd_card_hole_height])

mount_hole = (
    nuts_n_bolts.cyl_head_bolt.nutcatch_parallel("M3", l=WALL_WIDTH)
    + nuts_n_bolts.cyl_head_bolt.hole_through(name="M3", l=10, cld=0.1, h=0, hcld=0.4)
)

ear = (
    cylinder(d = 10, h = WALL_WIDTH)
    + translate([0, 0, -WALL_WIDTH])(cylinder(d = 10, h = WALL_WIDTH))
    + translate([0,-5,0])(cube([5, 10, WALL_WIDTH]))
    - translate([0,0,-2])(rotate([0,180,0])(mount_hole))
)

ear_left = translate([5, 0, -5])(rotate([-90,-90,0])(ear))
ear_right = translate([5, WALL_WIDTH, -5])(rotate([90,-90,0])(ear))

skirt_width = WIDTH - (CASE_WALL_WIDTH * 2)
skirt = (
    cube([DEPTH - (CASE_WALL_WIDTH * 2), skirt_width, SKIRT_HEIGHT])
    - translate([WALL_WIDTH, WALL_WIDTH, 0])(cube([
        DEPTH - (CASE_WALL_WIDTH * 2) - (WALL_WIDTH * 2), 
        skirt_width - (WALL_WIDTH * 2), 
        SKIRT_HEIGHT]))
    - translate([0, skirt_width - sd_card_hole_width - 7, 0])(sd_card_hole)
    + translate([25,0,0])(ear_right)
    + translate([60,0,0])(ear_right)
    + translate([100,0,0])(ear_right)
    + translate([25, skirt_width - WALL_WIDTH, 0])(ear_left)
    + translate([100, skirt_width - WALL_WIDTH, 0])(ear_left) 
    )

rpi_stand = cylinder(d = 7, h = WALL_WIDTH)
raspberry_pi_stands = (
      translate([0, 0, -WALL_WIDTH])(rpi_stand)
    + translate([58, 0, -WALL_WIDTH])(rpi_stand)
    + translate([58, 49, -WALL_WIDTH])(rpi_stand)
    + translate([0, 49, -WALL_WIDTH])(rpi_stand)
)

rpi_hole = cylinder(d = 3.2, h = WALL_WIDTH * 2)
raspberry_pi_holes = (
      translate([0, 0, -WALL_WIDTH])(rpi_hole)
    + translate([58, 0, -WALL_WIDTH])(rpi_hole)
    + translate([58, 49, -WALL_WIDTH])(rpi_hole)
    + translate([0, 49, -WALL_WIDTH])(rpi_hole)
)

lcd_wire_hole = cube([15, 25, WALL_WIDTH])
full = (
    top_lid
    - translate([10,40,0])(lcd_wire_hole)
    + translate([49, 30, 0])(raspberry_pi_stands)
    - translate([49, 30, 0])(raspberry_pi_holes)
    + translate([CASE_WALL_WIDTH, CASE_WALL_WIDTH, -SKIRT_HEIGHT])(skirt)
)
if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'top_lid.scad')

    a = full

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS)