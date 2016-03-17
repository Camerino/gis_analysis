import osgeo.ogr
shapefile = osgeo.ogr.Open("/home/alimjan/develop/shapefiles/tl_2009_us_state.shp")
numLayers = shapefile.GetLayerCount()
print "Shapefile contains %d layers" % numLayers
print
for layerNum in range(numLayers):
    layer = shapefile.GetLayer(layerNum)
    spatialRef = layer.GetSpatialRef().ExportToWkt()
    numFeatures = layer.GetFeatureCount()
    print "Layer %d has spatial reference %s" % (layerNum, spatialRef)
    print "Layer %d has %d features:" % (layerNum, numFeatures)
    print
for featureNum in range(numFeatures):
    feature = layer.GetFeature(featureNum)
    featureName = feature.GetField("NAME")
    print "Feature %d has name %s" % (featureNum, featureName)

	