#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

from solid import *
from solid.utils import *
from math import floor
from functools import reduce

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

#stand_hole = rotate([-90, 0, 0])(cylinder(d=2.9, h=4))
#stand_holes = (
#  stand_hole,
#  translate([52, 0, 0])(stand_hole)
#)

# bottom holes x y:
# 30 6
# 134.5 6
# 21.5 85
# 134.5 83

box_x = 142
box_y = 110
box_z = 47 # 47 min
wall_width = 2

fan_holes = (
  translate([0, 0, 0])(cylinder(d=2.8, h=10)),
  translate([0, 50, 0])(cylinder(d=2.8, h=10))
)

fan_air_hole = cube([4, 50, 50])

AIR_HOLE_WIDTH = 3
def air_holes(width, height):
  hole_height = (height - AIR_HOLE_WIDTH) / 2
  air_hole = cube([wall_width + 2, AIR_HOLE_WIDTH, hole_height])
  steps = range(0, floor(width / AIR_HOLE_WIDTH / 2))
  air_holes = []
  for step in steps:
    air_holes.append(translate([0, AIR_HOLE_WIDTH * 2 * step, 0])(air_hole))
    air_holes.append(translate([0, AIR_HOLE_WIDTH * 2 * step, hole_height + AIR_HOLE_WIDTH])(air_hole))

  return reduce(lambda a, b: a+b, air_holes)


#usb_hole = cube(size = [11, wall_width + 2, 9])
stepper_hole = cube(size = [15, 7, wall_width + 2])
power_hole = rotate([0, -90, 0])(cylinder(d=8, h=wall_width + 2))
chamber_hole = cube(size = [90, 65, wall_width + 2])

holes = (
  translate([30.1 + stand_diameter/2, 22.7 + stand_diameter / 2, 0])(stand_holes) +
#  translate([30.1 + 22.2, -1, wall_width + stand_height + 2])(usb_hole) +
#  translate([45, box_y - wall_width - 7, -1])(stepper_hole) +
#  translate([85, box_y - wall_width - 7, -1])(stepper_hole) +
  translate([40, 32, -1])(chamber_hole) +
  translate([wall_width + 1, 30, wall_width + stand_height + 2])(power_hole) +
  translate([wall_width + 1, 40, wall_width + stand_height + 2])(power_hole) +
  translate([wall_width + 1, 35, wall_width + stand_height + 10])(power_hole) +
  translate([13, 50, -1])(fan_holes)
  + translate([-1,55, wall_width])(fan_air_hole)
  + translate([-1, 5, 10])(air_holes(22, 30))
  + translate([box_x - 2, 40, 6])(air_holes(box_y - 40, 35))
#  + translate([box_x - 7, -1, 6])(rotate([0,0,90])(air_holes(box_x - 5, 35)))
#  + translate([box_x - 7, box_y - wall_width - 1, 6])(rotate([0,0,90])(air_holes(box_x - 5, 35)))
#  translate([24, -1, 10])(stand_holes)
)

box_base = cube(size = [box_x, box_y, box_z]) - translate([wall_width, wall_width, wall_width])( 
        cube(size = [
          box_x - wall_width * 2, 
          box_y - wall_width * 2, 
          box_z
        ]))

box_with_stands = (box_base
  + translate([30.1 + stand_diameter/2, 22.7 + stand_diameter / 2, wall_width])(mks_stands))

sd_card_slot = cube(size=[15, 2, 4])

card_width = 29
card_depth = 19
card_connector_hole = cube(size=[5.5, 20, 13.5])
card_fence_height = 3.5
sd_card_holder = rotate([90, 0, -90])(
    cube(size=[card_width + 4, 2, card_depth + 2]) + 
    translate([0, 2, 0])(cube(size=[2, card_fence_height, card_depth + 2])) +
    translate([card_width + 2, 2, 0])(cube(size=[2, card_fence_height, card_depth + 2])) +
    translate([2, 2, card_depth])(cube(size=[card_width, card_fence_height, 2])) -
    translate([4, -15, 2.2])(card_connector_hole)
)

sd_card_hole = rotate([90, 0, -90])(translate([2, 2 , -1])(
    cube(size=[card_width, 7, 2]) +
    translate([12,3.5,-2])(cube(size=[12, 2, 3]))
))

box = (
  box_with_stands
  + translate([box_x - wall_width, 35, 38])(sd_card_holder)
  ) - (
    holes
    + translate([box_x - wall_width, 35, 38])(sd_card_hole)
  )

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