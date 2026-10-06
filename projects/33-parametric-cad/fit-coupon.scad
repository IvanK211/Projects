// Small hole/peg clearance coupon. Print before modeling a functional mating assembly.
nominal=5;
gaps=[0.1,0.2,0.3,0.4];
$fn=48;
assert(nominal>0);
for(i=[0:len(gaps)-1]) {
  translate([i*16,0,0]) difference(){
    cube([14,14,4]);
    translate([7,7,-1]) cylinder(h=6,d=nominal+2*gaps[i]);
  }
}
translate([7,23,0]) cylinder(h=10,d=nominal);
