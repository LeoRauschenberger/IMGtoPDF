# Imgtopdf by Leo Rauschenberger

import os, pathlib
from PIL import Image
from glob import glob

print("This script converts all JPG to PDF in the folder it is started from and also saves the PDFs there. It does not delete any files.")
print("Please make sure you have PIL, pathlib installed.")

# Please add additional formats if needed
suffix = ['.jpg','.jpeg','.png']

# -------------------------------
imglist =[]
path=os.getcwd()
imglist=glob('*.jpg')+glob('*.jpeg')+glob('*.png')

print('IMG-Files found:\n')
print(*imglist, sep = "\n")
print('\n')
print("Processing files now. Please wait...")

for i in imglist:
    dr = path+'\\'+i
    image = Image.open(dr)
    
    # Check size and reduce if necessary
    size = os.path.getsize(i)
    if size > 2000000:
        f = 2
        print("Reducing size...")
    else:
        f = 1
    width, height = image.size
    new_size = (width//f, height//f)
    resimg = image.resize(new_size)
    im = resimg.convert('RGB')
    
    # If width > than height, rotate it to get portrait 
    if im.width > im.height:
        prompt = ""
        print("Your image '"+i+"' is in Landscape.")
        while prompt not in ["Y","N"]:
            prompt = input("Want to rotate the image? Y/N: ").upper()
        if prompt == "Y":
            im=im.rotate(270,expand=True)
        elif prompt == "N":
            print("OK, keeping orientation.")
    
    # Remove suffix and replace by .pdf:
    dr2 = os.path.splitext(dr)[0]+'.pdf'
    im.save(dr2)
    

print("Done")
input("Press enter to exit.")
