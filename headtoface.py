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
parser = argparse.ArgumentParser(description='Obtaining transformation to move the Head ply file to line up with the Face ply file')
parser.add_argument('--inputhead', default=None, type=str, help="Path to your Head ply file")
parser.add_argument('--outputhead', default=None, type=str, help="Path to save the transformed Head ply file");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.inputhead  == None or args.outputhead == None):
    parser.print_help()
    sys.exit(0)
print("GENERATING TRANSFORMED HEAD");


head = args.inputhead
thead = args.outputhead


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PLY Reader'
headply = PLYReader(FileNames=[head])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1563, 776]

# show data in view
headplyDisplay = Show(headply, renderView1)

# trace defaults for the display properties.
headplyDisplay.Representation = 'Surface'
headplyDisplay.ColorArrayName = [None, '']
headplyDisplay.OSPRayScaleArray = 'TCoords'
headplyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
headplyDisplay.SelectOrientationVectors = 'None'
headplyDisplay.ScaleFactor = 0.0437952995300293
headplyDisplay.SelectScaleArray = 'None'
headplyDisplay.GlyphType = 'Arrow'
headplyDisplay.GlyphTableIndexArray = 'None'
headplyDisplay.GaussianRadius = 0.002189764976501465
headplyDisplay.SetScaleArray = ['POINTS', 'TCoords']
headplyDisplay.ScaleTransferFunction = 'PiecewiseFunction'
headplyDisplay.OpacityArray = ['POINTS', 'TCoords']
headplyDisplay.OpacityTransferFunction = 'PiecewiseFunction'
headplyDisplay.DataAxesGrid = 'GridAxesRepresentation'
headplyDisplay.SelectionCellLabelFontFile = ''
headplyDisplay.SelectionPointLabelFontFile = ''
headplyDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
headplyDisplay.DataAxesGrid.XTitleFontFile = ''
headplyDisplay.DataAxesGrid.YTitleFontFile = ''
headplyDisplay.DataAxesGrid.ZTitleFontFile = ''
headplyDisplay.DataAxesGrid.XLabelFontFile = ''
headplyDisplay.DataAxesGrid.YLabelFontFile = ''
headplyDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
headplyDisplay.PolarAxes.PolarAxisTitleFontFile = ''
headplyDisplay.PolarAxes.PolarAxisLabelFontFile = ''
headplyDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
headplyDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Transform'
transform1 = Transform(Input=headply)
transform1.Transform = 'Transform'

# Properties modified on transform1.Transform
transform1.Transform.Translate =  [0.025397, -0.112455, -0.034450]
# show data in view
transform1Display = Show(transform1, renderView1)

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = [None, '']
transform1Display.OSPRayScaleArray = 'TCoords'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 0.0437952995300293
transform1Display.SelectScaleArray = 'None'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'None'
transform1Display.GaussianRadius = 0.002189764976501465
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
Hide(headply, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData(thead, proxy=transform1, ColorArrayName=['POINTS', ''],
    LookupTable=None)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0013615041971206665, 0.0544624999165535, 1.8262578542302315]
renderView1.CameraFocalPoint = [-0.0013615041971206665, 0.0544624999165535, 0.011012498289346695]
renderView1.CameraParallelScale = 0.32089342917246433

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
