# All_imgtopdf by Leo Rauschenberger
from PIL import Image
import pathlib
import os
from glob import glob

print("This script converts all JPG to PDF in the folder it is started from. It does not delete any files.")
print("Please make sure you have PIL, pathlib installed")

imglist =[]
path=os.getcwd()
imglist = glob('*.jpg')
print('*.jpg','-Files found:',imglist)

if imglist:
    print("Processing files now. Please wait...")

    for i in imglist:
        dr = path+'\\'+i
        image = Image.open(dr)
        width, height = image.size
        new_size = (width//2, height//2)
        resimg = image.resize(new_size)
        im = resimg.convert('RGB')
        dr2 = dr.removesuffix('.jpg') + '.pdf'
        im.save(dr2)
        

print("Done")
input("Press any key to exit.")
