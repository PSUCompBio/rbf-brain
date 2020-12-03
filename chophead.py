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
parser = argparse.ArgumentParser(description='Chopping Head to remove unnecesary node points fo lining up head to face; also storing the head ply file as ascii for future use')
parser.add_argument('--input', default=None, type=str, help="Path to your Head ply file")
parser.add_argument('--output', default=None, type=str, help="Path to save the chopped Head stl file");
parser.add_argument('--outputascii', default=None, type=str, help="Path to save the Head ply ascii file");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.input  == None or args.output == None or args.outputascii == None):
    parser.print_help()
    sys.exit(0)
print("GENERATING CHOPPED HEAD");


input = args.input
output = args.output
outputascii = args.outputascii

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PLY Reader'
modelply = PLYReader(FileNames=input)

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
modelplyDisplay.ScaleFactor = 0.04566257148981095
modelplyDisplay.SelectScaleArray = 'None'
modelplyDisplay.GlyphType = 'Arrow'
modelplyDisplay.GlyphTableIndexArray = 'None'
modelplyDisplay.GaussianRadius = 0.0022831285744905473
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

# create a new 'Clip'
clip1 = Clip(Input=modelply)
clip1.ClipType = 'Plane'
clip1.Scalars = [None, '']

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [-0.0012623295187950134, 0.05791253596544266, 0.0060445889830589294]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [-0.0013615041971206665, 0.0544624999165535, 0.011012498289346695]
clip1.ClipType.Normal = [0.0, -1.0, 0.0]

# Properties modified on clip1
clip1.Scalars = ['POINTS', '']

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [-0.0013615041971206665, 0.0544624999165535, 0.011012498289346695]
clip1.ClipType.Normal = [0.0, -1.0, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.OSPRayScaleArray = 'TCoords'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.02281668409705162
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.0011408342048525812
clip1Display.SetScaleArray = ['POINTS', 'TCoords']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'TCoords']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.012984257715649804

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(modelply, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=clip1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.ColorArrayName = [None, '']
extractSurface1Display.OSPRayScaleArray = 'TCoords'
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.SelectOrientationVectors = 'None'
extractSurface1Display.ScaleFactor = 0.02281668409705162
extractSurface1Display.SelectScaleArray = 'None'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.GlyphTableIndexArray = 'None'
extractSurface1Display.GaussianRadius = 0.0011408342048525812
extractSurface1Display.SetScaleArray = ['POINTS', 'TCoords']
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityArray = ['POINTS', 'TCoords']
extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface1Display.SelectionCellLabelFontFile = ''
extractSurface1Display.SelectionPointLabelFontFile = ''
extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface1Display.DataAxesGrid.XTitleFontFile = ''
extractSurface1Display.DataAxesGrid.YTitleFontFile = ''
extractSurface1Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface1Display.DataAxesGrid.XLabelFontFile = ''
extractSurface1Display.DataAxesGrid.YLabelFontFile = ''
extractSurface1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface1Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface1Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface1Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData(output, proxy=extractSurface1, FileType='Ascii')

# hide data in view
Hide(extractSurface1, renderView1)

# set active source
SetActiveSource(modelply)

# show data in view
modelplyDisplay = Show(modelply, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# save data
SaveData(outputascii, proxy=modelply, FileType='Ascii',    ColorArrayName=['POINTS', ''],
    LookupTable=None)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0012623295187950134, 0.05791253596544266, 1.273002544146821]
renderView1.CameraFocalPoint = [-0.0012623295187950134, 0.05791253596544266, 0.0060445889830589294]
renderView1.CameraParallelScale = 0.3279128481405272

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
