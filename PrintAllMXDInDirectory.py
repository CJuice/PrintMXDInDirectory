###################################
# Script:  PrintAllMXDInDirectory.py
# Author:  CJuice on GitHub
# Date:  20170921
# Purpose:  Step through a directory and subdirectories looking for ESRI map documents (.mxd).
#           Export each found document to a pdf. Originally created to print a slew of mxd's created
#           for a customer request.
# Inputs: Input file directory, and output location
# Outputs: PDF of each map document
###################################
import os, sys
from arcpy import mapping

#Original
strInFileDirectory = raw_input("In Directory: ")
strOutFileDirectory = raw_input("Out Directory: ")
count = 0

for (dirname, dirs, files) in os.walk(strInFileDirectory):
    # print dirname
    # print dirs
    # print files
    # print "\n"
    # print dirname
    for filename in files:
        if filename.endswith(".mxd"): # & count <= 1
            #Needed to first rename the files to be distinct by adding the data date. Did this just once.
            # strNewName = dirname[-8:] + filename
            # os.rename(os.path.join(dirname,filename),os.path.join(dirname,strNewName))

            strMXDPath = os.path.join(dirname,filename)
            mapDoc = mapping.MapDocument(strMXDPath)
            strRootMXDName = filename[0:-4] + ".pdf"
            strNewPdfPath = os.path.join(strOutFileDirectory,strRootMXDName)
            try:
                mapping.ExportToPDF(map_document=mapDoc,out_pdf=strNewPdfPath)
            except:
                print "problem exporting to pdf"
            count+=1
            print "MXD printed: {}, count={}".format(filename,count)
            del mapDoc
print "All Done"
sys.exit()