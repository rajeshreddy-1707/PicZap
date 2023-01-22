from math import log10, sqrt
import cv2
import numpy as np


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


x = int(input("Enter no."))
n = 1814
z = 0

for i in range(0, x):
    n = n+1
    z = str(n)
    original = cv2.imread(
        "D://Code/Input/2000/Image ("+z+").jpg")
    compressed = cv2.imread(
        "D://Code/Compress/compressed ("+z+").jpg")
    # compressed.show()
    value = PSNR(original, compressed)
    print(value, file=open("D://Code/Compress/PSNR.txt", "a"))
    mse = np.mean((original - compressed) ** 2)
    rmse = sqrt(mse)
    nrmse = rmse/mse
    print(nrmse, file=open("D://Code/Compress/NRMSE.txt", "a"))
    print(rmse, file=open("D://Code/Compress/RMSE.txt", "a"))
    print(mse, file=open("D://Code/Compress/MSE.txt", "a"))
    print(n)
