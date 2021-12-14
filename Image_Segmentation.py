# segments image into characters

# https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/

import cv2
import os

def segment_image(filename):

    # Read image from which text needs to be extracted
    img = cv2.imread(f"Cropped_Images/{filename}.jpg")
    cv2.imshow("original", img)

    # Preprocessing

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("grayscale", gray)

    # thresholding
    # threshold = pixel value that turns into black/white
    # OTSU finds optimal threshold value
    # returns thresh value, image
    ret, thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    cv2.imshow("thresholded", thresh_img)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    # (1, 1) detects letters
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))

    # Applying dilation on the threshold image
    # dilation = exaggerating features of the image
    dilation = cv2.dilate(thresh_img, rect_kernel, iterations=1)

    # Finding contours
    # contour = curve joining all continuous points having same color or intensity
    # finds white from black background
    # RETR_LIST = returns list of all the contours (no hierarchy)
    # CHAIN_APPROX_NONE = keep all points
    # returns list of contours, hierarchy
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_LIST,
                                           cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    print("total number of contours in image:", len(contours))

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("boxed", im2)

    # save contours to new images
    path = f"Cropped_Contours/{filename}"
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(len(contours)):
        x, y, width, height = cv2.boundingRect(contours[i])
        roi = thresh_img[y: y + height, x: x + width]
        #cv2.imwrite(os.path.join(path, f"contour{i}.png"), roi)

    cv2.waitKey(0)
