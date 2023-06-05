# from __future__ import print_function
# import cv2 as cv
# import pypdfium2 as pdfium
# import numpy as np
# import matplotlib.pyplot as plt
# import sys
# import os
# import pandas as pd
# from tkinter import Tk
# from hladanie_chyb import control
# PY3 = sys.version_info[0] == 3

# if PY3:
#     xrange = range

# from tkinter.filedialog import askdirectory
# from tkinter import filedialog as fd

# path = askdirectory(title='Select your folder')
# print('Path: ' + path)
# path = str(path)

# entries = os.listdir(path)
# print(entries)
# correct = fd.askopenfilename(title='Select correct test')
# print('Correct test: ' + correct)
# exists = os.path.exists(path)
# print(exists)
# exists2 = os.path.exists(correct)
# print(exists2)
# path_str = str(path)
# for i in entries:
#     test = path.format(i)
#     print(test)
#     result = control(test, correct, path)
#     print('Number of mistakes: {}'.format(result))
from __future__ import print_function
import cv2 as cv
import numpy as np
import sys
import os
from tkinter import Tk
import pandas as pd
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range

from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd

def control(test, correct, path):
    # load the input images
    img = cv.imread(test)
    img_correct = cv.imread(correct)
    # print(img.shape) # Print image shape
    # cv.imshow("original", img)
    imgheight = img.shape[0]
    imgwidth=img.shape[1]
    height = int(imgheight/2)
    width = int(imgwidth)
    imgheight = int(imgheight)
    # Cropping an image
    cropped_image = img[0:height, 0:width]
    cropped_image2 = img[height:imgheight, 0:width]
    cropped_image3 = img_correct[height:imgheight, 0:width]
    cropped_image4 = img_correct[height:imgheight, 0:width]
    # Display cropped image
    # cv.imshow("cropped", cropped_image)
    # cv.imshow("cropped2", cropped_image2)
    # cv.imshow("cropped3", cropped_image3)
    # Save the cropped image
    cv.imwrite(path+"Cropped Image.jpg", cropped_image)
    cv.imwrite(path+"Cropped Image2.jpg", cropped_image2)
    cv.imwrite(path+"Cropped Image3.jpg", cropped_image3)
    cv.waitKey(0)
    cv.destroyAllWindows()

    img1 = cv.imread(path+'Cropped Image2.jpg')
    img2 = cv.imread(path+'Cropped Image3.jpg')

    # convert the images to grayscale
    img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

    # define the function to compute MSE between two images
    def mse(img1, img2):
        h, w = img1.shape
        diff = cv.subtract(img1, img2)
        err = np.sum(diff**2)
        mse = err/(float(h*w))
        return mse, diff

    error, diff = mse(img1, img2)
    print("Image matching Error between the two images:",error)

    # cv.imshow("difference", diff)
    result = path+'fotky/result.png'
    cv.imwrite(result, diff)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image = cv.imread(path+'fotky/result.png')
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    blur = cv.GaussianBlur(gray, (11, 11), 0)
    canny = cv.Canny(blur, 30, 150, 3)
    dilated = cv.dilate(canny, (1, 1), iterations=0)
    
    (cnt, hierarchy) = cv.findContours(
        dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    cv.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
    # cv.imshow('None approximation', rgb)
    cv.waitKey(0)
    cv.imwrite(path+'contours_none_image1.jpg', rgb)
    cv.destroyAllWindows()

    count = int(len(cnt))
    # print("Squares in the image : ", count)

    try: 
        os.remove(path+"contours_none_image1.jpg")
    except: pass
    try: 
        os.remove(result)
    except: pass
    try: 
        os.remove(path+"Cropped Image.jpg")
    except: pass
    try: 
        os.remove(path+"Cropped Image3.jpg")
    except: pass
    try: 
        os.remove(path+"Cropped Image2.jpg")
    except: pass

    return count

# Rest of your code...

path = askdirectory(title='Select your folder')
print('Path: ' + path)
path = str(path)

entries = os.listdir(path)
print(entries)
correct = askopenfilename(title='Select correct test')
print('Correct test: ' + correct)
exists = os.path.exists(path)
print(exists)
exists2 = os.path.exists(correct)
print(exists2)
path_str = str(path)
for i in entries:
    test = os.path.join(path, i)
    print(test)
    result = control(test, correct, path)
    print('Number of mistakes: {}'.format(result))    