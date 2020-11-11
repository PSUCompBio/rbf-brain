import argparse
################# CLI ARGUMENT CONFIG ##################
# Setting up Argument parsing
parser = argparse.ArgumentParser(description='Script to add texture to transformed head ply file')
parser.add_argument('--inputheadoriginal', default=None, type=str, help="Path to original head ply file (ascii)");
parser.add_argument('--inputheadtrans', default=None, type=str, help="Path to tansformed head ply file");
parser.add_argument('--outputheadtransUV', default=None, type=str, help="Path to transformed head ply file with UV data");
args = parser.parse_args()

#########################################################
# If arguments are invalid or none then exit the script with error !

if (args.inputheadoriginal  == None or args.inputheadtrans == None or args.outputheadtransUV == None):
    parser.print_help()
    sys.exit(0)

orihead = args.inputheadoriginal
transhead = args.inputheadtrans
transheaduv = args.outputheadtransUV
with open(orihead) as original:
    for line in original:
        if line.startswith("element vertex"):
            a, b, c = line.split()
            nnodes = int(c)
        if line.startswith("element face"):
            d, e, f = line.split()
            nel = int(f)
        if line.startswith('end'):
            break
    nodes = [[0]*5 for i in range(nnodes)]
    count = 0
    for line in original:
        nodes[count][:] = line.split()
        count = count + 1
        if (count == nnodes):
            break
    elements = [[0]*4 for i in range(nel)]
    count = 0
    for line in original:
        elements[count][:] = line.split()
        count = count + 1
        if (count == nel):
            break
with open(transhead) as trans:
    for line in trans:
        if line.startswith('end'):
            break
    tnodes = [[0]*3 for i in range(nnodes)]
    count = 0
    for line in trans:
        tnodes[count][:] = line.split()
        count = count + 1
        if (count == nnodes):
            break
transuv = open(transheaduv, 'w')
transuv.write("ply\n")
transuv.write("format ascii 1.0\n")
transuv.write("comment VCGLIB generated\n")
transuv.write("comment TextureFile model.jpg\n")
transuv.write("element vertex %d\n" %nnodes)
transuv.write("property float x\n")
transuv.write("property float y\n")
transuv.write("property float z\n")
transuv.write("element face %d\n" %nel)
transuv.write("property list uchar int vertex_indices\n")
transuv.write("property list uchar float texcoord\n")
transuv.write("end_header\n")
for i in range(nnodes):
    transuv.write("%s %s %s\n" %(tnodes[i][0], tnodes[i][1], tnodes[i][2]))
for i in range(nel):
    transuv.write("3 %s %s %s 6 %s %s %s %s %s %s\n" %(elements[i][1], elements[i][2], elements[i][3], nodes[int(elements[i][1])][3], nodes[int(elements[i][1])][4], nodes[int(elements[i][2])][3], nodes[int(elements[i][2])][4], nodes[int(elements[i][3])][3], nodes[int(elements[i][3])][4]))
