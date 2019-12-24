
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('matplotlib', 'inline')
from pygem import RBFParameters, RBF, StlHandler, VtkHandler
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse


################# CLI ARGUMENT CONFIG ##################
# Setting up Argument parsing
parser = argparse.ArgumentParser(description='A Utility package to generate Morphed Mesh VTK from Parameters (PRM) & Coarse Mesh (VTK) file')
parser.add_argument('--p', default=None, type=str, help="Path to your Paramaters file (e.g. parameters.prm)")
parser.add_argument('--m', default=None, type=str, help="Path to your Coarse-Mesh VTK File");
parser.add_argument('--output', default=None, type=str, help="Path to save your Morphed VTK File (e.g. coarse_morphed_mesh.vtk)");
args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.p  == None or args.m == None or args.output == None):
    parser.print_help()
    sys.exit(0)

parameter_file_path = args.p
mesh_file_path = args.m
output_morphed_vtk_path = args.output





cwd = os.getcwd()
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)


# In[2]:


params = RBFParameters()
params.read_parameters(parameter_file_path)


# In[2]:


vtk_handler = VtkHandler()
mesh = vtk_handler.parse(mesh_file_path)


# In[4]:


rbf = RBF(params, mesh)
rbf.perform()
new_mesh_points = rbf.modified_mesh_points
vtk_handler.write(new_mesh_points, output_morphed_vtk_path)
