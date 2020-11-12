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
parser = argparse.ArgumentParser(description='Script to chop of unnecesary region in head model')
parser.add_argument('--input', default=None, type=str, help="Path to your head stl file (head.stl)")
parser.add_argument('--output', default=None, type=str, help="Path to your chopped head stl file (choppedhead.stl)");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.input  == None or args.output == None):
    parser.print_help()
    sys.exit(0)
print("CHOPPING HEAD");


input_file = args.input
output_file = args.output

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'STL Reader'
model = STLReader(FileNames=[input_file])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1563, 776]

# show data in view
modelDisplay = Show(model, renderView1)

# get color transfer function/color map for 'STLSolidLabeling'
sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')

# trace defaults for the display properties.
modelDisplay.Representation = 'Surface'
modelDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
modelDisplay.LookupTable = sTLSolidLabelingLUT
modelDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
modelDisplay.SelectOrientationVectors = 'None'
modelDisplay.ScaleFactor = 0.0437952995300293
modelDisplay.SelectScaleArray = 'STLSolidLabeling'
modelDisplay.GlyphType = 'Arrow'
modelDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
modelDisplay.GaussianRadius = 0.002189764976501465
modelDisplay.SetScaleArray = [None, '']
modelDisplay.ScaleTransferFunction = 'PiecewiseFunction'
modelDisplay.OpacityArray = [None, '']
modelDisplay.OpacityTransferFunction = 'PiecewiseFunction'
modelDisplay.DataAxesGrid = 'GridAxesRepresentation'
modelDisplay.SelectionCellLabelFontFile = ''
modelDisplay.SelectionPointLabelFontFile = ''
modelDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
modelDisplay.DataAxesGrid.XTitleFontFile = ''
modelDisplay.DataAxesGrid.YTitleFontFile = ''
modelDisplay.DataAxesGrid.ZTitleFontFile = ''
modelDisplay.DataAxesGrid.XLabelFontFile = ''
modelDisplay.DataAxesGrid.YLabelFontFile = ''
modelDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
modelDisplay.PolarAxes.PolarAxisTitleFontFile = ''
modelDisplay.PolarAxes.PolarAxisLabelFontFile = ''
modelDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
modelDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
modelDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'STLSolidLabeling'
sTLSolidLabelingPWF = GetOpacityTransferFunction('STLSolidLabeling')

# create a new 'Clip'
clip1 = Clip(Input=model)
clip1.ClipType = 'Plane'
clip1.Scalars = ['CELLS', 'STLSolidLabeling']

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [-0.0013615041971206665, 0.0544624999165535, 0.011012498289346695]

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, -1.0, 0.0]

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, -1.0, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['CELLS', 'STLSolidLabeling']
clip1Display.LookupTable = sTLSolidLabelingLUT
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.02416646257042885
clip1Display.SelectScaleArray = 'STLSolidLabeling'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'STLSolidLabeling'
clip1Display.GaussianRadius = 0.0012083231285214425
clip1Display.SetScaleArray = [None, '']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = [None, '']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = sTLSolidLabelingPWF
clip1Display.ScalarOpacityUnitDistance = 0.014576333985766372

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
Hide(model, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=clip1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.ColorArrayName = ['CELLS', 'STLSolidLabeling']
extractSurface1Display.LookupTable = sTLSolidLabelingLUT
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.SelectOrientationVectors = 'None'
extractSurface1Display.ScaleFactor = 0.02416646257042885
extractSurface1Display.SelectScaleArray = 'STLSolidLabeling'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.GlyphTableIndexArray = 'STLSolidLabeling'
extractSurface1Display.GaussianRadius = 0.0012083231285214425
extractSurface1Display.SetScaleArray = [None, '']
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityArray = [None, '']
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

# show color bar/color legend
extractSurface1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData(output_file, proxy=extractSurface1, FileType='Ascii')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.2411985070937017, 0.0544624999165535, 0.011012498289346695]
renderView1.CameraFocalPoint = [-0.0013615041971206665, 0.0544624999165535, 0.011012498289346695]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.32089342917246433

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
