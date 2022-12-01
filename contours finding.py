#contours finding
import cv2 as cv
import pypdfium2 as pdfium
import numpy as np
import matplotlib.pyplot as plt

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

# image = cv.imread('fotky\image_1.png')

# img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# # apply binary thresholding
# ret, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
# # visualize the binary image
# cv.imshow('Binary image', thresh)
# cv.waitKey(0)
# cv.imwrite('image_thres1.jpg', thresh)
# cv.destroyAllWindows()

# img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# # apply binary thresholding
# ret, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
# # detect the contours on the binary image using cv.CHAIN_APPROX_NONE
# contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
                                      
# # draw contours on the original image
# image_copy = image.copy()
# cv.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv.LINE_AA)
                
# # see the results
# cv.imshow('None approximation', image_copy)
# cv.waitKey(0)
# cv.imwrite('contours_none_image1.jpg', image_copy)
# cv.destroyAllWindows()

# load the input images
# img1 = cv.imread('fotky\image_1.png')
# img2 = cv.imread('fotky\image_2.png')

# # convert the images to grayscale
# img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
# img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# # define the function to compute MSE between two images
# def mse(img1, img2):
#    h, w = img1.shape
#    diff = cv.subtract(img1, img2)
#    err = np.sum(diff**2)
#    mse = err/(float(h*w))
#    return mse, diff

# error, diff = mse(img1, img2)
# print("Image matching Error between the two images:",error)

# cv.imshow("difference", diff)
# cv.waitKey(0)
# cv.destroyAllWindows()



img1 = cv.imread('fotky\image_1.png')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
h, w = img1.shape

img2 = cv.imread('panda1.jpg')
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
img3 = cv.imread('bike.jpg')
img3 = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)

def error(img1, img2):
   diff = cv.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   msre = np.sqrt(mse)
   return mse, diff

match_error12, diff12 = error(img1, img2)
match_error13, diff13 = error(img1, img3)
match_error23, diff23 = error(img2, img3)

print("Image matching Error between image 1 and image 2:",match_error12)
print("Image matching Error between image 1 and image 3:",match_error13)
print("Image matching Error between image 2 and image 3:",match_error23)

plt.subplot(221), plt.imshow(diff12,'gray'),plt.title("image1 - Image2"),plt.axis('off')
plt.subplot(222), plt.imshow(diff13,'gray'),plt.title("image1 - Image3"),plt.axis('off')
plt.subplot(223), plt.imshow(diff23,'gray'),plt.title("image2 - Image3"),plt.axis('off')
plt.show()