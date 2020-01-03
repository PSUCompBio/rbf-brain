import sys
from plyfile import PlyData, PlyElement
import numpy as np

args = sys.argv
fileInp = str(args[1])

J0 = [2468, 3059, 12788, 131, 7789, 588, 5934, 1590, 1735]
J2 = np.cumsum(J0)+np.arange(9)

with open(fileInp, 'rb') as f:
    plydata = PlyData.read(f)
    X = []

# a = np.asarray(a)
    for J1 in J2:
        fID = J1//7
        rem = J1%7-3
        i1 = plydata['face'][fID][0][rem]
        vData = plydata['vertex'][i1]
        X.append(vData)

fw = open('parameters_new.prm', 'w')
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

x2 = 2*X[4][0]-X[5][0]
x10 = 2*X[4][0]-X[3][0]
x12 = 2*X[4][0]-X[6][0]

fw.write("deformed control points:  %.17f %.17f %.17f\n"% (X[5][0], X[5][1], X[5][2]))
fw.write("                          %.17f %.17f %.17f\n"% (x2, X[5][1], X[5][2]))
fw.write("                          %.17f %.17f %.17f\n"% (X[4][0], X[2][1], X[2][2]))
fw.write("                          %.17f %.17f %.17f\n"% (X[4][0], X[0][1], X[0][2]))
fw.write("                          %.17f %.17f %.17f\n"% (X[4][0], X[7][1], X[7][2]))
fw.write("                          %.17f %.17f %.17f\n"% (X[4][0], X[1][1], X[1][2]))
fw.write("                          %.17f %.17f %.17f\n"% (X[4][0], X[8][1], X[8][2]))
fw.write("                          %.17f %.17f %.17f\n"% (X[4][0], X[4][1], X[4][2]))
fw.write("                          %.17f %.17f %.17f\n"% (X[3][0], X[3][1], X[3][2]))
fw.write("                          %.17f %.17f %.17f\n"% (x10, X[3][1], X[3][2]))
fw.write("                          %.17f %.17f %.17f\n"% (X[6][0], X[6][1], X[6][2]))
fw.write("                          %.17f %.17f %.17f\n"% (x12, X[6][1], X[6][2]))
fw.close()
