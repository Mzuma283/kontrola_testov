import cv2 as cv

img = cv.imread('uml_graph.png')

cv.imshow('uml_graph', img)

cv.waitKey(0)