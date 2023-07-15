# https://note.nkmk.me/en/python-pillow-qrcode/
# pyqrcode
# https://pypi.org/project/qrcode/
import qrcode
img = qrcode.make("This is QR code")
img.save("youtubeQR.jpg")

# Install opencv: pip install opencv-python
import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("myQRCode.jpg"))
print("Decoded text is: ", val)



# pic to greyscale
import cv2
#reading image
image = cv2.imread("dog.jpg")
#converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image inversion
# Invert the grayscale image also called the negative image, this will be our
# inverted grayscale image. Inversion is basically used to enhance details.
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
# Finally create the pencil sketch by mixing the grayscale image with the inverted blurry image. This is done
# by dividing the grayscale image by the inverted blurry image.
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of Dog", pencil_sketch)
cv2.waitKey(0)
