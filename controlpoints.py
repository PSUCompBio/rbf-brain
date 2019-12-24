
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
fw.write("original control points:  0.0628782 0.015671 -0.0100175\n")
fw.write("                          -0.0628782 0.015671 -0.0100175\n")
fw.write("                          0.0 0.100023 -0.0145602\n")
fw.write("                          0.0 0.016584 0.075011\n")
fw.write("                          0.0 0.029327 -0.0959088\n")
fw.write("                          0.0 0.047411 0.072255\n")
fw.write("                          0.0 -0.044087 -0.0127582\n")
fw.write("                          0.0 0.083373 -0.072815\n")
fw.write("                          0.0313799 0.061778 0.056319\n")
fw.write("                          -0.0313799 0.061778 0.056319\n")
fw.write("                          0.0555525 0.018242 -0.062097\n")
fw.write("                          -0.0555525 0.018242 -0.062097\n\n")
for i in range(2468):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x4,y4,z4 = numbers.split(" ")
for i in range(3059):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x6,y6,z6 = numbers.split(" ")
for i in range(12788):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x3,y3,z3 = numbers.split(" ")
for i in range(131):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x9,y9,z9 = numbers.split(" ")
for i in range(7789):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x8,y8,z8 = numbers.split(" ")
for i in range(588):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x1,y1,z1 = numbers.split(" ")
for i in range(5934):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x11,y11,z11 = numbers.split(" ")
for i in range(1590):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x5,y5,z5 = numbers.split(" ")
for i in range(1735):
    waste = fr.readline()
numbers = fr.readline()
a,b,c,d,x7,y7,z7 = numbers.split(" ")
x2 = 2*float(x8)-float(x1)
x10 = 2*float(x8)-float(x9)
x12 = 2*float(x8)-float(x11)
fr.close()
fw.write("deformed control points:  %s %s %s" % (x1, y1, z1))
fw.write("                          %f %s %s" % (x2, y1, z1))
fw.write("                          %s %s %s" % (x8, y3, z3))
fw.write("                          %s %s %s" % (x8, y4, z4))
fw.write("                          %s %s %s" % (x8, y5, z5))
fw.write("                          %s %s %s" % (x8, y6, z6))
fw.write("                          %s %s %s" % (x8, y7, z7))
fw.write("                          %s %s %s" % (x8, y8, z8))
fw.write("                          %s %s %s" % (x9, y9, z9))
fw.write("                          %f %s %s" % (x10, y9, z9))
fw.write("                          %s %s %s" % (x11, y11, z11))
fw.write("                          %f %s %s" % (x12, y11, z11))
fw.close()
