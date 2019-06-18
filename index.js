const { mks } = require('./mks') 
const { rpi } = require('./rpi')
const { fan } = require('./fan') 

const electronics = union(
  translate([0, 0, 2], mks),
//  translate([12, 0, 20], rpi),
  translate([-5, 45, 0], rotate([0, -90, 0],fan)),
)

const standDiameter = 7.5
const standHeight = 3
const mksStands = union(
  translate([0, 0,-1], cylinder({d:standDiameter, h:standHeight})),
  translate([0, 76, -1], cylinder({d:standDiameter, h:standHeight})),
  translate([102, 76, -1], cylinder({d:standDiameter, h:standHeight})),
  translate([102, 0, -1], cylinder({d:standDiameter, h:standHeight})) 
)

const standHoles = union(
  translate([0, 0,-1], cylinder({d:2.8, h:10})),
  translate([0, 76, -1], cylinder({d:2.8, h:10})),
  translate([102, 76, -1], cylinder({d:2.8, h:10})),
  translate([102, 0, -1], cylinder({d:2.8, h:10})) 
)

const fanHoles = union(
  translate([0, 0, 0], cylinder({d:2.8, h:10})),
  translate([0, 50, 0], cylinder({d:2.8, h:10})),
)

const boxX = 142
const boxY = 100
const boxZ = 22 // 47 min
const wallWidth = 2

const usbHole = cube({size: [11, wallWidth, 9]})
const stepperHole = cube({size: [15, 7, wallWidth] })
const powerHole = rotate([0, -90, 0], cylinder({d: 8, h: wallWidth }))

const holes = union(
  translate([30.1 + standDiameter/2, 2.7 + standDiameter / 2, 0], standHoles),
  translate([30.1 + 22.2, 0, wallWidth + standHeight + 2], usbHole),
  translate([45, boxY - wallWidth - 7, 0], stepperHole),
  translate([85, boxY - wallWidth - 7, 0], stepperHole),
  translate([wallWidth, 10, wallWidth + standHeight + 2], powerHole),
  translate([wallWidth, 20, wallWidth + standHeight + 2], powerHole),
  translate([wallWidth, 15, wallWidth + standHeight + 10], powerHole),
  translate([13, 40, -1], fanHoles)
)

const box = color([1,0.5,0.3, 0.8],
  difference(
    union( 
      difference(
      cube({size: [boxX, boxY, boxZ]}),
      translate([wallWidth, wallWidth, wallWidth], 
        cube({size: [
          boxX - wallWidth * 2, 
          boxY - wallWidth * 2, 
          boxZ - wallWidth
        ]}))
      ),
      translate([30.1 + standDiameter/2, 2.7 + standDiameter / 2, wallWidth], mksStands)
    ),
    holes
  ) 
)

function main () {
  return [
//    translate([30, 2.5, 2], electronics),
    translate([0, 0, 0], box)
  ]
}