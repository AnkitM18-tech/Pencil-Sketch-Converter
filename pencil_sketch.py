import cv2

#Getting the image
image = cv2.imread("bachpan.jpg")

#Resizing the Image
image = cv2.resize(image,(900,800))

#Converting to grayscale
grayScale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Inverting the image
image_invert = cv2.bitwise_not(grayScale)

#Gaussian Blurred Image
gaussian_blur = cv2.GaussianBlur(image_invert,(23,23),sigmaX = 0,sigmaY=0)

#Sketch
sketch_image = cv2.divide(grayScale,255-gaussian_blur,scale = 256)

#Showing the pictures in a Window
cv2.imshow("Sketch Image",sketch_image)
cv2.imshow("Invert Image",image_invert)
cv2.imshow("GrayScale Image",grayScale)

#Writing in a Image file
cv2.imwrite("Picture_Sketch.jpg",sketch_image)
cv2.imwrite("Invert_Image.jpg",image_invert)
cv2.imwrite("GrayScale_Image.jpg",grayScale)

cv2.waitKey(0)