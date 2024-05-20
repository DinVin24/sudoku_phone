#import mouse
import keyboard
from main import *
from test_reading import *
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#import time

#def click_mouse(x, y):
#    mouse.move(x, y, absolute=True)
#    mouse.press(button='left')
#    time.sleep(0.2)
#    mouse.release(button='left')

READ_SCREEN()

sudoku = read_puzzle("date.in")
solve_sudoku(sudoku, 1, 1)
#print_puzzle(sudoku)
buttons = [0, (288,840),(337,840),(384,840),(432,840),(477,840),(525,840),(577,840),(619,840),(670,840)]

for i in range (9):
    for j in range (9):
        if sudoku[i+1][j+1].fix==False:
            if keyboard.is_pressed('o'):
                break
            xoffset = (j - 1) / 3 * 2 + j * 48
            yoffset = (i - 1) / 3 * 2 + i * 48
            pyautogui.moveTo(284+xoffset, 224+yoffset)
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            pyautogui.moveTo(buttons[sudoku[i+1][j+1].val][0],buttons[sudoku[i+1][j+1].val][1])
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
    if keyboard.is_pressed('o'):
        break
pyautogui.moveTo(0,0)

