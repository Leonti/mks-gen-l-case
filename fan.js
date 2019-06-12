const {cylinder, cube} = require('@jscad/csg/api').primitives3d
const {color} = require('@jscad/csg/api').color
const {difference, union} = require('@jscad/csg/api').booleanOps
const {translate} = require('@jscad/csg/api').transformations

const basePlate = color("brown", cube({size: [110, 84, 1.4]}))  

const holes = union(
  translate([0, 0, -1], cylinder({d:4.5, h:12})),
  translate([0, 32.5, -1], cylinder({d:4.5, h:12})),
  translate([32.5, 32.5, -1], cylinder({d:4.5, h:12})),
  translate([32.5, 0, -1], cylinder({d:4.5, h:12})) 
)

const body = color("gray", 
  cube({size: [40, 40, 10]})
)

const fan = difference(
  body, 
  translate([4, 4, 0], holes)
)

module.exports = {
  fan
}