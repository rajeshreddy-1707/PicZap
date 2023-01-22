from skimage.metrics import structural_similarity
import argparse
import imutils
import cv2

x = int(input("Enter no."))
n = 1814
z = 0

for i in range(0, x):
    n = n+1
    z = str(n)

    # load the two input images
    imageA = cv2.imread("D://Code/Input/2000/Image ("+z+").jpg")
    imageB = cv2.imread("D://Code/Compress/compressed ("+z+").jpg")

    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("{}".format(score), file=open("D://Code/Compress/SSIM.txt", "a"))
    print(n)
    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ

    # thresh = cv2.threshold(diff, 0, 255,
    # cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    # cv2.CHAIN_APPROX_SIMPLE)
    #cnts = imutils.grab_contours(cnts)

    # loop over the contours

    # for c in cnts:
    #(x, y, w, h) = cv2.boundingRect(c)
    #cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # show the output images
    #cv2.imshow("Original", imageA)
    #cv2.imshow("Modified", imageB)
    #cv2.imshow("Diff", diff)
    #cv2.imshow("Thresh", thresh)
    # cv2.waitKey(0)
