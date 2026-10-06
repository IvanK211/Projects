// Fictional open-top electronics tray. Not waterproof, mains-rated or load-certified.
// Dimensions are arbitrary reference choices, not recovered hardware dimensions.
part="base"; // [base,lid]
outer=[80,50,24];
wall=2;
floor_thickness=2;
clearance=0.35;
assert(min(outer)>2*wall && floor_thickness>0 && clearance>=0);
module base(){
  difference(){
    cube(outer);
    translate([wall,wall,floor_thickness])
      cube([outer[0]-2*wall,outer[1]-2*wall,outer[2]]);
  }
}
module lid(){
  union(){
    cube([outer[0],outer[1],floor_thickness]);
    translate([wall+clearance,wall+clearance,floor_thickness])
      difference(){
        cube([outer[0]-2*(wall+clearance),outer[1]-2*(wall+clearance),3]);
        translate([wall,wall,-0.1])
          cube([outer[0]-4*wall-2*clearance,outer[1]-4*wall-2*clearance,3.2]);
      }
  }
}
if(part=="base") base(); else if(part=="lid") lid(); else assert(false,"Choose base or lid");
