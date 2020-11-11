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
parser = argparse.ArgumentParser(description='A Utility package to generate STL from PLY file')
parser.add_argument('--input', default=None, type=str, help="Path to your PLY (Model.ply)")
parser.add_argument('--output', default=None, type=str, help="Path to your output STL (Model.stl)");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.input  == None or args.output == None):
    parser.print_help()
    sys.exit(0)
print("GENERATING STL FROM PLY");


input_file = args.input
output_file = args.output


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PLY Reader'
modelply = PLYReader(FileNames=[input_file])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1515, 776]

# show data in view
modelplyDisplay = Show(modelply, renderView1)

# trace defaults for the display properties.
modelplyDisplay.Representation = 'Surface'
modelplyDisplay.ColorArrayName = [None, '']
modelplyDisplay.OSPRayScaleArray = 'TCoords'
modelplyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
modelplyDisplay.SelectOrientationVectors = 'None'
modelplyDisplay.ScaleFactor = 0.024037830531597137
modelplyDisplay.SelectScaleArray = 'None'
modelplyDisplay.GlyphType = 'Arrow'
modelplyDisplay.GlyphTableIndexArray = 'None'
modelplyDisplay.GaussianRadius = 0.0012018915265798568
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

# create a new 'Transform'
transform1 = Transform(Input=modelply)
transform1.Transform = 'Transform'

# Properties modified on transform1.Transform
transform1.Transform.Translate = [0.0, -0.328, -0.0415]
transform1.Transform.Rotate = [180.0, 0.0, 0.0]

# show data in view
transform1Display = Show(transform1, renderView1)

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = [None, '']
transform1Display.OSPRayScaleArray = 'TCoords'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 0.024037832021713258
transform1Display.SelectScaleArray = 'None'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'None'
transform1Display.GaussianRadius = 0.0012018916010856629
transform1Display.SetScaleArray = ['POINTS', 'TCoords']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'TCoords']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.SelectionCellLabelFontFile = ''
transform1Display.SelectionPointLabelFontFile = ''
transform1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
transform1Display.DataAxesGrid.XTitleFontFile = ''
transform1Display.DataAxesGrid.YTitleFontFile = ''
transform1Display.DataAxesGrid.ZTitleFontFile = ''
transform1Display.DataAxesGrid.XLabelFontFile = ''
transform1Display.DataAxesGrid.YLabelFontFile = ''
transform1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
transform1Display.PolarAxes.PolarAxisTitleFontFile = ''
transform1Display.PolarAxes.PolarAxisLabelFontFile = ''
transform1Display.PolarAxes.LastRadialAxisTextFontFile = ''
transform1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(modelply, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData(output_file, proxy=transform1, FileType='Ascii')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.00048365816473960876, -0.013336770236492157, 0.6907360276912337]
renderView1.CameraFocalPoint = [0.00048365816473960876, -0.013336770236492157, -0.0049173831939697266]
renderView1.CameraParallelScale = 0.18004835152761986

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
