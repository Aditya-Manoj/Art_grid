import tkinter as tk
import cv2
import numpy as np
# Creating the Main GUI Window
root = tk.Tk()
e = tk.Entry(root, width=50)
e.grid(row=1, column=1)
impath = "str"

def tex():
    # text3 = e.get()
    # label3 = tk.Label(root, text="Hola " + e.get())
    # label3.grid(row=2, column=0)
    impath = e.get()

text1 = "          ART GRID MAKER"
label1 = tk.Label(root, text=text1)  # pos 0,0
# label1.grid(row=0, column=0)
label1.grid(row=0, column=0)
text2 = "Enter IMG Path : "
label2 = tk.Label(root, text=text2)  # pos 1,0
label2.grid(row=1, column=0)
button1 = tk.Button(root, text="GO", command=tex)  # pos 1,1
button1.grid(row=1, column=2)

img = cv2.imread(impath)
cv2.imshow("THE IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

root.mainloop()