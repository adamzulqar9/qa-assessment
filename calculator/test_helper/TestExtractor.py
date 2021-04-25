import cv2
import pytesseract
import calculator.config as config
import pyautogui
import numpy as np


def capture_value(image):
    """
    Captures calculator image
    :param image: image name to save as
    :return: None
    """
    value = pyautogui.screenshot(region=config.capture_region)
    value = cv2.cvtColor(np.array(value), cv2.COLOR_RGB2BGR)
    cv2.imwrite(image, value)


def extract_value():
    """
    Process capture calculator image and extract value
    :return: extracted value in str
    """
    text = None

    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.pytesseract.tesseract_cmd = config.tesseract_path

    image = "calculator_value.png"
    capture_value(image)

    # Read image from which text needs to be extracted
    img = cv2.imread(image)

    # Preprocessing the image starts

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area of the rectangle to be detected.
    # A smaller value like (10, 10) will detect each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    full_text = ''
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]

        # Apply OCR on the cropped image
        custom_config = '-l eng --oem 1 --psm 10 -c preserve_interword_spaces=1 ' \
                        '-c tessedit_char_whitelist=".0123456789- " '
        text = pytesseract.image_to_string(cropped, config=custom_config)
        full_text += text

    return text.rstrip()
