# All_imgtopdf by Leo Rauschenberger
from PIL import Image
import pathlib
import os
from glob import glob

# Versions:
# 3-1 is now able to turn pdfs both directions

print("This script converts all JPG to PDF in the folder it is started from and also saves the PDFs there. \nThe script does NOT delete any files. Please do this yourself.")
print("Please make sure you have PIL, pathlib installed")

# Settings
suffix = ['.jpg','.jpeg','.png'] # Please add additional formats if needed
rename = 'y' # ('y','n') if you want to prompted to follow format YYMMDD_Store(_1)

# -------------------------------
imglist =[]
path=os.getcwd()
imglist=glob('*.jpg')+glob('*.jpeg')+glob('*.png')

print('Image-Files found:',imglist)
print("Processing files now. Please wait...")

for i in imglist:
    dr = path+'\\'+i
    image = Image.open(dr)
    #check size and reduce if necessary
    size = os.path.getsize(i)
    if size > 2000000:
        f = 2
        print("Reducing size of",i)
    else:
        f = 1
    width, height = image.size
    new_size = (width//f, height//f)
    resimg = image.resize(new_size)
    im = resimg.convert('RGB')
    #if width > than height, rotate it to get portrait 
    if im.width > im.height:
        im.show()
        prompt = input("Seems like your image is in Landscape, wanna rotate it? \nC (Clock) / CC (Counter-Clock) / N: ").upper()
        if prompt == "C":
            im=im.rotate(-90,expand=True)#clockwise
        elif prompt == "CC":
            im=im.rotate(90,expand=True) #counterclockwise
        elif prompt == "N":
            print("OK, keeping orientation")
    # generate name by removing file extension and then adding ".pdf"
    pt = pathlib.Path(dr).suffix
    dr2 = dr.removesuffix(pt) + '.pdf'
    # prompt user to fix name if format of name is wrong
    if not i[0:5].isdigit() and rename == 'y':
        print("-> It seems that your image ",i," does not follow the format YYMMDD_Store(_1) . Please fix!")
        newname = input("New name YYMMDD_Store(_1) : ")
        dr2 = path+'\\'+newname+'.pdf'
    # save file
    im.save(dr2)
    

print("Done")
input("Press enter to exit.")
