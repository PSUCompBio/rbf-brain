
import sys
import argparse



################# CLI ARGUMENT CONFIG ##################
# Setting up Argument parsing
parser = argparse.ArgumentParser(description='A Utility package to generate centroid text data from Coarse Mesh Morphed VTK')
parser.add_argument('--input', default=None, type=str, help="Path to your Morphed Mesh VTK")
parser.add_argument('--output', default=None, type=str, help="Path to save your Centroid Table Text Data");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.input  == None or args.output == None):
    parser.print_help()
    sys.exit(0)

morphed_mesh_vtk_file_path = args.input
centroid_table_text_file_path = args.output

fmorphed = open(morphed_mesh_vtk_file_path, 'r') #need a generic name here like mesh.vtk
foriginal = open('centroid_coarse.txt', 'r')
waste = fmorphed.readline()
waste = fmorphed.readline()
waste = fmorphed.readline()
waste = fmorphed.readline()
keep = fmorphed.readline()
a, b, c = keep.split(" ")
vertices = int(b)
lines = int(vertices/3)
lastline = vertices%3
nodes = [[0 for x in range(3)] for y in range(vertices)]
for i in range(0, vertices-2, 3):
    text = fmorphed.readline()
    p,q,r,s,t,u,v,w,x,y = text.split(" ")
    P = float(p)
    Q = float(q)
    R = float(r)
    S = float(s)
    T = float(t)
    U = float(u)
    V = float(v)
    W = float(w)
    X = float(x)
    nodes[i][0] = P
    nodes[i][1] = Q
    nodes[i][2] = R
    nodes[i+1][0] = S
    nodes[i+1][1] = T
    nodes[i+1][2] = U
    nodes[i+2][0] = V
    nodes[i+2][1] = W
    nodes[i+2][2] = X
if(lastline==0):
    text = fmorphed.readline()
    p,q,r,s,t,u,v,w,x,y = text.split(" ")
    P = float(p)
    Q = float(q)
    R = float(r)
    S = float(s)
    T = float(t)
    U = float(u)
    V = float(v)
    W = float(w)
    X = float(x)
    nodes[vertices-3][0] = P
    nodes[vertices-3][1] = Q
    nodes[vertices-3][2] = R
    nodes[vertices-2][0] = S
    nodes[vertices-2][1] = T
    nodes[vertices-2][2] = U
    nodes[vertices-1][0] = V
    nodes[vertices-1][1] = W
    nodes[vertices-1][2] = X
elif(lastline==1):
    text = fmorphed.readline()
    p,q,r,s = text.split(" ")
    P = float(p)
    Q = float(q)
    R = float(r)
    nodes[vertices-1][0] = P
    nodes[vertices-1][1] = Q
    nodes[vertices-1][2] = R
elif(lastline==2):
    text = fmorphed.readline()
    p,q,r,s,t,u,v = text.split(" ")
    P = float(p)
    Q = float(q)
    R = float(r)
    S = float(s)
    T = float(t)
    U = float(u)
    nodes[vertices-2][0] = P
    nodes[vertices-2][1] = Q
    nodes[vertices-2][2] = R
    nodes[vertices-1][0] = S
    nodes[vertices-1][1] = T
    nodes[vertices-1][2] = U
text = fmorphed.readline()
a, b, c = text.split(" ")
cells = int(b)
newcentroid = [[0 for x in range(4)] for y in range(cells)]
oldcentroid = [[0 for x in range(4)] for y in range(cells)]
for k in range(cells):
    text = fmorphed.readline()
    a,b,c,d,e,f,g,h,i,j = text.split(" ")
    B = int(b)
    C = int(c)
    D = int(d)
    E = int(e)
    F = int(f)
    G = int(g)
    H = int(h)
    I = int(i)
    xsum = nodes[B][0]+nodes[C][0]+nodes[D][0]+nodes[E][0]+nodes[F][0]+nodes[G][0]+nodes[H][0]+nodes[I][0]
    ysum = nodes[B][1]+nodes[C][1]+nodes[D][1]+nodes[E][1]+nodes[F][1]+nodes[G][1]+nodes[H][1]+nodes[I][1]
    zsum = nodes[B][2]+nodes[C][2]+nodes[D][2]+nodes[E][2]+nodes[F][2]+nodes[G][2]+nodes[H][2]+nodes[I][2]
    newcentroid[k][0] = k+1
    newcentroid[k][1] = xsum/8
    newcentroid[k][2] = ysum/8
    newcentroid[k][3] = zsum/8
    template = foriginal.readline()
    p,q,r,s = template.split(" ")
    oldcentroid[k][0] = float(q)
    oldcentroid[k][1] = float(r)
    oldcentroid[k][2] = float(s)
fmorphed.close()
foriginal.close()
fcentroid = open(centroid_table_text_file_path, 'w') #need another generic name here like centroidtable.txt
for i in range(cells):
    fcentroid.write("%d %f %f %f %f %f %f\n" % (i+1, newcentroid[i][1], newcentroid[i][2], newcentroid[i][3], oldcentroid[i][0], oldcentroid[i][1], oldcentroid[i][2]))
fcentroid.close()
