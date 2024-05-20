import pytesseract
import cv2
import pyautogui
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_digit_from_image(image_path, output_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scale_percent = 200
    width = int(gray_image.shape[1] * scale_percent / 100)
    height = int(gray_image.shape[0] * scale_percent / 100)
    dim = (width, height)
    upscaled_image = cv2.resize(gray_image, dim, interpolation=cv2.INTER_LINEAR)

    #SAVES THE CHANGED IMAGE
    #cv2.imwrite(output_path, upscaled_image)

    # Use pytesseract to extract text (digits) from the image
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    digit = pytesseract.image_to_string(upscaled_image, config=custom_config)

    # Clean up the extracted text (remove non-digit characters)
    digit = ''.join(filter(str.isdigit, digit))

    return int(digit) if digit else 0

def READ_SCREEN():
    table = ""
    for i in range(9):
        for j in range(9):
            xoffset = (j - 1) / 3 * 2 + j * 48
            yoffset = (i - 1) / 3 * 2 + i * 48
            photo_name = str(i + 1) + str(j + 1) + ".png"
            pyautogui.screenshot(photo_name, region=(268 + int(xoffset), 208 + int(yoffset), 32, 32))
            d = extract_digit_from_image(photo_name, photo_name)
            #print(str(i + 1) + " " + str(j + 1) + "=", d)
            if j!=8: table = table + str(d) + " "
            else: table = table + str(d)
        table = table + '\n'
        #print(str((i+1)*10) + "%")
    f = open("date.in", "w")
    f.write(table)
    f.close()
