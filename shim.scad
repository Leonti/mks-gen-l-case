$fn = 48;

difference() {
	cube(size = [15, 15, 1.7500000000]);
	translate(v = [8.5000000000, 7.5000000000, -1]) {
		cylinder(d = 7, h = 10);
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

shim = (
    cube(size=[15, 15, 1.75]) - 
    translate([8.5, 7.5, -1])(cylinder(d=7, h=10))
)

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'shim.scad')
 
    a = shim

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS) 
 
************************************************/
