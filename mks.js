const {cylinder, cube} = require('@jscad/csg/api').primitives3d
const {color} = require('@jscad/csg/api').color
const {difference, union} = require('@jscad/csg/api').booleanOps
const {translate} = require('@jscad/csg/api').transformations

const basePlate = color("brown", cube({size: [110, 84, 1.4]}))  

const baseHoles = union(
  translate([0, 0,-1], cylinder({d:2.75, h:3})),
  translate([0, 76, -1], cylinder({d:2.75, h:3})),
  translate([102, 76, -1], cylinder({d:2.75, h:3})),
  translate([102, 0, -1], cylinder({d:2.75, h:3})) 
)

const usb = color("gray", 
  cube({size: [12, 16, 11]})
)

const powerConnectors = color("green", 
  cube({size: [11, 24, 20]})
)

const steppers = color("green",
  cube({size: [108, 16, 28]})
)

const aux1 = color("black",
  cube({size: [18, 9, 9]})
)

const exp = color("black",
  cube({size: [9, 20, 9]})
)

const stepperConnectors = color("yellow",
  cube({size: [90, 6, 6]})  
)

const thConnectors = color("yellow",
  cube({size: [24, 6, 6]})  
)

const base = difference(
  basePlate, 
  translate([4, 4, 0], baseHoles)
)

const mks = union(
  base,
  translate([22, 0, 1.4], usb),
  translate([0, 8, 1.4], powerConnectors),
  translate([1, 61, 1.4], steppers),
  translate([8, 77.5, 1.4], stepperConnectors),
  translate([60, 0, 1.4], aux1),
  translate([78.5, 1, 1.4], thConnectors),
  translate([100, 19, 1.4], exp),
  translate([100, 40, 1.4], exp),
)

function main () {
  return [
    mks
  ];
}

module.exports = {
  mks
}