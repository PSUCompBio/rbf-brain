# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PLY Reader'
modelply = PLYReader(FileNames=['model.ply'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1443, 776]

# show data in view
modelplyDisplay = Show(modelply, renderView1)

# trace defaults for the display properties.
modelplyDisplay.Representation = 'Surface'
modelplyDisplay.AmbientColor = [1.0, 1.0, 1.0]
modelplyDisplay.ColorArrayName = [None, '']
modelplyDisplay.DiffuseColor = [1.0, 1.0, 1.0]
modelplyDisplay.LookupTable = None
modelplyDisplay.MapScalars = 1
modelplyDisplay.MultiComponentsMapping = 0
modelplyDisplay.InterpolateScalarsBeforeMapping = 1
modelplyDisplay.Opacity = 1.0
modelplyDisplay.PointSize = 2.0
modelplyDisplay.LineWidth = 1.0
modelplyDisplay.RenderLinesAsTubes = 0
modelplyDisplay.RenderPointsAsSpheres = 0
modelplyDisplay.Interpolation = 'Gouraud'
modelplyDisplay.Specular = 0.0
modelplyDisplay.SpecularColor = [1.0, 1.0, 1.0]
modelplyDisplay.SpecularPower = 100.0
modelplyDisplay.Luminosity = 0.0
modelplyDisplay.Ambient = 0.0
modelplyDisplay.Diffuse = 1.0
modelplyDisplay.EdgeColor = [0.0, 0.0, 0.5]
modelplyDisplay.BackfaceRepresentation = 'Follow Frontface'
modelplyDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
modelplyDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
modelplyDisplay.BackfaceOpacity = 1.0
modelplyDisplay.Position = [0.0, 0.0, 0.0]
modelplyDisplay.Scale = [1.0, 1.0, 1.0]
modelplyDisplay.Orientation = [0.0, 0.0, 0.0]
modelplyDisplay.Origin = [0.0, 0.0, 0.0]
modelplyDisplay.Pickable = 1
modelplyDisplay.Texture = None
modelplyDisplay.Triangulate = 0
modelplyDisplay.UseShaderReplacements = 0
modelplyDisplay.ShaderReplacements = ''
modelplyDisplay.NonlinearSubdivisionLevel = 1
modelplyDisplay.UseDataPartitions = 0
modelplyDisplay.OSPRayUseScaleArray = 0
modelplyDisplay.OSPRayScaleArray = 'TCoords'
modelplyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
modelplyDisplay.OSPRayMaterial = 'None'
modelplyDisplay.Orient = 0
modelplyDisplay.OrientationMode = 'Direction'
modelplyDisplay.SelectOrientationVectors = 'None'
modelplyDisplay.Scaling = 0
modelplyDisplay.ScaleMode = 'No Data Scaling Off'
modelplyDisplay.ScaleFactor = 0.025753611326217653
modelplyDisplay.SelectScaleArray = 'None'
modelplyDisplay.GlyphType = 'Arrow'
modelplyDisplay.UseGlyphTable = 0
modelplyDisplay.GlyphTableIndexArray = 'None'
modelplyDisplay.UseCompositeGlyphTable = 0
modelplyDisplay.UseGlyphCullingAndLOD = 0
modelplyDisplay.LODValues = []
modelplyDisplay.ColorByLODIndex = 0
modelplyDisplay.GaussianRadius = 0.0012876805663108826
modelplyDisplay.ShaderPreset = 'Sphere'
modelplyDisplay.CustomTriangleScale = 3
modelplyDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
modelplyDisplay.Emissive = 0
modelplyDisplay.ScaleByArray = 0
modelplyDisplay.SetScaleArray = ['POINTS', 'TCoords']
modelplyDisplay.ScaleArrayComponent = 'X'
modelplyDisplay.UseScaleFunction = 1
modelplyDisplay.ScaleTransferFunction = 'PiecewiseFunction'
modelplyDisplay.OpacityByArray = 0
modelplyDisplay.OpacityArray = ['POINTS', 'TCoords']
modelplyDisplay.OpacityArrayComponent = 'X'
modelplyDisplay.OpacityTransferFunction = 'PiecewiseFunction'
modelplyDisplay.DataAxesGrid = 'GridAxesRepresentation'
modelplyDisplay.SelectionCellLabelBold = 0
modelplyDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
modelplyDisplay.SelectionCellLabelFontFamily = 'Arial'
modelplyDisplay.SelectionCellLabelFontFile = ''
modelplyDisplay.SelectionCellLabelFontSize = 18
modelplyDisplay.SelectionCellLabelItalic = 0
modelplyDisplay.SelectionCellLabelJustification = 'Left'
modelplyDisplay.SelectionCellLabelOpacity = 1.0
modelplyDisplay.SelectionCellLabelShadow = 0
modelplyDisplay.SelectionPointLabelBold = 0
modelplyDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
modelplyDisplay.SelectionPointLabelFontFamily = 'Arial'
modelplyDisplay.SelectionPointLabelFontFile = ''
modelplyDisplay.SelectionPointLabelFontSize = 18
modelplyDisplay.SelectionPointLabelItalic = 0
modelplyDisplay.SelectionPointLabelJustification = 'Left'
modelplyDisplay.SelectionPointLabelOpacity = 1.0
modelplyDisplay.SelectionPointLabelShadow = 0
modelplyDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
modelplyDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
modelplyDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
modelplyDisplay.GlyphType.TipResolution = 6
modelplyDisplay.GlyphType.TipRadius = 0.1
modelplyDisplay.GlyphType.TipLength = 0.35
modelplyDisplay.GlyphType.ShaftResolution = 6
modelplyDisplay.GlyphType.ShaftRadius = 0.03
modelplyDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
modelplyDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
modelplyDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
modelplyDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
modelplyDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
modelplyDisplay.DataAxesGrid.XTitle = 'X Axis'
modelplyDisplay.DataAxesGrid.YTitle = 'Y Axis'
modelplyDisplay.DataAxesGrid.ZTitle = 'Z Axis'
modelplyDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
modelplyDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
modelplyDisplay.DataAxesGrid.XTitleFontFile = ''
modelplyDisplay.DataAxesGrid.XTitleBold = 0
modelplyDisplay.DataAxesGrid.XTitleItalic = 0
modelplyDisplay.DataAxesGrid.XTitleFontSize = 12
modelplyDisplay.DataAxesGrid.XTitleShadow = 0
modelplyDisplay.DataAxesGrid.XTitleOpacity = 1.0
modelplyDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
modelplyDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
modelplyDisplay.DataAxesGrid.YTitleFontFile = ''
modelplyDisplay.DataAxesGrid.YTitleBold = 0
modelplyDisplay.DataAxesGrid.YTitleItalic = 0
modelplyDisplay.DataAxesGrid.YTitleFontSize = 12
modelplyDisplay.DataAxesGrid.YTitleShadow = 0
modelplyDisplay.DataAxesGrid.YTitleOpacity = 1.0
modelplyDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
modelplyDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
modelplyDisplay.DataAxesGrid.ZTitleFontFile = ''
modelplyDisplay.DataAxesGrid.ZTitleBold = 0
modelplyDisplay.DataAxesGrid.ZTitleItalic = 0
modelplyDisplay.DataAxesGrid.ZTitleFontSize = 12
modelplyDisplay.DataAxesGrid.ZTitleShadow = 0
modelplyDisplay.DataAxesGrid.ZTitleOpacity = 1.0
modelplyDisplay.DataAxesGrid.FacesToRender = 63
modelplyDisplay.DataAxesGrid.CullBackface = 0
modelplyDisplay.DataAxesGrid.CullFrontface = 1
modelplyDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
modelplyDisplay.DataAxesGrid.ShowGrid = 0
modelplyDisplay.DataAxesGrid.ShowEdges = 1
modelplyDisplay.DataAxesGrid.ShowTicks = 1
modelplyDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
modelplyDisplay.DataAxesGrid.AxesToLabel = 63
modelplyDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
modelplyDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
modelplyDisplay.DataAxesGrid.XLabelFontFile = ''
modelplyDisplay.DataAxesGrid.XLabelBold = 0
modelplyDisplay.DataAxesGrid.XLabelItalic = 0
modelplyDisplay.DataAxesGrid.XLabelFontSize = 12
modelplyDisplay.DataAxesGrid.XLabelShadow = 0
modelplyDisplay.DataAxesGrid.XLabelOpacity = 1.0
modelplyDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
modelplyDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
modelplyDisplay.DataAxesGrid.YLabelFontFile = ''
modelplyDisplay.DataAxesGrid.YLabelBold = 0
modelplyDisplay.DataAxesGrid.YLabelItalic = 0
modelplyDisplay.DataAxesGrid.YLabelFontSize = 12
modelplyDisplay.DataAxesGrid.YLabelShadow = 0
modelplyDisplay.DataAxesGrid.YLabelOpacity = 1.0
modelplyDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
modelplyDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
modelplyDisplay.DataAxesGrid.ZLabelFontFile = ''
modelplyDisplay.DataAxesGrid.ZLabelBold = 0
modelplyDisplay.DataAxesGrid.ZLabelItalic = 0
modelplyDisplay.DataAxesGrid.ZLabelFontSize = 12
modelplyDisplay.DataAxesGrid.ZLabelShadow = 0
modelplyDisplay.DataAxesGrid.ZLabelOpacity = 1.0
modelplyDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
modelplyDisplay.DataAxesGrid.XAxisPrecision = 2
modelplyDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
modelplyDisplay.DataAxesGrid.XAxisLabels = []
modelplyDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
modelplyDisplay.DataAxesGrid.YAxisPrecision = 2
modelplyDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
modelplyDisplay.DataAxesGrid.YAxisLabels = []
modelplyDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
modelplyDisplay.DataAxesGrid.ZAxisPrecision = 2
modelplyDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
modelplyDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
modelplyDisplay.PolarAxes.Visibility = 0
modelplyDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
modelplyDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
modelplyDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
modelplyDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
modelplyDisplay.PolarAxes.EnableCustomRange = 0
modelplyDisplay.PolarAxes.CustomRange = [0.0, 1.0]
modelplyDisplay.PolarAxes.PolarAxisVisibility = 1
modelplyDisplay.PolarAxes.RadialAxesVisibility = 1
modelplyDisplay.PolarAxes.DrawRadialGridlines = 1
modelplyDisplay.PolarAxes.PolarArcsVisibility = 1
modelplyDisplay.PolarAxes.DrawPolarArcsGridlines = 1
modelplyDisplay.PolarAxes.NumberOfRadialAxes = 0
modelplyDisplay.PolarAxes.AutoSubdividePolarAxis = 1
modelplyDisplay.PolarAxes.NumberOfPolarAxis = 0
modelplyDisplay.PolarAxes.MinimumRadius = 0.0
modelplyDisplay.PolarAxes.MinimumAngle = 0.0
modelplyDisplay.PolarAxes.MaximumAngle = 90.0
modelplyDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
modelplyDisplay.PolarAxes.Ratio = 1.0
modelplyDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.PolarAxisTitleVisibility = 1
modelplyDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
modelplyDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
modelplyDisplay.PolarAxes.PolarLabelVisibility = 1
modelplyDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
modelplyDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
modelplyDisplay.PolarAxes.RadialLabelVisibility = 1
modelplyDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
modelplyDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
modelplyDisplay.PolarAxes.RadialUnitsVisibility = 1
modelplyDisplay.PolarAxes.ScreenSize = 10.0
modelplyDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
modelplyDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
modelplyDisplay.PolarAxes.PolarAxisTitleFontFile = ''
modelplyDisplay.PolarAxes.PolarAxisTitleBold = 0
modelplyDisplay.PolarAxes.PolarAxisTitleItalic = 0
modelplyDisplay.PolarAxes.PolarAxisTitleShadow = 0
modelplyDisplay.PolarAxes.PolarAxisTitleFontSize = 12
modelplyDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
modelplyDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
modelplyDisplay.PolarAxes.PolarAxisLabelFontFile = ''
modelplyDisplay.PolarAxes.PolarAxisLabelBold = 0
modelplyDisplay.PolarAxes.PolarAxisLabelItalic = 0
modelplyDisplay.PolarAxes.PolarAxisLabelShadow = 0
modelplyDisplay.PolarAxes.PolarAxisLabelFontSize = 12
modelplyDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
modelplyDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
modelplyDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
modelplyDisplay.PolarAxes.LastRadialAxisTextBold = 0
modelplyDisplay.PolarAxes.LastRadialAxisTextItalic = 0
modelplyDisplay.PolarAxes.LastRadialAxisTextShadow = 0
modelplyDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
modelplyDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
modelplyDisplay.PolarAxes.EnableDistanceLOD = 1
modelplyDisplay.PolarAxes.DistanceLODThreshold = 0.7
modelplyDisplay.PolarAxes.EnableViewAngleLOD = 1
modelplyDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
modelplyDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
modelplyDisplay.PolarAxes.PolarTicksVisibility = 1
modelplyDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
modelplyDisplay.PolarAxes.TickLocation = 'Both'
modelplyDisplay.PolarAxes.AxisTickVisibility = 1
modelplyDisplay.PolarAxes.AxisMinorTickVisibility = 0
modelplyDisplay.PolarAxes.ArcTickVisibility = 1
modelplyDisplay.PolarAxes.ArcMinorTickVisibility = 0
modelplyDisplay.PolarAxes.DeltaAngleMajor = 10.0
modelplyDisplay.PolarAxes.DeltaAngleMinor = 5.0
modelplyDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
modelplyDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
modelplyDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
modelplyDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
modelplyDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
modelplyDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
modelplyDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
modelplyDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
modelplyDisplay.PolarAxes.ArcMajorTickSize = 0.0
modelplyDisplay.PolarAxes.ArcTickRatioSize = 0.3
modelplyDisplay.PolarAxes.ArcMajorTickThickness = 1.0
modelplyDisplay.PolarAxes.ArcTickRatioThickness = 0.5
modelplyDisplay.PolarAxes.Use2DMode = 0
modelplyDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=modelply)
extractSurface1.PieceInvariant = 1
extractSurface1.NonlinearSubdivisionLevel = 1

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.AmbientColor = [1.0, 1.0, 1.0]
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
extractSurface1Display.OSPRayScaleArray = 'TCoords'
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.OSPRayMaterial = 'None'
extractSurface1Display.Orient = 0
extractSurface1Display.OrientationMode = 'Direction'
extractSurface1Display.SelectOrientationVectors = 'None'
extractSurface1Display.Scaling = 0
extractSurface1Display.ScaleMode = 'No Data Scaling Off'
extractSurface1Display.ScaleFactor = 0.025753611326217653
extractSurface1Display.SelectScaleArray = 'None'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.UseGlyphTable = 0
extractSurface1Display.GlyphTableIndexArray = 'None'
extractSurface1Display.UseCompositeGlyphTable = 0
extractSurface1Display.UseGlyphCullingAndLOD = 0
extractSurface1Display.LODValues = []
extractSurface1Display.ColorByLODIndex = 0
extractSurface1Display.GaussianRadius = 0.0012876805663108826
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
extractSurface1Display.SetScaleArray = ['POINTS', 'TCoords']
extractSurface1Display.ScaleArrayComponent = 'X'
extractSurface1Display.UseScaleFunction = 1
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityByArray = 0
extractSurface1Display.OpacityArray = ['POINTS', 'TCoords']
extractSurface1Display.OpacityArrayComponent = 'X'
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
extractSurface1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
extractSurface1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.XTitleFontFile = ''
extractSurface1Display.DataAxesGrid.XTitleBold = 0
extractSurface1Display.DataAxesGrid.XTitleItalic = 0
extractSurface1Display.DataAxesGrid.XTitleFontSize = 12
extractSurface1Display.DataAxesGrid.XTitleShadow = 0
extractSurface1Display.DataAxesGrid.XTitleOpacity = 1.0
extractSurface1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
extractSurface1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.YTitleFontFile = ''
extractSurface1Display.DataAxesGrid.YTitleBold = 0
extractSurface1Display.DataAxesGrid.YTitleItalic = 0
extractSurface1Display.DataAxesGrid.YTitleFontSize = 12
extractSurface1Display.DataAxesGrid.YTitleShadow = 0
extractSurface1Display.DataAxesGrid.YTitleOpacity = 1.0
extractSurface1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
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
extractSurface1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
extractSurface1Display.DataAxesGrid.ShowGrid = 0
extractSurface1Display.DataAxesGrid.ShowEdges = 1
extractSurface1Display.DataAxesGrid.ShowTicks = 1
extractSurface1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
extractSurface1Display.DataAxesGrid.AxesToLabel = 63
extractSurface1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
extractSurface1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.XLabelFontFile = ''
extractSurface1Display.DataAxesGrid.XLabelBold = 0
extractSurface1Display.DataAxesGrid.XLabelItalic = 0
extractSurface1Display.DataAxesGrid.XLabelFontSize = 12
extractSurface1Display.DataAxesGrid.XLabelShadow = 0
extractSurface1Display.DataAxesGrid.XLabelOpacity = 1.0
extractSurface1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
extractSurface1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
extractSurface1Display.DataAxesGrid.YLabelFontFile = ''
extractSurface1Display.DataAxesGrid.YLabelBold = 0
extractSurface1Display.DataAxesGrid.YLabelItalic = 0
extractSurface1Display.DataAxesGrid.YLabelFontSize = 12
extractSurface1Display.DataAxesGrid.YLabelShadow = 0
extractSurface1Display.DataAxesGrid.YLabelOpacity = 1.0
extractSurface1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
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
extractSurface1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
extractSurface1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
extractSurface1Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface1Display.PolarAxes.PolarAxisTitleBold = 0
extractSurface1Display.PolarAxes.PolarAxisTitleItalic = 0
extractSurface1Display.PolarAxes.PolarAxisTitleShadow = 0
extractSurface1Display.PolarAxes.PolarAxisTitleFontSize = 12
extractSurface1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
extractSurface1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
extractSurface1Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface1Display.PolarAxes.PolarAxisLabelBold = 0
extractSurface1Display.PolarAxes.PolarAxisLabelItalic = 0
extractSurface1Display.PolarAxes.PolarAxisLabelShadow = 0
extractSurface1Display.PolarAxes.PolarAxisLabelFontSize = 12
extractSurface1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
extractSurface1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
extractSurface1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
extractSurface1Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface1Display.PolarAxes.LastRadialAxisTextBold = 0
extractSurface1Display.PolarAxes.LastRadialAxisTextItalic = 0
extractSurface1Display.PolarAxes.LastRadialAxisTextShadow = 0
extractSurface1Display.PolarAxes.LastRadialAxisTextFontSize = 12
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
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
Hide(modelply, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData('model.stl', proxy=extractSurface1, FileType='Ascii',
    WriteTimeSteps=0)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.7449932456512144, -0.008460191575401527, 0.07168099272384612]
renderView1.CameraFocalPoint = [-0.0005472525954246521, -0.006206795573234558, -0.01217762753367424]
renderView1.CameraViewUp = [-0.010928766284721721, 0.9974719757219301, -0.0702155233326876]
renderView1.CameraParallelScale = 0.1938962672602083

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
