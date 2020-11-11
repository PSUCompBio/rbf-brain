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
parser.add_argument('--input', default=None, type=str, help="Path to your Mesh (.vtk file)")
parser.add_argument('--outputskull', default=None, type=str, help="Path to your output skull PLY (skull.ply)");
parser.add_argument('--outputbrain', default=None, type=str, help="Path to your output brain PLY (brain.ply)");

args = parser.parse_args()

#########################################################

# If arguments are invalid or none then exit the script with error !

if (args.input  == None or args.outputskull == None or args.outputbrain == None):
    parser.print_help()
    sys.exit(0)
print("GENERATING PLY FROM VTK");


input_file = args.input
outputskull_file = args.outputskull
outputbrain_file = args.outputbrain


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
brain_rotatedvtk = LegacyVTKReader(FileNames=[input_file])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1563, 776]

# show data in view
brain_rotatedvtkDisplay = Show(brain_rotatedvtk, renderView1)

# trace defaults for the display properties.
brain_rotatedvtkDisplay.Representation = 'Surface'
brain_rotatedvtkDisplay.AmbientColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.ColorArrayName = [None, '']
brain_rotatedvtkDisplay.DiffuseColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.LookupTable = None
brain_rotatedvtkDisplay.MapScalars = 1
brain_rotatedvtkDisplay.MultiComponentsMapping = 0
brain_rotatedvtkDisplay.InterpolateScalarsBeforeMapping = 1
brain_rotatedvtkDisplay.Opacity = 1.0
brain_rotatedvtkDisplay.PointSize = 2.0
brain_rotatedvtkDisplay.LineWidth = 1.0
brain_rotatedvtkDisplay.RenderLinesAsTubes = 0
brain_rotatedvtkDisplay.RenderPointsAsSpheres = 0
brain_rotatedvtkDisplay.Interpolation = 'Gouraud'
brain_rotatedvtkDisplay.Specular = 0.0
brain_rotatedvtkDisplay.SpecularColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.SpecularPower = 100.0
brain_rotatedvtkDisplay.Luminosity = 0.0
brain_rotatedvtkDisplay.Ambient = 0.0
brain_rotatedvtkDisplay.Diffuse = 1.0
brain_rotatedvtkDisplay.EdgeColor = [0.0, 0.0, 0.5]
brain_rotatedvtkDisplay.BackfaceRepresentation = 'Follow Frontface'
brain_rotatedvtkDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.BackfaceOpacity = 1.0
brain_rotatedvtkDisplay.Position = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.Scale = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.Orientation = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.Origin = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.Pickable = 1
brain_rotatedvtkDisplay.Texture = None
brain_rotatedvtkDisplay.Triangulate = 0
brain_rotatedvtkDisplay.UseShaderReplacements = 0
brain_rotatedvtkDisplay.ShaderReplacements = ''
brain_rotatedvtkDisplay.NonlinearSubdivisionLevel = 1
brain_rotatedvtkDisplay.UseDataPartitions = 0
brain_rotatedvtkDisplay.OSPRayUseScaleArray = 0
brain_rotatedvtkDisplay.OSPRayScaleArray = ''
brain_rotatedvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
brain_rotatedvtkDisplay.OSPRayMaterial = 'None'
brain_rotatedvtkDisplay.Orient = 0
brain_rotatedvtkDisplay.OrientationMode = 'Direction'
brain_rotatedvtkDisplay.SelectOrientationVectors = 'None'
brain_rotatedvtkDisplay.Scaling = 0
brain_rotatedvtkDisplay.ScaleMode = 'No Data Scaling Off'
brain_rotatedvtkDisplay.ScaleFactor = 0.016502300277352333
brain_rotatedvtkDisplay.SelectScaleArray = 'None'
brain_rotatedvtkDisplay.GlyphType = 'Arrow'
brain_rotatedvtkDisplay.UseGlyphTable = 0
brain_rotatedvtkDisplay.GlyphTableIndexArray = 'None'
brain_rotatedvtkDisplay.UseCompositeGlyphTable = 0
brain_rotatedvtkDisplay.UseGlyphCullingAndLOD = 0
brain_rotatedvtkDisplay.LODValues = []
brain_rotatedvtkDisplay.ColorByLODIndex = 0
brain_rotatedvtkDisplay.GaussianRadius = 0.0008251150138676167
brain_rotatedvtkDisplay.ShaderPreset = 'Sphere'
brain_rotatedvtkDisplay.CustomTriangleScale = 3
brain_rotatedvtkDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
brain_rotatedvtkDisplay.Emissive = 0
brain_rotatedvtkDisplay.ScaleByArray = 0
brain_rotatedvtkDisplay.SetScaleArray = [None, '']
brain_rotatedvtkDisplay.ScaleArrayComponent = 0
brain_rotatedvtkDisplay.UseScaleFunction = 1
brain_rotatedvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
brain_rotatedvtkDisplay.OpacityByArray = 0
brain_rotatedvtkDisplay.OpacityArray = [None, '']
brain_rotatedvtkDisplay.OpacityArrayComponent = 0
brain_rotatedvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
brain_rotatedvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
brain_rotatedvtkDisplay.SelectionCellLabelBold = 0
brain_rotatedvtkDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
brain_rotatedvtkDisplay.SelectionCellLabelFontFamily = 'Arial'
brain_rotatedvtkDisplay.SelectionCellLabelFontFile = ''
brain_rotatedvtkDisplay.SelectionCellLabelFontSize = 18
brain_rotatedvtkDisplay.SelectionCellLabelItalic = 0
brain_rotatedvtkDisplay.SelectionCellLabelJustification = 'Left'
brain_rotatedvtkDisplay.SelectionCellLabelOpacity = 1.0
brain_rotatedvtkDisplay.SelectionCellLabelShadow = 0
brain_rotatedvtkDisplay.SelectionPointLabelBold = 0
brain_rotatedvtkDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
brain_rotatedvtkDisplay.SelectionPointLabelFontFamily = 'Arial'
brain_rotatedvtkDisplay.SelectionPointLabelFontFile = ''
brain_rotatedvtkDisplay.SelectionPointLabelFontSize = 18
brain_rotatedvtkDisplay.SelectionPointLabelItalic = 0
brain_rotatedvtkDisplay.SelectionPointLabelJustification = 'Left'
brain_rotatedvtkDisplay.SelectionPointLabelOpacity = 1.0
brain_rotatedvtkDisplay.SelectionPointLabelShadow = 0
brain_rotatedvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
brain_rotatedvtkDisplay.ScalarOpacityFunction = None
brain_rotatedvtkDisplay.ScalarOpacityUnitDistance = 0.00979290191082286
brain_rotatedvtkDisplay.SelectMapper = 'Projected tetra'
brain_rotatedvtkDisplay.SamplingDimensions = [128, 128, 128]
brain_rotatedvtkDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
brain_rotatedvtkDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
brain_rotatedvtkDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
brain_rotatedvtkDisplay.GlyphType.TipResolution = 6
brain_rotatedvtkDisplay.GlyphType.TipRadius = 0.1
brain_rotatedvtkDisplay.GlyphType.TipLength = 0.35
brain_rotatedvtkDisplay.GlyphType.ShaftResolution = 6
brain_rotatedvtkDisplay.GlyphType.ShaftRadius = 0.03
brain_rotatedvtkDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brain_rotatedvtkDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
brain_rotatedvtkDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brain_rotatedvtkDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
brain_rotatedvtkDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
brain_rotatedvtkDisplay.DataAxesGrid.XTitle = 'X Axis'
brain_rotatedvtkDisplay.DataAxesGrid.YTitle = 'Y Axis'
brain_rotatedvtkDisplay.DataAxesGrid.ZTitle = 'Z Axis'
brain_rotatedvtkDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
brain_rotatedvtkDisplay.DataAxesGrid.XTitleFontFile = ''
brain_rotatedvtkDisplay.DataAxesGrid.XTitleBold = 0
brain_rotatedvtkDisplay.DataAxesGrid.XTitleItalic = 0
brain_rotatedvtkDisplay.DataAxesGrid.XTitleFontSize = 12
brain_rotatedvtkDisplay.DataAxesGrid.XTitleShadow = 0
brain_rotatedvtkDisplay.DataAxesGrid.XTitleOpacity = 1.0
brain_rotatedvtkDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
brain_rotatedvtkDisplay.DataAxesGrid.YTitleFontFile = ''
brain_rotatedvtkDisplay.DataAxesGrid.YTitleBold = 0
brain_rotatedvtkDisplay.DataAxesGrid.YTitleItalic = 0
brain_rotatedvtkDisplay.DataAxesGrid.YTitleFontSize = 12
brain_rotatedvtkDisplay.DataAxesGrid.YTitleShadow = 0
brain_rotatedvtkDisplay.DataAxesGrid.YTitleOpacity = 1.0
brain_rotatedvtkDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
brain_rotatedvtkDisplay.DataAxesGrid.ZTitleFontFile = ''
brain_rotatedvtkDisplay.DataAxesGrid.ZTitleBold = 0
brain_rotatedvtkDisplay.DataAxesGrid.ZTitleItalic = 0
brain_rotatedvtkDisplay.DataAxesGrid.ZTitleFontSize = 12
brain_rotatedvtkDisplay.DataAxesGrid.ZTitleShadow = 0
brain_rotatedvtkDisplay.DataAxesGrid.ZTitleOpacity = 1.0
brain_rotatedvtkDisplay.DataAxesGrid.FacesToRender = 63
brain_rotatedvtkDisplay.DataAxesGrid.CullBackface = 0
brain_rotatedvtkDisplay.DataAxesGrid.CullFrontface = 1
brain_rotatedvtkDisplay.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.DataAxesGrid.ShowGrid = 0
brain_rotatedvtkDisplay.DataAxesGrid.ShowEdges = 1
brain_rotatedvtkDisplay.DataAxesGrid.ShowTicks = 1
brain_rotatedvtkDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
brain_rotatedvtkDisplay.DataAxesGrid.AxesToLabel = 63
brain_rotatedvtkDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
brain_rotatedvtkDisplay.DataAxesGrid.XLabelFontFile = ''
brain_rotatedvtkDisplay.DataAxesGrid.XLabelBold = 0
brain_rotatedvtkDisplay.DataAxesGrid.XLabelItalic = 0
brain_rotatedvtkDisplay.DataAxesGrid.XLabelFontSize = 12
brain_rotatedvtkDisplay.DataAxesGrid.XLabelShadow = 0
brain_rotatedvtkDisplay.DataAxesGrid.XLabelOpacity = 1.0
brain_rotatedvtkDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
brain_rotatedvtkDisplay.DataAxesGrid.YLabelFontFile = ''
brain_rotatedvtkDisplay.DataAxesGrid.YLabelBold = 0
brain_rotatedvtkDisplay.DataAxesGrid.YLabelItalic = 0
brain_rotatedvtkDisplay.DataAxesGrid.YLabelFontSize = 12
brain_rotatedvtkDisplay.DataAxesGrid.YLabelShadow = 0
brain_rotatedvtkDisplay.DataAxesGrid.YLabelOpacity = 1.0
brain_rotatedvtkDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
brain_rotatedvtkDisplay.DataAxesGrid.ZLabelFontFile = ''
brain_rotatedvtkDisplay.DataAxesGrid.ZLabelBold = 0
brain_rotatedvtkDisplay.DataAxesGrid.ZLabelItalic = 0
brain_rotatedvtkDisplay.DataAxesGrid.ZLabelFontSize = 12
brain_rotatedvtkDisplay.DataAxesGrid.ZLabelShadow = 0
brain_rotatedvtkDisplay.DataAxesGrid.ZLabelOpacity = 1.0
brain_rotatedvtkDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
brain_rotatedvtkDisplay.DataAxesGrid.XAxisPrecision = 2
brain_rotatedvtkDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
brain_rotatedvtkDisplay.DataAxesGrid.XAxisLabels = []
brain_rotatedvtkDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
brain_rotatedvtkDisplay.DataAxesGrid.YAxisPrecision = 2
brain_rotatedvtkDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
brain_rotatedvtkDisplay.DataAxesGrid.YAxisLabels = []
brain_rotatedvtkDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
brain_rotatedvtkDisplay.DataAxesGrid.ZAxisPrecision = 2
brain_rotatedvtkDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
brain_rotatedvtkDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
brain_rotatedvtkDisplay.PolarAxes.Visibility = 0
brain_rotatedvtkDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
brain_rotatedvtkDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
brain_rotatedvtkDisplay.PolarAxes.EnableCustomRange = 0
brain_rotatedvtkDisplay.PolarAxes.CustomRange = [0.0, 1.0]
brain_rotatedvtkDisplay.PolarAxes.PolarAxisVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.RadialAxesVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.DrawRadialGridlines = 1
brain_rotatedvtkDisplay.PolarAxes.PolarArcsVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.DrawPolarArcsGridlines = 1
brain_rotatedvtkDisplay.PolarAxes.NumberOfRadialAxes = 0
brain_rotatedvtkDisplay.PolarAxes.AutoSubdividePolarAxis = 1
brain_rotatedvtkDisplay.PolarAxes.NumberOfPolarAxis = 0
brain_rotatedvtkDisplay.PolarAxes.MinimumRadius = 0.0
brain_rotatedvtkDisplay.PolarAxes.MinimumAngle = 0.0
brain_rotatedvtkDisplay.PolarAxes.MaximumAngle = 90.0
brain_rotatedvtkDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
brain_rotatedvtkDisplay.PolarAxes.Ratio = 1.0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
brain_rotatedvtkDisplay.PolarAxes.PolarLabelVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
brain_rotatedvtkDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
brain_rotatedvtkDisplay.PolarAxes.RadialLabelVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
brain_rotatedvtkDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
brain_rotatedvtkDisplay.PolarAxes.RadialUnitsVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.ScreenSize = 10.0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleFontFile = ''
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleBold = 0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleItalic = 0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleShadow = 0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTitleFontSize = 12
brain_rotatedvtkDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
brain_rotatedvtkDisplay.PolarAxes.PolarAxisLabelFontFile = ''
brain_rotatedvtkDisplay.PolarAxes.PolarAxisLabelBold = 0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisLabelItalic = 0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisLabelShadow = 0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisLabelFontSize = 12
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTextBold = 0
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTextItalic = 0
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTextShadow = 0
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
brain_rotatedvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
brain_rotatedvtkDisplay.PolarAxes.EnableDistanceLOD = 1
brain_rotatedvtkDisplay.PolarAxes.DistanceLODThreshold = 0.7
brain_rotatedvtkDisplay.PolarAxes.EnableViewAngleLOD = 1
brain_rotatedvtkDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
brain_rotatedvtkDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
brain_rotatedvtkDisplay.PolarAxes.PolarTicksVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
brain_rotatedvtkDisplay.PolarAxes.TickLocation = 'Both'
brain_rotatedvtkDisplay.PolarAxes.AxisTickVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.AxisMinorTickVisibility = 0
brain_rotatedvtkDisplay.PolarAxes.ArcTickVisibility = 1
brain_rotatedvtkDisplay.PolarAxes.ArcMinorTickVisibility = 0
brain_rotatedvtkDisplay.PolarAxes.DeltaAngleMajor = 10.0
brain_rotatedvtkDisplay.PolarAxes.DeltaAngleMinor = 5.0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
brain_rotatedvtkDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
brain_rotatedvtkDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
brain_rotatedvtkDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
brain_rotatedvtkDisplay.PolarAxes.ArcMajorTickSize = 0.0
brain_rotatedvtkDisplay.PolarAxes.ArcTickRatioSize = 0.3
brain_rotatedvtkDisplay.PolarAxes.ArcMajorTickThickness = 1.0
brain_rotatedvtkDisplay.PolarAxes.ArcTickRatioThickness = 0.5
brain_rotatedvtkDisplay.PolarAxes.Use2DMode = 0
brain_rotatedvtkDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=brain_rotatedvtk)
extractSurface1.PieceInvariant = 1
extractSurface1.NonlinearSubdivisionLevel = 1

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.AmbientColor = [0.0, 0.0, 0.0]
extractSurface1Display.ColorArrayName = [None, '']
extractSurface1Display.DiffuseColor = [1.0, 1.0, 1.0]
extractSurface1Display.LookupTable = None
extractSurface1Display.MapScalars = 1
extractSurface1Display.MultiComponentsMapping = 0
extractSurface1Display.InterpolateScalarsBeforeMapping = 1
extractSurface1Display.Opacity = 1.0
extractSurface1Display.PointSize = 2.0
extractSurface1Display.LineWidth = 1.0
extractSurface1Display.RenderLinesAsTubes = 0
extractSurface1Display.RenderPointsAsSpheres = 0
extractSurface1Display.Interpolation = 'Gouraud'
extractSurface1Display.Specular = 0.0
extractSurface1Display.SpecularColor = [1.0, 1.0, 1.0]
extractSurface1Display.SpecularPower = 100.0
extractSurface1Display.Luminosity = 0.0
extractSurface1Display.Ambient = 0.0
extractSurface1Display.Diffuse = 1.0
extractSurface1Display.EdgeColor = [0.0, 0.0, 0.5]
extractSurface1Display.BackfaceRepresentation = 'Follow Frontface'
extractSurface1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
extractSurface1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
extractSurface1Display.BackfaceOpacity = 1.0
extractSurface1Display.Position = [0.0, 0.0, 0.0]
extractSurface1Display.Scale = [1.0, 1.0, 1.0]
extractSurface1Display.Orientation = [0.0, 0.0, 0.0]
extractSurface1Display.Origin = [0.0, 0.0, 0.0]
extractSurface1Display.Pickable = 1
extractSurface1Display.Texture = None
extractSurface1Display.Triangulate = 0
extractSurface1Display.UseShaderReplacements = 0
extractSurface1Display.ShaderReplacements = ''
extractSurface1Display.NonlinearSubdivisionLevel = 1
extractSurface1Display.UseDataPartitions = 0
extractSurface1Display.OSPRayUseScaleArray = 0
extractSurface1Display.OSPRayScaleArray = ''
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.OSPRayMaterial = 'None'
extractSurface1Display.Orient = 0
extractSurface1Display.OrientationMode = 'Direction'
extractSurface1Display.SelectOrientationVectors = 'None'
extractSurface1Display.Scaling = 0
extractSurface1Display.ScaleMode = 'No Data Scaling Off'
extractSurface1Display.ScaleFactor = 0.016502300277352333
extractSurface1Display.SelectScaleArray = 'None'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.UseGlyphTable = 0
extractSurface1Display.GlyphTableIndexArray = 'None'
extractSurface1Display.UseCompositeGlyphTable = 0
extractSurface1Display.UseGlyphCullingAndLOD = 0
extractSurface1Display.LODValues = []
extractSurface1Display.ColorByLODIndex = 0
extractSurface1Display.GaussianRadius = 0.0008251150138676167
extractSurface1Display.ShaderPreset = 'Sphere'
extractSurface1Display.CustomTriangleScale = 3
extractSurface1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
extractSurface1Display.Emissive = 0
extractSurface1Display.ScaleByArray = 0
extractSurface1Display.SetScaleArray = [None, '']
extractSurface1Display.ScaleArrayComponent = 0
extractSurface1Display.UseScaleFunction = 1
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityByArray = 0
extractSurface1Display.OpacityArray = [None, '']
extractSurface1Display.OpacityArrayComponent = 0
extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface1Display.SelectionCellLabelBold = 0
extractSurface1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
extractSurface1Display.SelectionCellLabelFontFamily = 'Arial'
extractSurface1Display.SelectionCellLabelFontFile = ''
extractSurface1Display.SelectionCellLabelFontSize = 18
extractSurface1Display.SelectionCellLabelItalic = 0
extractSurface1Display.SelectionCellLabelJustification = 'Left'
extractSurface1Display.SelectionCellLabelOpacity = 1.0
extractSurface1Display.SelectionCellLabelShadow = 0
extractSurface1Display.SelectionPointLabelBold = 0
extractSurface1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
extractSurface1Display.SelectionPointLabelFontFamily = 'Arial'
extractSurface1Display.SelectionPointLabelFontFile = ''
extractSurface1Display.SelectionPointLabelFontSize = 18
extractSurface1Display.SelectionPointLabelItalic = 0
extractSurface1Display.SelectionPointLabelJustification = 'Left'
extractSurface1Display.SelectionPointLabelOpacity = 1.0
extractSurface1Display.SelectionPointLabelShadow = 0
extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
extractSurface1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
extractSurface1Display.GlyphType.TipResolution = 6
extractSurface1Display.GlyphType.TipRadius = 0.1
extractSurface1Display.GlyphType.TipLength = 0.35
extractSurface1Display.GlyphType.ShaftResolution = 6
extractSurface1Display.GlyphType.ShaftRadius = 0.03
extractSurface1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
extractSurface1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
extractSurface1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface1Display.DataAxesGrid.XTitle = 'X Axis'
extractSurface1Display.DataAxesGrid.YTitle = 'Y Axis'
extractSurface1Display.DataAxesGrid.ZTitle = 'Z Axis'
extractSurface1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.XTitleFontFile = ''
extractSurface1Display.DataAxesGrid.XTitleBold = 0
extractSurface1Display.DataAxesGrid.XTitleItalic = 0
extractSurface1Display.DataAxesGrid.XTitleFontSize = 12
extractSurface1Display.DataAxesGrid.XTitleShadow = 0
extractSurface1Display.DataAxesGrid.XTitleOpacity = 1.0
extractSurface1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.YTitleFontFile = ''
extractSurface1Display.DataAxesGrid.YTitleBold = 0
extractSurface1Display.DataAxesGrid.YTitleItalic = 0
extractSurface1Display.DataAxesGrid.YTitleFontSize = 12
extractSurface1Display.DataAxesGrid.YTitleShadow = 0
extractSurface1Display.DataAxesGrid.YTitleOpacity = 1.0
extractSurface1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface1Display.DataAxesGrid.ZTitleBold = 0
extractSurface1Display.DataAxesGrid.ZTitleItalic = 0
extractSurface1Display.DataAxesGrid.ZTitleFontSize = 12
extractSurface1Display.DataAxesGrid.ZTitleShadow = 0
extractSurface1Display.DataAxesGrid.ZTitleOpacity = 1.0
extractSurface1Display.DataAxesGrid.FacesToRender = 63
extractSurface1Display.DataAxesGrid.CullBackface = 0
extractSurface1Display.DataAxesGrid.CullFrontface = 1
extractSurface1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.ShowGrid = 0
extractSurface1Display.DataAxesGrid.ShowEdges = 1
extractSurface1Display.DataAxesGrid.ShowTicks = 1
extractSurface1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
extractSurface1Display.DataAxesGrid.AxesToLabel = 63
extractSurface1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.XLabelFontFile = ''
extractSurface1Display.DataAxesGrid.XLabelBold = 0
extractSurface1Display.DataAxesGrid.XLabelItalic = 0
extractSurface1Display.DataAxesGrid.XLabelFontSize = 12
extractSurface1Display.DataAxesGrid.XLabelShadow = 0
extractSurface1Display.DataAxesGrid.XLabelOpacity = 1.0
extractSurface1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.YLabelFontFile = ''
extractSurface1Display.DataAxesGrid.YLabelBold = 0
extractSurface1Display.DataAxesGrid.YLabelItalic = 0
extractSurface1Display.DataAxesGrid.YLabelFontSize = 12
extractSurface1Display.DataAxesGrid.YLabelShadow = 0
extractSurface1Display.DataAxesGrid.YLabelOpacity = 1.0
extractSurface1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.ZLabelFontFile = ''
extractSurface1Display.DataAxesGrid.ZLabelBold = 0
extractSurface1Display.DataAxesGrid.ZLabelItalic = 0
extractSurface1Display.DataAxesGrid.ZLabelFontSize = 12
extractSurface1Display.DataAxesGrid.ZLabelShadow = 0
extractSurface1Display.DataAxesGrid.ZLabelOpacity = 1.0
extractSurface1Display.DataAxesGrid.XAxisNotation = 'Mixed'
extractSurface1Display.DataAxesGrid.XAxisPrecision = 2
extractSurface1Display.DataAxesGrid.XAxisUseCustomLabels = 0
extractSurface1Display.DataAxesGrid.XAxisLabels = []
extractSurface1Display.DataAxesGrid.YAxisNotation = 'Mixed'
extractSurface1Display.DataAxesGrid.YAxisPrecision = 2
extractSurface1Display.DataAxesGrid.YAxisUseCustomLabels = 0
extractSurface1Display.DataAxesGrid.YAxisLabels = []
extractSurface1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
extractSurface1Display.DataAxesGrid.ZAxisPrecision = 2
extractSurface1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
extractSurface1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface1Display.PolarAxes.Visibility = 0
extractSurface1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
extractSurface1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
extractSurface1Display.PolarAxes.EnableCustomRange = 0
extractSurface1Display.PolarAxes.CustomRange = [0.0, 1.0]
extractSurface1Display.PolarAxes.PolarAxisVisibility = 1
extractSurface1Display.PolarAxes.RadialAxesVisibility = 1
extractSurface1Display.PolarAxes.DrawRadialGridlines = 1
extractSurface1Display.PolarAxes.PolarArcsVisibility = 1
extractSurface1Display.PolarAxes.DrawPolarArcsGridlines = 1
extractSurface1Display.PolarAxes.NumberOfRadialAxes = 0
extractSurface1Display.PolarAxes.AutoSubdividePolarAxis = 1
extractSurface1Display.PolarAxes.NumberOfPolarAxis = 0
extractSurface1Display.PolarAxes.MinimumRadius = 0.0
extractSurface1Display.PolarAxes.MinimumAngle = 0.0
extractSurface1Display.PolarAxes.MaximumAngle = 90.0
extractSurface1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
extractSurface1Display.PolarAxes.Ratio = 1.0
extractSurface1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.PolarAxisTitleVisibility = 1
extractSurface1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
extractSurface1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
extractSurface1Display.PolarAxes.PolarLabelVisibility = 1
extractSurface1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
extractSurface1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
extractSurface1Display.PolarAxes.RadialLabelVisibility = 1
extractSurface1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
extractSurface1Display.PolarAxes.RadialLabelLocation = 'Bottom'
extractSurface1Display.PolarAxes.RadialUnitsVisibility = 1
extractSurface1Display.PolarAxes.ScreenSize = 10.0
extractSurface1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
extractSurface1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
extractSurface1Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface1Display.PolarAxes.PolarAxisTitleBold = 0
extractSurface1Display.PolarAxes.PolarAxisTitleItalic = 0
extractSurface1Display.PolarAxes.PolarAxisTitleShadow = 0
extractSurface1Display.PolarAxes.PolarAxisTitleFontSize = 12
extractSurface1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
extractSurface1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
extractSurface1Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface1Display.PolarAxes.PolarAxisLabelBold = 0
extractSurface1Display.PolarAxes.PolarAxisLabelItalic = 0
extractSurface1Display.PolarAxes.PolarAxisLabelShadow = 0
extractSurface1Display.PolarAxes.PolarAxisLabelFontSize = 12
extractSurface1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
extractSurface1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
extractSurface1Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface1Display.PolarAxes.LastRadialAxisTextBold = 0
extractSurface1Display.PolarAxes.LastRadialAxisTextItalic = 0
extractSurface1Display.PolarAxes.LastRadialAxisTextShadow = 0
extractSurface1Display.PolarAxes.LastRadialAxisTextFontSize = 12
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
extractSurface1Display.PolarAxes.EnableDistanceLOD = 1
extractSurface1Display.PolarAxes.DistanceLODThreshold = 0.7
extractSurface1Display.PolarAxes.EnableViewAngleLOD = 1
extractSurface1Display.PolarAxes.ViewAngleLODThreshold = 0.7
extractSurface1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
extractSurface1Display.PolarAxes.PolarTicksVisibility = 1
extractSurface1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
extractSurface1Display.PolarAxes.TickLocation = 'Both'
extractSurface1Display.PolarAxes.AxisTickVisibility = 1
extractSurface1Display.PolarAxes.AxisMinorTickVisibility = 0
extractSurface1Display.PolarAxes.ArcTickVisibility = 1
extractSurface1Display.PolarAxes.ArcMinorTickVisibility = 0
extractSurface1Display.PolarAxes.DeltaAngleMajor = 10.0
extractSurface1Display.PolarAxes.DeltaAngleMinor = 5.0
extractSurface1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
extractSurface1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
extractSurface1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
extractSurface1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
extractSurface1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
extractSurface1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
extractSurface1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
extractSurface1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
extractSurface1Display.PolarAxes.ArcMajorTickSize = 0.0
extractSurface1Display.PolarAxes.ArcTickRatioSize = 0.3
extractSurface1Display.PolarAxes.ArcMajorTickThickness = 1.0
extractSurface1Display.PolarAxes.ArcTickRatioThickness = 0.5
extractSurface1Display.PolarAxes.Use2DMode = 0
extractSurface1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(brain_rotatedvtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData(outputskull_file, proxy=extractSurface1, FileType='Binary',
    EnableColoring=0,
    EnableAlpha=0,
    ColorArrayName=['POINTS', ''],
    LookupTable=None,
    WriteTimeSteps=0,
    Filenamesuffix='_%d')

# hide data in view
Hide(extractSurface1, renderView1)

# set active source
SetActiveSource(brain_rotatedvtk)

# show data in view
brain_rotatedvtkDisplay = Show(brain_rotatedvtk, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Threshold'
threshold1 = Threshold(Input=brain_rotatedvtk)
threshold1.Scalars = ['CELLS', 'Part ID']
threshold1.ThresholdRange = [0.0, 9.0]
threshold1.AllScalars = 1
threshold1.UseContinuousCellRange = 0

# Properties modified on threshold1
threshold1.ThresholdRange = [2.0, 9.0]

# show data in view
threshold1Display = Show(threshold1, renderView1)

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.AmbientColor = [0.0, 0.0, 0.0]
threshold1Display.ColorArrayName = [None, '']
threshold1Display.DiffuseColor = [1.0, 1.0, 1.0]
threshold1Display.LookupTable = None
threshold1Display.MapScalars = 1
threshold1Display.MultiComponentsMapping = 0
threshold1Display.InterpolateScalarsBeforeMapping = 1
threshold1Display.Opacity = 1.0
threshold1Display.PointSize = 2.0
threshold1Display.LineWidth = 1.0
threshold1Display.RenderLinesAsTubes = 0
threshold1Display.RenderPointsAsSpheres = 0
threshold1Display.Interpolation = 'Gouraud'
threshold1Display.Specular = 0.0
threshold1Display.SpecularColor = [1.0, 1.0, 1.0]
threshold1Display.SpecularPower = 100.0
threshold1Display.Luminosity = 0.0
threshold1Display.Ambient = 0.0
threshold1Display.Diffuse = 1.0
threshold1Display.EdgeColor = [0.0, 0.0, 0.5]
threshold1Display.BackfaceRepresentation = 'Follow Frontface'
threshold1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
threshold1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
threshold1Display.BackfaceOpacity = 1.0
threshold1Display.Position = [0.0, 0.0, 0.0]
threshold1Display.Scale = [1.0, 1.0, 1.0]
threshold1Display.Orientation = [0.0, 0.0, 0.0]
threshold1Display.Origin = [0.0, 0.0, 0.0]
threshold1Display.Pickable = 1
threshold1Display.Texture = None
threshold1Display.Triangulate = 0
threshold1Display.UseShaderReplacements = 0
threshold1Display.ShaderReplacements = ''
threshold1Display.NonlinearSubdivisionLevel = 1
threshold1Display.UseDataPartitions = 0
threshold1Display.OSPRayUseScaleArray = 0
threshold1Display.OSPRayScaleArray = ''
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.OSPRayMaterial = 'None'
threshold1Display.Orient = 0
threshold1Display.OrientationMode = 'Direction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.Scaling = 0
threshold1Display.ScaleMode = 'No Data Scaling Off'
threshold1Display.ScaleFactor = 0.015447470173239709
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.UseGlyphTable = 0
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.UseCompositeGlyphTable = 0
threshold1Display.UseGlyphCullingAndLOD = 0
threshold1Display.LODValues = []
threshold1Display.ColorByLODIndex = 0
threshold1Display.GaussianRadius = 0.0007723735086619854
threshold1Display.ShaderPreset = 'Sphere'
threshold1Display.CustomTriangleScale = 3
threshold1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
threshold1Display.Emissive = 0
threshold1Display.ScaleByArray = 0
threshold1Display.SetScaleArray = [None, '']
threshold1Display.ScaleArrayComponent = 0
threshold1Display.UseScaleFunction = 1
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityByArray = 0
threshold1Display.OpacityArray = [None, '']
threshold1Display.OpacityArrayComponent = 0
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.SelectionCellLabelBold = 0
threshold1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
threshold1Display.SelectionCellLabelFontFamily = 'Arial'
threshold1Display.SelectionCellLabelFontFile = ''
threshold1Display.SelectionCellLabelFontSize = 18
threshold1Display.SelectionCellLabelItalic = 0
threshold1Display.SelectionCellLabelJustification = 'Left'
threshold1Display.SelectionCellLabelOpacity = 1.0
threshold1Display.SelectionCellLabelShadow = 0
threshold1Display.SelectionPointLabelBold = 0
threshold1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
threshold1Display.SelectionPointLabelFontFamily = 'Arial'
threshold1Display.SelectionPointLabelFontFile = ''
threshold1Display.SelectionPointLabelFontSize = 18
threshold1Display.SelectionPointLabelItalic = 0
threshold1Display.SelectionPointLabelJustification = 'Left'
threshold1Display.SelectionPointLabelOpacity = 1.0
threshold1Display.SelectionPointLabelShadow = 0
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = None
threshold1Display.ScalarOpacityUnitDistance = 0.010700302715290278
threshold1Display.SelectMapper = 'Projected tetra'
threshold1Display.SamplingDimensions = [128, 128, 128]
threshold1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
threshold1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
threshold1Display.GlyphType.TipResolution = 6
threshold1Display.GlyphType.TipRadius = 0.1
threshold1Display.GlyphType.TipLength = 0.35
threshold1Display.GlyphType.ShaftResolution = 6
threshold1Display.GlyphType.ShaftRadius = 0.03
threshold1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
threshold1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
threshold1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold1Display.DataAxesGrid.XTitle = 'X Axis'
threshold1Display.DataAxesGrid.YTitle = 'Y Axis'
threshold1Display.DataAxesGrid.ZTitle = 'Z Axis'
threshold1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
threshold1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
threshold1Display.DataAxesGrid.XTitleFontFile = ''
threshold1Display.DataAxesGrid.XTitleBold = 0
threshold1Display.DataAxesGrid.XTitleItalic = 0
threshold1Display.DataAxesGrid.XTitleFontSize = 12
threshold1Display.DataAxesGrid.XTitleShadow = 0
threshold1Display.DataAxesGrid.XTitleOpacity = 1.0
threshold1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
threshold1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
threshold1Display.DataAxesGrid.YTitleFontFile = ''
threshold1Display.DataAxesGrid.YTitleBold = 0
threshold1Display.DataAxesGrid.YTitleItalic = 0
threshold1Display.DataAxesGrid.YTitleFontSize = 12
threshold1Display.DataAxesGrid.YTitleShadow = 0
threshold1Display.DataAxesGrid.YTitleOpacity = 1.0
threshold1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
threshold1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
threshold1Display.DataAxesGrid.ZTitleFontFile = ''
threshold1Display.DataAxesGrid.ZTitleBold = 0
threshold1Display.DataAxesGrid.ZTitleItalic = 0
threshold1Display.DataAxesGrid.ZTitleFontSize = 12
threshold1Display.DataAxesGrid.ZTitleShadow = 0
threshold1Display.DataAxesGrid.ZTitleOpacity = 1.0
threshold1Display.DataAxesGrid.FacesToRender = 63
threshold1Display.DataAxesGrid.CullBackface = 0
threshold1Display.DataAxesGrid.CullFrontface = 1
threshold1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
threshold1Display.DataAxesGrid.ShowGrid = 0
threshold1Display.DataAxesGrid.ShowEdges = 1
threshold1Display.DataAxesGrid.ShowTicks = 1
threshold1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
threshold1Display.DataAxesGrid.AxesToLabel = 63
threshold1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
threshold1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
threshold1Display.DataAxesGrid.XLabelFontFile = ''
threshold1Display.DataAxesGrid.XLabelBold = 0
threshold1Display.DataAxesGrid.XLabelItalic = 0
threshold1Display.DataAxesGrid.XLabelFontSize = 12
threshold1Display.DataAxesGrid.XLabelShadow = 0
threshold1Display.DataAxesGrid.XLabelOpacity = 1.0
threshold1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
threshold1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
threshold1Display.DataAxesGrid.YLabelFontFile = ''
threshold1Display.DataAxesGrid.YLabelBold = 0
threshold1Display.DataAxesGrid.YLabelItalic = 0
threshold1Display.DataAxesGrid.YLabelFontSize = 12
threshold1Display.DataAxesGrid.YLabelShadow = 0
threshold1Display.DataAxesGrid.YLabelOpacity = 1.0
threshold1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
threshold1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
threshold1Display.DataAxesGrid.ZLabelFontFile = ''
threshold1Display.DataAxesGrid.ZLabelBold = 0
threshold1Display.DataAxesGrid.ZLabelItalic = 0
threshold1Display.DataAxesGrid.ZLabelFontSize = 12
threshold1Display.DataAxesGrid.ZLabelShadow = 0
threshold1Display.DataAxesGrid.ZLabelOpacity = 1.0
threshold1Display.DataAxesGrid.XAxisNotation = 'Mixed'
threshold1Display.DataAxesGrid.XAxisPrecision = 2
threshold1Display.DataAxesGrid.XAxisUseCustomLabels = 0
threshold1Display.DataAxesGrid.XAxisLabels = []
threshold1Display.DataAxesGrid.YAxisNotation = 'Mixed'
threshold1Display.DataAxesGrid.YAxisPrecision = 2
threshold1Display.DataAxesGrid.YAxisUseCustomLabels = 0
threshold1Display.DataAxesGrid.YAxisLabels = []
threshold1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
threshold1Display.DataAxesGrid.ZAxisPrecision = 2
threshold1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
threshold1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold1Display.PolarAxes.Visibility = 0
threshold1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
threshold1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
threshold1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
threshold1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
threshold1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
threshold1Display.PolarAxes.EnableCustomRange = 0
threshold1Display.PolarAxes.CustomRange = [0.0, 1.0]
threshold1Display.PolarAxes.PolarAxisVisibility = 1
threshold1Display.PolarAxes.RadialAxesVisibility = 1
threshold1Display.PolarAxes.DrawRadialGridlines = 1
threshold1Display.PolarAxes.PolarArcsVisibility = 1
threshold1Display.PolarAxes.DrawPolarArcsGridlines = 1
threshold1Display.PolarAxes.NumberOfRadialAxes = 0
threshold1Display.PolarAxes.AutoSubdividePolarAxis = 1
threshold1Display.PolarAxes.NumberOfPolarAxis = 0
threshold1Display.PolarAxes.MinimumRadius = 0.0
threshold1Display.PolarAxes.MinimumAngle = 0.0
threshold1Display.PolarAxes.MaximumAngle = 90.0
threshold1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
threshold1Display.PolarAxes.Ratio = 1.0
threshold1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
threshold1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
threshold1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
threshold1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
threshold1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
threshold1Display.PolarAxes.PolarAxisTitleVisibility = 1
threshold1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
threshold1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
threshold1Display.PolarAxes.PolarLabelVisibility = 1
threshold1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
threshold1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
threshold1Display.PolarAxes.RadialLabelVisibility = 1
threshold1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
threshold1Display.PolarAxes.RadialLabelLocation = 'Bottom'
threshold1Display.PolarAxes.RadialUnitsVisibility = 1
threshold1Display.PolarAxes.ScreenSize = 10.0
threshold1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
threshold1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
threshold1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
threshold1Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold1Display.PolarAxes.PolarAxisTitleBold = 0
threshold1Display.PolarAxes.PolarAxisTitleItalic = 0
threshold1Display.PolarAxes.PolarAxisTitleShadow = 0
threshold1Display.PolarAxes.PolarAxisTitleFontSize = 12
threshold1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
threshold1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
threshold1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
threshold1Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold1Display.PolarAxes.PolarAxisLabelBold = 0
threshold1Display.PolarAxes.PolarAxisLabelItalic = 0
threshold1Display.PolarAxes.PolarAxisLabelShadow = 0
threshold1Display.PolarAxes.PolarAxisLabelFontSize = 12
threshold1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
threshold1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
threshold1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
threshold1Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold1Display.PolarAxes.LastRadialAxisTextBold = 0
threshold1Display.PolarAxes.LastRadialAxisTextItalic = 0
threshold1Display.PolarAxes.LastRadialAxisTextShadow = 0
threshold1Display.PolarAxes.LastRadialAxisTextFontSize = 12
threshold1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
threshold1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
threshold1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
threshold1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
threshold1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
threshold1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
threshold1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
threshold1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
threshold1Display.PolarAxes.EnableDistanceLOD = 1
threshold1Display.PolarAxes.DistanceLODThreshold = 0.7
threshold1Display.PolarAxes.EnableViewAngleLOD = 1
threshold1Display.PolarAxes.ViewAngleLODThreshold = 0.7
threshold1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
threshold1Display.PolarAxes.PolarTicksVisibility = 1
threshold1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
threshold1Display.PolarAxes.TickLocation = 'Both'
threshold1Display.PolarAxes.AxisTickVisibility = 1
threshold1Display.PolarAxes.AxisMinorTickVisibility = 0
threshold1Display.PolarAxes.ArcTickVisibility = 1
threshold1Display.PolarAxes.ArcMinorTickVisibility = 0
threshold1Display.PolarAxes.DeltaAngleMajor = 10.0
threshold1Display.PolarAxes.DeltaAngleMinor = 5.0
threshold1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
threshold1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
threshold1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
threshold1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
threshold1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
threshold1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
threshold1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
threshold1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
threshold1Display.PolarAxes.ArcMajorTickSize = 0.0
threshold1Display.PolarAxes.ArcTickRatioSize = 0.3
threshold1Display.PolarAxes.ArcMajorTickThickness = 1.0
threshold1Display.PolarAxes.ArcTickRatioThickness = 0.5
threshold1Display.PolarAxes.Use2DMode = 0
threshold1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(brain_rotatedvtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold1)
extractSurface2.PieceInvariant = 1
extractSurface2.NonlinearSubdivisionLevel = 1

# show data in view
extractSurface2Display = Show(extractSurface2, renderView1)

# trace defaults for the display properties.
extractSurface2Display.Representation = 'Surface'
extractSurface2Display.AmbientColor = [0.0, 0.0, 0.0]
extractSurface2Display.ColorArrayName = [None, '']
extractSurface2Display.DiffuseColor = [1.0, 1.0, 1.0]
extractSurface2Display.LookupTable = None
extractSurface2Display.MapScalars = 1
extractSurface2Display.MultiComponentsMapping = 0
extractSurface2Display.InterpolateScalarsBeforeMapping = 1
extractSurface2Display.Opacity = 1.0
extractSurface2Display.PointSize = 2.0
extractSurface2Display.LineWidth = 1.0
extractSurface2Display.RenderLinesAsTubes = 0
extractSurface2Display.RenderPointsAsSpheres = 0
extractSurface2Display.Interpolation = 'Gouraud'
extractSurface2Display.Specular = 0.0
extractSurface2Display.SpecularColor = [1.0, 1.0, 1.0]
extractSurface2Display.SpecularPower = 100.0
extractSurface2Display.Luminosity = 0.0
extractSurface2Display.Ambient = 0.0
extractSurface2Display.Diffuse = 1.0
extractSurface2Display.EdgeColor = [0.0, 0.0, 0.5]
extractSurface2Display.BackfaceRepresentation = 'Follow Frontface'
extractSurface2Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
extractSurface2Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
extractSurface2Display.BackfaceOpacity = 1.0
extractSurface2Display.Position = [0.0, 0.0, 0.0]
extractSurface2Display.Scale = [1.0, 1.0, 1.0]
extractSurface2Display.Orientation = [0.0, 0.0, 0.0]
extractSurface2Display.Origin = [0.0, 0.0, 0.0]
extractSurface2Display.Pickable = 1
extractSurface2Display.Texture = None
extractSurface2Display.Triangulate = 0
extractSurface2Display.UseShaderReplacements = 0
extractSurface2Display.ShaderReplacements = ''
extractSurface2Display.NonlinearSubdivisionLevel = 1
extractSurface2Display.UseDataPartitions = 0
extractSurface2Display.OSPRayUseScaleArray = 0
extractSurface2Display.OSPRayScaleArray = ''
extractSurface2Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface2Display.OSPRayMaterial = 'None'
extractSurface2Display.Orient = 0
extractSurface2Display.OrientationMode = 'Direction'
extractSurface2Display.SelectOrientationVectors = 'None'
extractSurface2Display.Scaling = 0
extractSurface2Display.ScaleMode = 'No Data Scaling Off'
extractSurface2Display.ScaleFactor = 0.015447470173239709
extractSurface2Display.SelectScaleArray = 'None'
extractSurface2Display.GlyphType = 'Arrow'
extractSurface2Display.UseGlyphTable = 0
extractSurface2Display.GlyphTableIndexArray = 'None'
extractSurface2Display.UseCompositeGlyphTable = 0
extractSurface2Display.UseGlyphCullingAndLOD = 0
extractSurface2Display.LODValues = []
extractSurface2Display.ColorByLODIndex = 0
extractSurface2Display.GaussianRadius = 0.0007723735086619854
extractSurface2Display.ShaderPreset = 'Sphere'
extractSurface2Display.CustomTriangleScale = 3
extractSurface2Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
extractSurface2Display.Emissive = 0
extractSurface2Display.ScaleByArray = 0
extractSurface2Display.SetScaleArray = [None, '']
extractSurface2Display.ScaleArrayComponent = 0
extractSurface2Display.UseScaleFunction = 1
extractSurface2Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface2Display.OpacityByArray = 0
extractSurface2Display.OpacityArray = [None, '']
extractSurface2Display.OpacityArrayComponent = 0
extractSurface2Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface2Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface2Display.SelectionCellLabelBold = 0
extractSurface2Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
extractSurface2Display.SelectionCellLabelFontFamily = 'Arial'
extractSurface2Display.SelectionCellLabelFontFile = ''
extractSurface2Display.SelectionCellLabelFontSize = 18
extractSurface2Display.SelectionCellLabelItalic = 0
extractSurface2Display.SelectionCellLabelJustification = 'Left'
extractSurface2Display.SelectionCellLabelOpacity = 1.0
extractSurface2Display.SelectionCellLabelShadow = 0
extractSurface2Display.SelectionPointLabelBold = 0
extractSurface2Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
extractSurface2Display.SelectionPointLabelFontFamily = 'Arial'
extractSurface2Display.SelectionPointLabelFontFile = ''
extractSurface2Display.SelectionPointLabelFontSize = 18
extractSurface2Display.SelectionPointLabelItalic = 0
extractSurface2Display.SelectionPointLabelJustification = 'Left'
extractSurface2Display.SelectionPointLabelOpacity = 1.0
extractSurface2Display.SelectionPointLabelShadow = 0
extractSurface2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface2Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
extractSurface2Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
extractSurface2Display.GlyphType.TipResolution = 6
extractSurface2Display.GlyphType.TipRadius = 0.1
extractSurface2Display.GlyphType.TipLength = 0.35
extractSurface2Display.GlyphType.ShaftResolution = 6
extractSurface2Display.GlyphType.ShaftRadius = 0.03
extractSurface2Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
extractSurface2Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
extractSurface2Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface2Display.DataAxesGrid.XTitle = 'X Axis'
extractSurface2Display.DataAxesGrid.YTitle = 'Y Axis'
extractSurface2Display.DataAxesGrid.ZTitle = 'Z Axis'
extractSurface2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
extractSurface2Display.DataAxesGrid.XTitleFontFamily = 'Arial'
extractSurface2Display.DataAxesGrid.XTitleFontFile = ''
extractSurface2Display.DataAxesGrid.XTitleBold = 0
extractSurface2Display.DataAxesGrid.XTitleItalic = 0
extractSurface2Display.DataAxesGrid.XTitleFontSize = 12
extractSurface2Display.DataAxesGrid.XTitleShadow = 0
extractSurface2Display.DataAxesGrid.XTitleOpacity = 1.0
extractSurface2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
extractSurface2Display.DataAxesGrid.YTitleFontFamily = 'Arial'
extractSurface2Display.DataAxesGrid.YTitleFontFile = ''
extractSurface2Display.DataAxesGrid.YTitleBold = 0
extractSurface2Display.DataAxesGrid.YTitleItalic = 0
extractSurface2Display.DataAxesGrid.YTitleFontSize = 12
extractSurface2Display.DataAxesGrid.YTitleShadow = 0
extractSurface2Display.DataAxesGrid.YTitleOpacity = 1.0
extractSurface2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
extractSurface2Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
extractSurface2Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface2Display.DataAxesGrid.ZTitleBold = 0
extractSurface2Display.DataAxesGrid.ZTitleItalic = 0
extractSurface2Display.DataAxesGrid.ZTitleFontSize = 12
extractSurface2Display.DataAxesGrid.ZTitleShadow = 0
extractSurface2Display.DataAxesGrid.ZTitleOpacity = 1.0
extractSurface2Display.DataAxesGrid.FacesToRender = 63
extractSurface2Display.DataAxesGrid.CullBackface = 0
extractSurface2Display.DataAxesGrid.CullFrontface = 1
extractSurface2Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
extractSurface2Display.DataAxesGrid.ShowGrid = 0
extractSurface2Display.DataAxesGrid.ShowEdges = 1
extractSurface2Display.DataAxesGrid.ShowTicks = 1
extractSurface2Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
extractSurface2Display.DataAxesGrid.AxesToLabel = 63
extractSurface2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
extractSurface2Display.DataAxesGrid.XLabelFontFamily = 'Arial'
extractSurface2Display.DataAxesGrid.XLabelFontFile = ''
extractSurface2Display.DataAxesGrid.XLabelBold = 0
extractSurface2Display.DataAxesGrid.XLabelItalic = 0
extractSurface2Display.DataAxesGrid.XLabelFontSize = 12
extractSurface2Display.DataAxesGrid.XLabelShadow = 0
extractSurface2Display.DataAxesGrid.XLabelOpacity = 1.0
extractSurface2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
extractSurface2Display.DataAxesGrid.YLabelFontFamily = 'Arial'
extractSurface2Display.DataAxesGrid.YLabelFontFile = ''
extractSurface2Display.DataAxesGrid.YLabelBold = 0
extractSurface2Display.DataAxesGrid.YLabelItalic = 0
extractSurface2Display.DataAxesGrid.YLabelFontSize = 12
extractSurface2Display.DataAxesGrid.YLabelShadow = 0
extractSurface2Display.DataAxesGrid.YLabelOpacity = 1.0
extractSurface2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
extractSurface2Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
extractSurface2Display.DataAxesGrid.ZLabelFontFile = ''
extractSurface2Display.DataAxesGrid.ZLabelBold = 0
extractSurface2Display.DataAxesGrid.ZLabelItalic = 0
extractSurface2Display.DataAxesGrid.ZLabelFontSize = 12
extractSurface2Display.DataAxesGrid.ZLabelShadow = 0
extractSurface2Display.DataAxesGrid.ZLabelOpacity = 1.0
extractSurface2Display.DataAxesGrid.XAxisNotation = 'Mixed'
extractSurface2Display.DataAxesGrid.XAxisPrecision = 2
extractSurface2Display.DataAxesGrid.XAxisUseCustomLabels = 0
extractSurface2Display.DataAxesGrid.XAxisLabels = []
extractSurface2Display.DataAxesGrid.YAxisNotation = 'Mixed'
extractSurface2Display.DataAxesGrid.YAxisPrecision = 2
extractSurface2Display.DataAxesGrid.YAxisUseCustomLabels = 0
extractSurface2Display.DataAxesGrid.YAxisLabels = []
extractSurface2Display.DataAxesGrid.ZAxisNotation = 'Mixed'
extractSurface2Display.DataAxesGrid.ZAxisPrecision = 2
extractSurface2Display.DataAxesGrid.ZAxisUseCustomLabels = 0
extractSurface2Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface2Display.PolarAxes.Visibility = 0
extractSurface2Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
extractSurface2Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
extractSurface2Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
extractSurface2Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
extractSurface2Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
extractSurface2Display.PolarAxes.EnableCustomRange = 0
extractSurface2Display.PolarAxes.CustomRange = [0.0, 1.0]
extractSurface2Display.PolarAxes.PolarAxisVisibility = 1
extractSurface2Display.PolarAxes.RadialAxesVisibility = 1
extractSurface2Display.PolarAxes.DrawRadialGridlines = 1
extractSurface2Display.PolarAxes.PolarArcsVisibility = 1
extractSurface2Display.PolarAxes.DrawPolarArcsGridlines = 1
extractSurface2Display.PolarAxes.NumberOfRadialAxes = 0
extractSurface2Display.PolarAxes.AutoSubdividePolarAxis = 1
extractSurface2Display.PolarAxes.NumberOfPolarAxis = 0
extractSurface2Display.PolarAxes.MinimumRadius = 0.0
extractSurface2Display.PolarAxes.MinimumAngle = 0.0
extractSurface2Display.PolarAxes.MaximumAngle = 90.0
extractSurface2Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
extractSurface2Display.PolarAxes.Ratio = 1.0
extractSurface2Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
extractSurface2Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
extractSurface2Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
extractSurface2Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
extractSurface2Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
extractSurface2Display.PolarAxes.PolarAxisTitleVisibility = 1
extractSurface2Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
extractSurface2Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
extractSurface2Display.PolarAxes.PolarLabelVisibility = 1
extractSurface2Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
extractSurface2Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
extractSurface2Display.PolarAxes.RadialLabelVisibility = 1
extractSurface2Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
extractSurface2Display.PolarAxes.RadialLabelLocation = 'Bottom'
extractSurface2Display.PolarAxes.RadialUnitsVisibility = 1
extractSurface2Display.PolarAxes.ScreenSize = 10.0
extractSurface2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
extractSurface2Display.PolarAxes.PolarAxisTitleOpacity = 1.0
extractSurface2Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
extractSurface2Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface2Display.PolarAxes.PolarAxisTitleBold = 0
extractSurface2Display.PolarAxes.PolarAxisTitleItalic = 0
extractSurface2Display.PolarAxes.PolarAxisTitleShadow = 0
extractSurface2Display.PolarAxes.PolarAxisTitleFontSize = 12
extractSurface2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
extractSurface2Display.PolarAxes.PolarAxisLabelOpacity = 1.0
extractSurface2Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
extractSurface2Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface2Display.PolarAxes.PolarAxisLabelBold = 0
extractSurface2Display.PolarAxes.PolarAxisLabelItalic = 0
extractSurface2Display.PolarAxes.PolarAxisLabelShadow = 0
extractSurface2Display.PolarAxes.PolarAxisLabelFontSize = 12
extractSurface2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
extractSurface2Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
extractSurface2Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
extractSurface2Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface2Display.PolarAxes.LastRadialAxisTextBold = 0
extractSurface2Display.PolarAxes.LastRadialAxisTextItalic = 0
extractSurface2Display.PolarAxes.LastRadialAxisTextShadow = 0
extractSurface2Display.PolarAxes.LastRadialAxisTextFontSize = 12
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextBold = 0
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
extractSurface2Display.PolarAxes.EnableDistanceLOD = 1
extractSurface2Display.PolarAxes.DistanceLODThreshold = 0.7
extractSurface2Display.PolarAxes.EnableViewAngleLOD = 1
extractSurface2Display.PolarAxes.ViewAngleLODThreshold = 0.7
extractSurface2Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
extractSurface2Display.PolarAxes.PolarTicksVisibility = 1
extractSurface2Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
extractSurface2Display.PolarAxes.TickLocation = 'Both'
extractSurface2Display.PolarAxes.AxisTickVisibility = 1
extractSurface2Display.PolarAxes.AxisMinorTickVisibility = 0
extractSurface2Display.PolarAxes.ArcTickVisibility = 1
extractSurface2Display.PolarAxes.ArcMinorTickVisibility = 0
extractSurface2Display.PolarAxes.DeltaAngleMajor = 10.0
extractSurface2Display.PolarAxes.DeltaAngleMinor = 5.0
extractSurface2Display.PolarAxes.PolarAxisMajorTickSize = 0.0
extractSurface2Display.PolarAxes.PolarAxisTickRatioSize = 0.3
extractSurface2Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
extractSurface2Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
extractSurface2Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
extractSurface2Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
extractSurface2Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
extractSurface2Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
extractSurface2Display.PolarAxes.ArcMajorTickSize = 0.0
extractSurface2Display.PolarAxes.ArcTickRatioSize = 0.3
extractSurface2Display.PolarAxes.ArcMajorTickThickness = 1.0
extractSurface2Display.PolarAxes.ArcTickRatioThickness = 0.5
extractSurface2Display.PolarAxes.Use2DMode = 0
extractSurface2Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(threshold1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData(outputbrain_file, proxy=extractSurface2, FileType='Binary',
    EnableColoring=0,
    EnableAlpha=0,
    ColorArrayName=['POINTS', ''],
    LookupTable=None,
    WriteTimeSteps=0,
    Filenamesuffix='_%d')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.31133940008392746, -0.20413725126707546, 0.2666841247968784]
renderView1.CameraFocalPoint = [-1.975148916244507e-05, 0.03594300150871277, -0.02023950032889843]
renderView1.CameraViewUp = [-0.7228767828588725, -0.1254151971104986, 0.6794999522717728]
renderView1.CameraParallelScale = 0.12597555822081147

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
