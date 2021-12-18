import cv2

img = cv2.imread("cat1.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # black-white picture

inverted_image = 255 - gray_image  # negative film

blurred = cv2.GaussianBlur(inverted_image, (9, 9), 0)  # cv2.BORDER_DEFAULT

inverted_blurred = 255 - blurred

pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# cv2.imshow("original", img)
cv2.imshow("pencil", pencil_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
