import cv2 as cv
import os

"""
    Convert tiff format to png + horizontal cropped tiff remote sensing image
"""
def Convert_To_Png_AndCut(dir):
    files = os.listdir(dir)
    ResultPath1 = "RS_ToPngDir/" # Define the save path after format conversion
    ResultPath2 = "RS_Cut_Result/" # Define the saving path after cutting
    for file in files: # The for loop can be removed here
        a, b = os.path.splitext(file) # file name of split image
        this_dir = os.path.join(dir + file) # Build save path + file name
        
        #img = cv.imread(this_dir, 1) # read tif image
        import tifffile as tifi
        img = tifi.imread("123/eso1242a.tif")
        # The second parameter is the number of channels and bit depth parameters,
        # IMREAD_UNCHANGED = -1 # No conversion. For example, if you save a 16-bit image, it will still be 16-bit when read.
        # IMREAD_GRAYSCALE = 0 # Perform conversion to grayscale image, for example, save as a 16-bit image, read out as 8-bit, and the type is CV_8UC1.
        # IMREAD_COLOR = 1 # Convert to RGB three-channel image, and the image depth is converted to 8 bits
        # IMREAD_ANYDEPTH = 2 # Keep the image depth unchanged, and convert to grayscale.
        # IMREAD_ANYCOLOR = 4 # If the number of image channels is less than or equal to 3, the original channel number will remain unchanged; if the number of channels is greater than 3, only the first three channels will be taken. The image depth is converted to 8 bits
        
        #cv.imwrite(ResultPath1 + a + "_" + ".png", img) # save as png format
        
        # Start cropping below-you can comment out the tiff format without cropping
        hight = img.shape[0] #opencv wording, get width and height
        width = img.shape[1]
        #Define crop size
        w = 250 # width
        h = 250 # height
        _id = 1 # File name for saving the cropping result: 0-N in ascending order
        i = 0
        while (i + h <= hight): # Control the height, the sum of the extra fixed size of the image is not needed
            j = 0
            while (j + w <= width): # Control the width, the sum of the extra fixed size of the image is not needed
                cropped = img[i:i + h, j:j + w] # The cropping coordinates are [y0:y1, x0:x1]
                cv.imwrite(ResultPath2 + a + "_" + str(_id) + ".jpg", cropped)
                _id += 1
                j += w
            i = i + h
"""
    Horizontal cropping of PNG images
"""
def toCutPng(dir):
    files = os.listdir(dir)
    ResultPath = "./RS_CutPng_Result/" # Define the saving path after cutting
    for file in files:
        a, b = os.path.splitext(file) # file name of split image
        this_dir = os.path.join(dir + file)
        img = Image.open(this_dir) # Open an image in order
        width, hight = img.size
        w = 480 # width
        h = 360 # height
        _id = 1 # File name for saving the cropping result: 0-N in ascending order
        y = 0
        while (y + h <= hight): # Control the height, the sum of the extra fixed size of the image is not needed
            x = 0
            while (x + w <= width): # Control the width, the sum of the extra fixed size of the image is not needed
                new_img = img.crop((x, y, x + w, y + h))
                new_img.save(ResultPath + a + "_" + str(_id) + b)
                _id += 1
                x += w
            y = y + h

if __name__ =='__main__':
    _path = r"123/" # The path of the remote sensing tiff image
    # Crop image
Convert_To_Png_AndCut(_path)
