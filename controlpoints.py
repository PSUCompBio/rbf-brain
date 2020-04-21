
import sys
import argparse



################# CLI ARGUMENT CONFIG ##################
# Setting up Argument parsing
parser = argparse.ArgumentParser(description='A Utility package file to generate parameters file which is used by RBF Scaling Code')
parser.add_argument('--input', default=None, type=str, help="Path to your STL (Model.stl)")
parser.add_argument('--output', default=None, type=str, help="Path to your Parameter File (parameters.prm)");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.input  == None or args.output == None):
    parser.print_help()
    sys.exit(0)

input_file = args.input
output_file = args.output



fr = open(input_file, 'r')
fw = open(output_file, 'w')
fw.write("[Radial Basis Functions]\n")
fw.write("basis function: polyharmonic_spline\n")
fw.write("radius: 2\n")
fw.write("power: 1\n\n")
fw.write("[Control points]\n\n")
fw.write("original control points:  0 0.016584 0.075011\n")
fw.write("                          0 0.031053 0.076372\n")
fw.write("                          0 0.047411 0.072255\n")
fw.write("                          -0.0279352 0.026812 0.070838\n")
fw.write("                          0 0.091122 0.0272437\n")
fw.write("                          -0.0461743 0.025816 0.0539813\n")
fw.write("                          -0.0210379 0.08391 0.0348771\n")
fw.write("                          0 0.0985704 0.00368058\n")
fw.write("                          0 0.099913 -0.0257866\n")
fw.write("                          0 0.096007 -0.0502764\n")
fw.write("                          -0.0276852 0.087927 -0.0486875\n")
fw.write("                          -0.0411181 0.058758 0.0466437\n")
fw.write("                          -0.059702 0.055669 -0.0223894\n")
fw.write("                          0 0.083373 -0.072815\n")
fw.write("                          0 0.062853 -0.0880947\n")
fw.write("                          -0.0536963 0.025614 0.0250154\n")
fw.write("                          -0.0533499 0.036906 -0.06624\n")
fw.write("                          -0.0625905 0.022682 -0.0089409\n")
fw.write("                          -0.0619482 0.016179 -0.0453949\n")
fw.write("                          -0.0206065 0.027631 -0.0922652\n")
fw.write("                          0 0.041498 -0.0951818\n")
fw.write("                          -0.0425306 0.006741 -0.0787254\n")
fw.write("                          0 0.00884 -0.093202\n")
fw.write("                          0 -0.044087 -0.0127582\n")
fw.write("                          0 -0.007478 -0.0870864\n")
fw.write("                          0 -0.02233899 -0.0637847\n")
fw.write("                          0 -0.03823 -0.0748673\n")
fw.write("                          0.0625905 0.022682 -0.0089409\n")
fw.write("                          0.0619482 0.016179 -0.0453949\n")
fw.write("                          0.059702 0.055669 -0.0223894\n")
fw.write("                          0.0533499 0.036906 -0.06624\n")
fw.write("                          0.0411181 0.058758 0.0466437\n")
fw.write("                          0.0276852 0.087927 -0.0486875\n")
fw.write("                          0.0210379 0.08391 0.0348771\n")
fw.write("                          0.0206065 0.027631 -0.0922652\n")
fw.write("                          0.0536963 0.025614 0.0250154\n")
fw.write("                          0.0461743 0.025816 0.0539813\n")
fw.write("                          0.0425306 0.006741 -0.0787254\n")
fw.write("                          0.0279352 0.026812 0.070838\n\n")
for i in range(2468):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x1,y1,z1 = numbers.split(" ")
for i in range(1994):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x2,y2,z2 = numbers.split(" ")
for i in range(1064):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x3,y3,z3 = numbers.split(" ")
for i in range(3791):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x4,y4,z4 = numbers.split(" ")
for i in range(3039):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x5,y5,z5 = numbers.split(" ")
for i in range(5718):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x6,y6,z6 = numbers.split(" ")
for i in range(181):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x7,y7,z7 = numbers.split(" ")
for i in range(55):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x8,y8,z8 = numbers.split(" ")
for i in range(3058):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x9,y9,z9 = numbers.split(" ")
for i in range(3261):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x10,y10,z10 = numbers.split(" ")
for i in range(33):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x11,y11,z11 = numbers.split(" ")
for i in range(103):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x12,y12,z12 = numbers.split(" ")
for i in range(818):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x13,y13,z13 = numbers.split(" ")
for i in range(643):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x14,y14,z14 = numbers.split(" ")
for i in range(3171):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x15,y15,z15 = numbers.split(" ")
for i in range(698):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x16,y16,z16 = numbers.split(" ")
for i in range(1455):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x17,y17,z17 = numbers.split(" ")
for i in range(427):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x18,y18,z18 = numbers.split(" ")
for i in range(551):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x19,y19,z19 = numbers.split(" ")
for i in range(97):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x20,y20,z20 = numbers.split(" ")
for i in range(29):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x21,y21,z21 = numbers.split(" ")
for i in range(3037):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x22,y22,z22 = numbers.split(" ")
for i in range(55):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x23,y23,z23 = numbers.split(" ")
for i in range(321):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x24,y24,z24 = numbers.split(" ")
for i in range(979):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x25,y25,z25 = numbers.split(" ")
for i in range(1307):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x26,y26,z26 = numbers.split(" ")
for i in range(2351):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x27,y27,z27 = numbers.split(" ")
x28 = 0.0-float(x18)
x29 = 0.0-float(x19)
x30 = 0.0-float(x13)
x31 = 0.0-float(x17)
x32 = 0.0-float(x12)
x33 = 0.0-float(x11)
x34 = 0.0-float(x7)
x35 = 0.0-float(x20)
x36 = 0.0-float(x16)
x37 = 0.0-float(x6)
x38 = 0.0-float(x22)
x39 = 0.0-float(x4)
fr.close()
fw.write("deformed control points:  %s %s %s" % (0, y1, z1))
fw.write("                          %s %s %s" % (0, y2, z2))
fw.write("                          %s %s %s" % (0, y3, z3))
fw.write("                          %s %s %s" % (x4, y4, z4))
fw.write("                          %s %s %s" % (0, y5, z5))
fw.write("                          %s %s %s" % (x6, y6, z6))
fw.write("                          %s %s %s" % (x7, y7, z7))
fw.write("                          %s %s %s" % (0, y8, z8))
fw.write("                          %s %s %s" % (0, y9, z9))
fw.write("                          %s %s %s" % (0, y10, z10))
fw.write("                          %s %s %s" % (x11, y11, z11))
fw.write("                          %s %s %s" % (x12, y12, z12))
fw.write("                          %s %s %s" % (x13, y13, z13))
fw.write("                          %s %s %s" % (0, y14, z14))
fw.write("                          %s %s %s" % (0, y15, z15))
fw.write("                          %s %s %s" % (x16, y16, z16))
fw.write("                          %s %s %s" % (x17, y17, z17))
fw.write("                          %s %s %s" % (x18, y18, z18))
fw.write("                          %s %s %s" % (x19, y19, z19))
fw.write("                          %s %s %s" % (x20, y20, z20))
fw.write("                          %s %s %s" % (0, y21, z21))
fw.write("                          %s %s %s" % (x22, y22, z22))
fw.write("                          %s %s %s" % (0, y23, z23))
fw.write("                          %s %s %s" % (0, y24, z24))
fw.write("                          %s %s %s" % (0, y25, z25))
fw.write("                          %s %s %s" % (0, y26, z26))
fw.write("                          %s %s %s" % (0, y27, z27))
fw.write("                          %s %s %s" % (x28, y18, z18))
fw.write("                          %s %s %s" % (x29, y19, z19))
fw.write("                          %s %s %s" % (x30, y13, z13))
fw.write("                          %s %s %s" % (x31, y17, z17))
fw.write("                          %s %s %s" % (x32, y12, z12))
fw.write("                          %s %s %s" % (x33, y11, z11))
fw.write("                          %s %s %s" % (x34, y7, z7))
fw.write("                          %s %s %s" % (x35, y20, z20))
fw.write("                          %s %s %s" % (x36, y16, z16))
fw.write("                          %s %s %s" % (x37, y6, z6))
fw.write("                          %s %s %s" % (x38, y22, z22))
fw.write("                          %s %s %s" % (x39, y4, z4))
fw.close()
