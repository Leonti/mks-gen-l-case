const {cylinder, cube} = require('@jscad/csg/api').primitives3d
const {color} = require('@jscad/csg/api').color
const {difference, union} = require('@jscad/csg/api').booleanOps
const {translate} = require('@jscad/csg/api').transformations

const basePlate = color("limegreen",
    cube({size: [85, 56, 1.4]})
)  
// 3.5
// 85/49
/* 
  translate([0, 0,-1], cylinder({d:2.75, h:3})),
  translate([0, 76, -1], cylinder({d:2.75, h:3})),
  translate([102, 76, -1], cylinder({d:2.75, h:3})),
  translate([102, 0, -1], cylinder({d:2.75, h:3})) 
*/
const baseHoles = union(
  translate([0, 0, -1], cylinder({d:2.75, h:3})),
  translate([0, 49, -1], cylinder({d:2.75, h:3})),
  translate([59, 49, -1], cylinder({d:2.75, h:3})),
  translate([59, 0,-1], cylinder({d:2.75, h:3})) 
)

const base = difference(
  basePlate, 
  translate([3.5, 3.5, 0], baseHoles)
  )

const header = (pins, rows) => {
  const base = color("darkgrey", cube([2.54*pins,2.54*rows,1.27]));
  
  const pinss = []
  for (let x = 0; x < pins; x++) {
    for (let y = 0; y < rows; y++) {
      let pin = cube([0.6,0.6,11.5])
      pinss.push(translate([x*2.54+(1.27+.6)/2,y*2.54+(1.27+.6)/2,-3.5], pin))
    }
  }

  return union(base, union(pinss))
}

const components = () => {
  const ethernet = cube([21,16,13.8])
  const usb1 = cube([17,13,15.5])
  const usb2 = cube([17,13,15.5])
  const microUsb = cube([8,6,2.6])
  const hdmi = cube([15,11.5,6.6])

  return union(
      translate([85-19, 2, 0], ethernet),
      translate([85-15, 29-13/2,0], usb1),
      translate([85-15, 47-13/2,0], usb2),
      translate([10.6-8/2,-1.5,0], microUsb),
      translate([32-15/2,-1.5,0], hdmi)    
  );
}

const rpi = union(
  base,
  translate([0, 0, 1.4], components()),
  translate([7, 50, 1.4], header(20, 2)),
)

function main () {
  return [
    rpi
  ];
}

module.exports = {
  rpi
}