from tkinter import *
from tkinter import filedialog
import cv2


def openfile():
    filepath = filedialog.askopenfilename()
    print(filepath)
    img = cv2.imread(filepath)
    Convert(filepath,img)

def Convert(filepath,image):
    original_image = cv2.imread(filepath)
    Gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    Gray_image = cv2.medianBlur(Gray_image, 5)
    detect_edge = cv2.adaptiveThreshold(Gray_image, 225, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image,9,250,250)
    output =cv2.bitwise_and(color, color, mask = detect_edge)

    cv2.imshow("Original picture" , original_image)
    cv2.imshow("Cartoon Effect " , output)
    cv2.waitKey(0)
    cv2.destroyAllWindow()


def savefile():
    print("file is saved")
def closeapplication():
    window.quit()
window = Tk()

menubar =  Menu(window)

window.config(menu=menubar)
filemenu = Menu(menubar)
menubar.add_cascade(label="file",menu=filemenu)
filemenu.add_command(label="open",command= openfile)
filemenu.add_command(label="save",command= savefile)
filemenu.add_separator()
filemenu.add_command(label="exit",command= closeapplication)
window.mainloop()


