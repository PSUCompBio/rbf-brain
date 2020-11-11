import argparse
################# CLI ARGUMENT CONFIG ##################
# Setting up Argument parsing
parser = argparse.ArgumentParser(description='Script to generate pvpython script that will line up head model with face model')
parser.add_argument('--inputhead', default=None, type=str, help="Path to head stl file");
parser.add_argument('--inputface', default=None, type=str, help="Path to face stl file");
args = parser.parse_args()

#########################################################
# If arguments are invalid or none then exit the script with error !

if (args.inputhead  == None or args.inputface == None):
    parser.print_help()
    sys.exit(0)

headpath = args.inputhead
facepath = args.inputface
xnose = 0
ynose = 0
znose = 0
with open(headpath) as head:
    for line in head:
        linenew = line.lstrip()
        if linenew.startswith('vertex'):
            a,xstr,ystr,zstr = line.split()
            x = float(xstr)
            y = float(ystr)
            z = float(zstr)
            if (z>znose):
                xnose = x
                ynose = y
                znose = z
xhead = xnose
yhead = ynose
zhead = znose
xnose = 0
ynose = 0
znose = 0
with open(facepath) as face:
    for line in face:
        linenew = line.lstrip()
        if linenew.startswith('vertex'):
            a,xstr,ystr,zstr = line.split()
            x = float(xstr)
            y = float(ystr)
            z = float(zstr)
            if (z>znose):
                xnose = x
                ynose = y
                znose = z
xface = xnose
yface = ynose
zface = znose
xdist = xface - xhead
ydist = yface - yhead
zdist = zface - zhead
headtoface = open('headtoface.py', 'w')
with open('templateheadtoface.py', 'r') as transform:
    for line in transform:
        if line.startswith('transform1.Transform.Translate'):
            headtoface.write("transform1.Transform.Translate =  [%f, %f, %f]" %(xdist, ydist, zdist))
        else:
            headtoface.write(line)
headtoface.close()
