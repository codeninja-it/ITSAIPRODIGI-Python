import cv2 as cv
from matplotlib import pyplot as plt

def z(d, b = 62, f = 50.0):
    return (b*f)/d

sx = cv.imread("asset/sx.jpg")
dx = cv.imread("asset/dx.jpg")

sx = cv.cvtColor(sx, cv.COLOR_BGR2GRAY)
dx = cv.cvtColor(dx, cv.COLOR_RGB2GRAY)

differenza = cv.absdiff(sx, dx)

cv.imwrite("asset/differenza.jpg", differenza)

stereo = cv.StereoBM.create(numDisparities=16, blockSize=15)
disparita = stereo.compute(sx, dx)

cv.imwrite("asset/disparita.jpg", disparita)

normalizzata = cv.normalize(disparita, None, 0, 255, cv.NORM_MINMAX)

cv.imwrite("asset/normalizzata.jpg", normalizzata)

ret, urto = cv.threshold(normalizzata, 140, 255, cv.THRESH_BINARY)

cv.imwrite("asset/urto.jpg", urto)