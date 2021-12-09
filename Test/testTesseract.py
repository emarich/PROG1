import pytesseract
import cv2

codeTxt = r"C:\Users\emari\Desktop\projects\PROG1\Test\code.txt"
imagePng = r"C:\Users\emari\Desktop\projects\PROG1\Test\image.png"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
img = cv2.imread(imagePng)
img = cv2.resize(img, (1920, 1080))

with open(codeTxt,"w+") as io:
	io.write(pytesseract.image_to_string(img))