# importing cv2
from tkinter import filedialog
from tkinter import *
from skimage.morphology import binary_dilation, binary_erosion
import random
import numpy as np
import tkinter as tk
import sys
import os
import cv2
# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode


def watermark_image(watermark, logo):

    # calculating dimensions
    # height and width of the logo
    h_logo, w_logo, _ = logo.shape

    # height and width of the image
    h_img, w_img, _ = watermark.shape

    # calculating coordinates of center
    # calculating center, where we are going to
    # place our watermark
    center_y = int(h_img/2)
    center_x = int(w_img/2)

    # calculating from top, bottom, right and left
    top_y = center_y - int(h_logo/2)
    left_x = center_x - int(w_logo/2)
    bottom_y = top_y + h_logo
    right_x = left_x + w_logo

    # adding watermark to the image
    destination = watermark[top_y:bottom_y, left_x:right_x]
    result = cv2.addWeighted(destination, 1, logo, 0.5, 0)

    # displaying and saving image
    watermark[top_y:bottom_y, left_x:right_x] = result
    cv2.imwrite("watermarked.jpg", watermark)
    cv2.imshow("Watermarked Image", watermark)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop_image(z):
    im = Image.open(z)
    left = int(im.size[0]/2-224/2)
    upper = int(im.size[1]/2-100/2)
    right = left + 224
    lower = upper + 100
    im_cropped = im.crop((left, upper, right, lower))
    newsize = (im.size[0], im.size[1])
    im1 = im_cropped.resize(newsize)
    im1.save("cropped.jpg")
    im1.show


def compress_image(x):
    def initialize_K_centroids(X, K):
        m = len(X)
        return X[np.random.choice(m, K, replace=False), :]

    def find_closest_centroids(X, centroids):
        m = len(X)
        c = np.zeros(m)
        for i in range(m):
            # Find distances
            distances = np.linalg.norm(X[i] - centroids, axis=1)

        # Assign closest cluster to c[i]
            c[i] = np.argmin(distances)

        return c

    def compute_means(X, idx, K):
        _, n = X.shape
        centroids = np.zeros((K, n))
        for k in range(K):
            examples = X[np.where(idx == k)]
            mean = [np.mean(column) for column in examples.T]
            centroids[k] = mean
        return centroids

    def load_image(path):
        """ Load image from path. Return a numpy array """
        image = Image.open(path)
        return np.asarray(image) / 255

    def find_k_means(X, K, max_iters=10):
        centroids = initialize_K_centroids(X, K)
        previous_centroids = centroids
        # for _ in range(max_iters):
        image = load_image(x)
        w, h, d = image.shape
        print('Image found with width: {}, height: {}, depth: {}'.format(w, h, d))

        X = image.reshape((w * h, d))

        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        if (centroids == previous_centroids).all():
            return centroids
        else:
            previous_centroids = centroids

        return centroids, idx

    try:
        image_path = sys.argv[1]
        assert os.path.isfile(x)
    except (IndexError, AssertionError):
        print('Please specify an image')

    image = load_image(x)
    w, h, d = image.shape
    print('Image found with width: {}, height: {}, depth: {}'.format(w, h, d))

    X = image.reshape((w * h, d))
    K = 20

    # K = 20, the desired number of colors in the compressed image

    colors, _ = find_k_means(X, K, max_iters=20)

    idx = find_closest_centroids(X, colors)

    idx = np.array(idx, dtype=np.uint8)
    X_reconstructed = np.array(
        colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
    compressed_image = Image.fromarray(X_reconstructed)

    compressed_image.save('compressed.jpg')


def remove_watermark():
    img = cv2.imread('watermarked.jpg')
    mask = cv2.imread('Watermark.jpg', 0)
    dst = cv2.inpaint(img, mask, 20, cv2.INPAINT_TELEA)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def openFile():
    f = filedialog.askopenfilename(initialdir="D:\\Code\\Input\\2000",
                                   title="Open file okay?",
                                   filetypes=(("Image files", "*.jpg"),
                                              ("all files", "*.*")))
    # file = open(filepath, 'r')
    # print(file.read())
    # print(filepath)
    # print(f, file=open("D://Code/Path.txt", "w"))
    with open("D://Code/Path.txt", 'w') as p:
        p.write(f)


def openFile_1():
    f = filedialog.askopenfilename(initialdir="C:\\Users\\ASUS\\Pictures\\EEE Experiment\\Code",
                                   title="Open file okay?",
                                   filetypes=(("Image files", "*.jpg"),
                                              ("all files", "*.*")))
    # file = open(filepath, 'r')
    # print(file.read())
    # print(filepath)
    # print(f, file=open("D://Code/Path.txt", "w"))
    with open("D://Code/Path_1.txt", 'w') as p:
        p.write(f)

    # x = filedialog.askopenfilename()
window = Tk()
window.geometry("150x150")
window.config(background="#03071e")
button = Button(text="Open Image", command=lambda: openFile(),
                foreground="#000000")
button.config(background="#ffba08")
button.config(height=2, width=10)
button.pack()
window.mainloop()
x = open("D://Code/Path.txt", "r")
y = x.read()
y = str(y)

window = Tk()
window.geometry("150x150")
window.config(background="#03071e")
button = Button(text="Open Watermark", command=lambda: openFile_1(),
                foreground="#000000")
button.config(background="#ffba08")
button.config(height=2, width=20)
button.pack()
window.mainloop()
j = open("D://Code/Path_1.txt", "r")
i = j.read()
i = str(i)

# water(q)
print(y)
img = cv2.imread(y)
wat = cv2.imread(i)
# cv2.imshow("", wat)
# cv2.waitKey(0)
ch = 0
while(ch != 5):
    print("1.to watermark the image")
    print("2.to compress the image")
    print("3.to crop the image")
    print("4.to remove watermark")
    print("5.to exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        watermark_image(wat, img)
    elif ch == 2:
        compress_image(y)
    elif ch == 3:
        crop_image(y)
    elif ch == 4:
        remove_watermark()
    elif ch == 5:
        print(
            "----------------------------------Exiting------------------------------------")
        break
    else:
        print("Enter Valid choice")
