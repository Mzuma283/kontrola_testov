from __future__ import print_function
import cv2 as cv
import pypdfium2 as pdfium
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range


# pdf = pdfium.PdfDocument("fotky\klokan_nevyplnene.pdf")
# n_pages = len(pdf)
# for page_number in range(n_pages):
#     page = pdf.get_page(page_number)
#     pil_image = page.render_topil(
#         scale=1,
#         rotation=0,
#         crop=(0, 0, 0, 0),
#         #colour=(255, 255, 255, 255),
#         #annotations=True,
#         greyscale=False,
#         optimise_mode=pdfium.OptimiseMode.NONE,
#     )
#     pil_image.save(f"fotky/image_{page_number+1}.png")

def control(test):
    # load the input images
    img = cv.imread(test)
    img_correct = cv.imread('fotky/image_2.png')
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
    cv.imwrite("Cropped Image.jpg", cropped_image)
    cv.imwrite("Cropped Image2.jpg", cropped_image2)
    cv.imwrite("Cropped Image3.jpg", cropped_image3)
    cv.waitKey(0)
    cv.destroyAllWindows()

    img1 = cv.imread('Cropped Image2.jpg')
    img2 = cv.imread('Cropped Image3.jpg')

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
    result = 'fotky/result.png'
    cv.imwrite(result, diff)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # img1 = cv.imread('Cropped Image3.jpg')
    # img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    # h, w = img1.shape

    # img2 = cv.imread('Cropped Image2.jpg')
    # img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    # img3 = cv.imread('Cropped Image4.jpg')
    # img3 = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)

    # def error(img1, img2):
    #     diff = cv.subtract(img1, img2)
    #     err = np.sum(diff**2)
    #     mse = err/(float(h*w))
    #     msre = np.sqrt(mse)
    #     return mse, diff

    # match_error12, diff12 = error(img1, img2)
    # match_error13, diff13 = error(img1, img3)
    # match_error23, diff23 = error(img2, img3)

    # print("Image matching Error between image 1 and image 2:",match_error12)
    # print("Image matching Error between image 1 and image 3:",match_error13)
    # print("Image matching Error between image 2 and image 3:",match_error23)

    # plt.subplot(221), plt.imshow(diff12,'gray'),plt.title("image1 - Image2"),plt.axis('off')
    # plt.subplot(222), plt.imshow(diff13,'gray'),plt.title("image1 - Image3"),plt.axis('off')
    # plt.subplot(223), plt.imshow(diff23,'gray'),plt.title("image2 - Image3"),plt.axis('off')
    # plt.show()

    image = cv.imread('fotky/result.png')
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
    cv.imwrite('contours_none_image1.jpg', rgb)
    cv.destroyAllWindows()

    count = int(len(cnt))
    # print("Squares in the image : ", count)

    try: 
        os.remove("contours_none_image1.jpg")
    except: pass
    try: 
        os.remove(result)
    except: pass
    try: 
        os.remove("Cropped Image.jpg")
    except: pass
    try: 
        os.remove("Cropped Image3.jpg")
    except: pass
    try: 
        os.remove("Cropped Image2.jpg")
    except: pass

    return count