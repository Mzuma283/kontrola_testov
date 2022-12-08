from __future__ import print_function
import cv2 as cv
import pypdfium2 as pdfium
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
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

# load the input images
img1 = cv.imread('fotky\image_2.png')
img2 = cv.imread('fotky\image_4.png')

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
count -= 1
print("Squares in the image : ", count)

try: 
    os.remove("contours_none_image1.jpg")
except: pass
try: 
    os.remove(result)
except: pass
# def angle_cos(p0, p1, p2):
#     d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
#     return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

# def find_squares(img):
#     img = cv.GaussianBlur(img, (5, 5), 0)
#     squares = []
#     for gray in cv.split(img):
#         for thrs in xrange(0, 255, 26):
#             if thrs == 0:
#                 bin = cv.Canny(gray, 0, 50, apertureSize=5)
#                 bin = cv.dilate(bin, None)
#             else:
#                 _retval, bin = cv.threshold(gray, thrs, 255, cv.THRESH_BINARY)
#             contours, _hierarchy = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#             for cnt in contours:
#                 cnt_len = cv.arcLength(cnt, True)
#                 cnt = cv.approxPolyDP(cnt, 0.02*cnt_len, True)
#                 if len(cnt) == 4 and cv.contourArea(cnt) > 1000 and cv.isContourConvex(cnt):
#                     cnt = cnt.reshape(-1, 2)
#                     max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
#                     if max_cos < 0.1:
#                         squares.append(cnt)
#     return squares

# def main():
#     from glob import glob
#     for fn in glob('../data/pic*.png'):
#         img = cv.imread(fn)
#         squares = find_squares(img)
#         cv.drawContours( img, squares, -1, (0, 255, 0), 3 )
#         cv.imshow('squares', img)
#         ch = cv.waitKey()
#         if ch == 27:
#             break

#     print('Done')


# if __name__ == '__main__':
#     print(__doc__)
#     main()
#     cv.destroyAllWindows()