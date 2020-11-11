# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import sys
import argparse



################# CLI ARGUMENT CONFIG ##################
# Setting up Argument parsing
parser = argparse.ArgumentParser(description='Script to convert ply file to stl file')
parser.add_argument('--input', default=None, type=str, help="Path to your ply file (model.ply)")
parser.add_argument('--output', default=None, type=str, help="Path to your stl file (model.stl)");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.input  == None or args.output == None):
    parser.print_help()
    sys.exit(0)
print("CONVERTING FILE FROM PLY TO STL");


input_file = args.input
output_file = args.output

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PLY Reader'
modelply = PLYReader(FileNames=input_file)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1563, 776]

# show data in view
modelplyDisplay = Show(modelply, renderView1)

# trace defaults for the display properties.
modelplyDisplay.Representation = 'Surface'
modelplyDisplay.ColorArrayName = [None, '']
modelplyDisplay.OSPRayScaleArray = 'TCoords'
modelplyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
modelplyDisplay.SelectOrientationVectors = 'None'
modelplyDisplay.ScaleFactor = 0.023257534205913546
modelplyDisplay.SelectScaleArray = 'None'
modelplyDisplay.GlyphType = 'Arrow'
modelplyDisplay.GlyphTableIndexArray = 'None'
modelplyDisplay.GaussianRadius = 0.0011628767102956773
modelplyDisplay.SetScaleArray = ['POINTS', 'TCoords']
modelplyDisplay.ScaleTransferFunction = 'PiecewiseFunction'
modelplyDisplay.OpacityArray = ['POINTS', 'TCoords']
modelplyDisplay.OpacityTransferFunction = 'PiecewiseFunction'
modelplyDisplay.DataAxesGrid = 'GridAxesRepresentation'
modelplyDisplay.SelectionCellLabelFontFile = ''
modelplyDisplay.SelectionPointLabelFontFile = ''
modelplyDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
modelplyDisplay.DataAxesGrid.XTitleFontFile = ''
modelplyDisplay.DataAxesGrid.YTitleFontFile = ''
modelplyDisplay.DataAxesGrid.ZTitleFontFile = ''
modelplyDisplay.DataAxesGrid.XLabelFontFile = ''
modelplyDisplay.DataAxesGrid.YLabelFontFile = ''
modelplyDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
modelplyDisplay.PolarAxes.PolarAxisTitleFontFile = ''
modelplyDisplay.PolarAxes.PolarAxisLabelFontFile = ''
modelplyDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData(output_file, proxy=modelply, FileType='Ascii')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.6811726195509455, -0.039651596423712715, 0.12482516793668763]
renderView1.CameraFocalPoint = [0.00032395869493484497, -0.01040361076593399, -0.0028440505266189575]
renderView1.CameraViewUp = [0.04626192541972582, 0.998768938758061, -0.017900872284787782]
renderView1.CameraParallelScale = 0.17944762151420837

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
