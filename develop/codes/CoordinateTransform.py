import pyproj

UTM_X = 565718.523517
UTM_Y = 3980998.9244

srcProj = pyproj.Proj(proj="utm", zone="11",
					  ellps="clrk66", units="m")
dstProj = pyproj.Proj(proj="longlat", ellps="WGS84",
					  datum="WGS84")

long,lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)

print "UTM zone 17 coordinate (%0.4f, %0.4f) = %0.4f, %0.4f" % (UTM_X, UTM_Y, lat, long)