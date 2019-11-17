import cv2
import numpy as np
from matplotlib import pyplot as plt

#Function for load an image
def ViewImage(image, name_of_window):
	cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
	cv2.imshow(name_of_window, image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# Version of OpenCV for our project
print(cv2.__version__)

#Show a picture
image = cv2.imread('E:/SkinCancer/HAM10000_images_part_1/ISIC_0024319.jpg')
height, width, channels = image.shape

#Print size of the image
# print(height, width)

#Show a source image
# ViewImage(image, "test_pic")

#Convert image to gray colors
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ViewImage(gray_image, "gray_graduation")

#Convert an image with gray colors to hot colors
ret, threshold_image = cv2.threshold(image.copy(), 175, 255, 0)
# ViewImage(threshold_image, "SG/H")

#Convert to gray color again (from hot colors)
second_gray = cv2.cvtColor(threshold_image, cv2.COLOR_BGR2GRAY)
# ViewImage(second_gray, "H/SG")

#Blurred for find contours?
# blurred = cv2.medianBlur(second_gray, 5)
# blurred = cv2.GaussianBlur(second_gray, (5, 5), 0)

#Count black pixels
numbers_of_pixels = 0

for coord_h in range(height):
	for coord_w in range(width):
		m_pixel = second_gray[coord_h, coord_w]

		if m_pixel == 0:
			numbers_of_pixels += 1
			# second_gray[coord_h, coord_w] = 0
		else:
			second_gray[coord_h, coord_w] = 175

print(numbers_of_pixels)

blurred = cv2.GaussianBlur(second_gray, (5, 5), 0)
# blurred = cv2.blur(second_gray, (5, 5))

# contours, hierarchy = cv2.findContours(second_gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(second_gray, contours, -1, (255, 0, 0), 3, cv2.LINE_AA, hierarchy, 1)
# ViewImage(blurred, "HZ")

edges = cv2.Canny(blurred, 50, 200, 255)

# ViewImage(edges, "Edges")
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
	if cv2.contourArea(contour) > 15:
		cv2.drawContours(image, contour, -1, (0, 255, 0), 2)

ViewImage(image, "Contours")



# plt.subplot(121), plt.imshow(second_gray, cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges, cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()
