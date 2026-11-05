$fn=100; $fa=0.1;

H_b=2;

module tyouen(Hight,Width,Radius){
    union(){
        translate([-(Width-2*Radius)/2,0,0])cylinder(h=Hight,r=Radius);
        translate([(Width-2*Radius)/2,0,0])cylinder(h=Hight,r=Radius);
        translate([-(Width-2*Radius)/2,-Radius,0])cube([Width-2*Radius,2*Radius,Hight]);
    }
}

module bogopin(){
    color([1,1,0]){
        union(){
            cylinder(h=.5,r=1);
            cylinder(h=2.7,r=.75);
            cylinder(h=4-.45,r=.45);
            translate([0,0,4-.45])sphere(r=.45);
        }
    }
}

module part(){
    translate([18.2,-6.5,-4.4]) union(){
        bogopin();
        translate([1.5,2,0])bogopin();
        translate([3,0,0])bogopin();
        translate([4.5,2,0])bogopin();
    }

    translate([15-0.6,-8.85/2,5-2.6]) rotate([0,0,90])union(){
        cube([6.27,9.96,0.5]);
        color([0,0,0])translate([0,0,0.5])cube([8.85,9.96,0.7]);
    }

    translate([0,0,0]) rotate([90,0,-90]) union(){
        translate([0,0,H_b])tyouen(10.5-H_b,8.25,1.2);
        translate([0,0,0])tyouen(H_b,8.25,3.25/2);
    }
}

// translate([-203,45,-0.4])import("bsercon.stl");


color([1,1,1,.5])translate([-3,0,.7]) rotate([0,0,90])union(){
    difference(){
        translate([0,0,-0.7])tyouen(15,17,5);
        union(){
            translate([-5,-0.45,3])cube([10,0.9,20]);
            translate([-4.5,-3.5,3])cube([9,7,20]);
            translate([0,0,8])tyouen(10,15,4);
            translate([0,0,3]) rotate([0,180,0]) union(){
                translate([0,0,H_b])tyouen(10.5-H_b,8.5,1.2);
                translate([0,0,0])tyouen(H_b,8.5,3.25/2);
            }
        }
    }
}