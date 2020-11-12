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
parser.add_argument('--input', default=None, type=str, help="Path to your VTK (coarse_brain.vtk)")
parser.add_argument('--output', default=None, type=str, help="Path to your output rotated VTK (rotated_coarse_brain.vtk)");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.input  == None or args.output == None):
    parser.print_help()
    sys.exit(0)
print("ROTATED MESH");


input_file = args.input
output_file = args.output


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
meshvtk = LegacyVTKReader(FileNames=[input_file])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1515, 776]

# show data in view
meshvtkDisplay = Show(meshvtk, renderView1)

# get color transfer function/color map for 'PartID'
partIDLUT = GetColorTransferFunction('PartID')

# get opacity transfer function/opacity map for 'PartID'
partIDPWF = GetOpacityTransferFunction('PartID')

# trace defaults for the display properties.
meshvtkDisplay.Representation = 'Surface'
meshvtkDisplay.ColorArrayName = ['CELLS', 'PartID']
meshvtkDisplay.LookupTable = partIDLUT
meshvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
meshvtkDisplay.SelectOrientationVectors = 'None'
meshvtkDisplay.ScaleFactor = 0.01650931015610695
meshvtkDisplay.SelectScaleArray = 'PartID'
meshvtkDisplay.GlyphType = 'Arrow'
meshvtkDisplay.GlyphTableIndexArray = 'PartID'
meshvtkDisplay.GaussianRadius = 0.0008254655078053474
meshvtkDisplay.SetScaleArray = [None, '']
meshvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
meshvtkDisplay.OpacityArray = [None, '']
meshvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
meshvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
meshvtkDisplay.SelectionCellLabelFontFile = ''
meshvtkDisplay.SelectionPointLabelFontFile = ''
meshvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
meshvtkDisplay.ScalarOpacityFunction = partIDPWF
meshvtkDisplay.ScalarOpacityUnitDistance = 0.009947062750141499

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
meshvtkDisplay.DataAxesGrid.XTitleFontFile = ''
meshvtkDisplay.DataAxesGrid.YTitleFontFile = ''
meshvtkDisplay.DataAxesGrid.ZTitleFontFile = ''
meshvtkDisplay.DataAxesGrid.XLabelFontFile = ''
meshvtkDisplay.DataAxesGrid.YLabelFontFile = ''
meshvtkDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
meshvtkDisplay.PolarAxes.PolarAxisTitleFontFile = ''
meshvtkDisplay.PolarAxes.PolarAxisLabelFontFile = ''
meshvtkDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
meshvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
meshvtkDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Transform'
transform1 = Transform(Input=meshvtk)
transform1.Transform = 'Transform'

# Properties modified on transform1.Transform
transform1.Transform.Translate = [0.0, -0.328, -0.0415]
transform1.Transform.Rotate = [180.0, 0.0, 0.0]

# show data in view
transform1Display = Show(transform1, renderView1)

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = ['CELLS', 'PartID']
transform1Display.LookupTable = partIDLUT
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 0.016509310528635978
transform1Display.SelectScaleArray = 'None'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'None'
transform1Display.GaussianRadius = 0.0008254655264317989
transform1Display.SetScaleArray = [None, '']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = [None, '']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.SelectionCellLabelFontFile = ''
transform1Display.SelectionPointLabelFontFile = ''
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.ScalarOpacityFunction = partIDPWF
transform1Display.ScalarOpacityUnitDistance = 0.009947062843542262

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
Hide(meshvtk, renderView1)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# save data
SaveData(output_file, proxy=transform1, FileType='Ascii')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.9001384973526e-05, 0.03535250654816627, 0.4739811780341929]
renderView1.CameraFocalPoint = [-2.9001384973526e-05, 0.03535250654816627, -0.020432548597455025]
renderView1.CameraParallelScale = 0.12796368861238183

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
