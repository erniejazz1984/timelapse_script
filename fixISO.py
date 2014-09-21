import exiftool
import os
from math import log
files = [f for f in os.listdir('.') if (os.path.isfile(f) and f.endswith(".NEF"))]
files.sort()
with exiftool.ExifTool() as et:
	metadata = et.get_metadata_batch(files)
baseISO=float(metadata[0]["EXIF:ISO"])
print "baseISO is ", baseISO
overallEV = 1.0 

for n,(d,f) in enumerate(zip(metadata,files)):	
	ISO=float(d["EXIF:ISO"])
	print "ISO for ", f, " is ", ISO
	aEV = -log(ISO/baseISO,2) + overallEV
	print "Adjust exposure value by " , aEV
	outfile = "%04d.jpg"%(n)
	print "Exporting file to ", outfile
	command = "ufraw-batch --out-type=jpg --size=1920,1080 --exposure=%f %s --output=%s"%(aEV,f,outfile)
	#command = "ufraw-batch --out-type=jpg --size=1920,1080 --exposure=auto DSC_6770.NEF --output=%s"%(outfile)
	os.system(command)
	


