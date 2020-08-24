import cv2
import copy
import os
# import numpy as np
# import tkinter

list_of_NOs = ('no', 'NO', 'No', 'n')
list_of_YES = ('yes', 'YES', 'Yes', 'y')
list_of_ROWS = ('rows', 'ROWS', 'R', 'r', 'Rows', 'row', 'Row', 'ROW')
list_of_COLS = ('columns', 'COLUMNS', 'C', 'c', 'Columns', 'column', 'Column', 'COLUMN')
def modify():
    print("NOT YET READY!")
    # cv2.namedWindow("CONTROL")
    # cv2.createTrackbar("BRIGHTNESS", "CONTROL", )
    # pic.set(10, 100)
    # cv2.imshow("modify", pic)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def gray_convert(img):
    # print("Basic Conversion into B&W : ")
    g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("BASIC CONVERSION", g_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return g_img
    # choice = input("Want to make modifications in contrast and Brightness?? ")
    # while True:
    #     choice = input("Want to make modifications in contrast and Brightness?? ")
    #     if choice in list_of_YES:
    #         modify()
    #         break
    #     elif choice in list_of_NOs:
    #         break
    #     else:
    #         print("YOUR CHOICE IS INVALID, PLEASE TRY AGAIN")

# pic_path = r"frame_at_6.jpg"
# pic = cv2.imread(pic_path)
# ch = input("CONVERT IMAGE TO GRAY? ")
# if ch in list_of_YES:
#     gray_convert(pic)
# elif ch in list_of_NOs:
#     pass
# else:
#     print("YOUR CHOICE IS INVALID, PLEASE TRY AGAIN")
#
# def grid_print(img):
#     row_boxes = int(input("Enter no.of boxes in rows : "))

def main():
    print("                    ART GRID MAKER")
    #Path = input("ENTER THE PATH of your image file : ")
    # Path = r""
    print("NOTE: Please copy the input image onto the DESKTOP of your DEVICE for successful EXECUTION.\n")
    Path = input("Enter the IMAGE Path : ")
    pic = cv2.imread(Path)

    cv2.imshow("YOUR IMAGE", pic)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    while True:
        choice = input("Do you want to convert image to GRAYSCALE? ")
        if choice in list_of_YES:
            pic = gray_convert(pic)
            break
        elif choice in list_of_NOs:
            break
        else:
            print("YOUR CHOICE IS INVALID, PLEASE TRY AGAIN")
    while True:
        choice = input("Wanna ROTATE the image? ")
        if choice in list_of_YES:
            pic = cv2.rotate(pic, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow("ROTATED", pic)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif choice in list_of_NOs:
            break
        else:
            print("YOUR CHOICE IS INVALID, PLEASE TRY AGAIN")
    height = pic.shape[0]
    width = pic.shape[1]
    u_height = 0
    hcount = 0
    wcount = 0
    u_width = 0

    print("GRID PRINTING................")
    Sq = input("DO YOU WANT SQUARE GRIDS? ")
    if Sq in list_of_YES:
        while True:
            custom = input("Customize ROWS or COLUMNS (R/C): ")
            if custom in list_of_ROWS:
                rows = int(input("Enter no.of rows: "))
                u_height = height // rows
                u_width = copy.copy(u_height)
                hcount = copy.copy(u_height)
                wcount = copy.copy(hcount)
                print("H : ", hcount, " W : ", wcount)
                break
            elif custom in list_of_COLS:
                cols = int(input("Enter no.of columns: "))
                u_width = width // cols
                u_height = copy.copy(u_width)
                wcount = copy.copy(u_width)
                hcount = copy.copy(wcount)
                print("H : ", hcount, " W : ", wcount)
                break
            else:
                print("INVALID .. TRY A DIFFERENT CHOICE")
                continue
    elif Sq in list_of_NOs:
        print("CUSTOM ROWS AND COLUMNS MODE: ")
        rows = int(input("Enter no.of rows: "))
        cols = int(input("Enter no.of columns: "))
        print("H : ", height, " W : ", width)
        u_height = height // rows
        u_width = width // cols
        hcount = copy.copy(u_height)
        wcount = copy.copy(u_width)
    else:
        print("INVALID CHOICE.........END OF EXECUTION")
        input()
        return 0

    print("H : ", hcount, " W : ", wcount)
    color = input("ENTER COLOR of GRID (B/W): ")
    c_tuple = (255, 255, 255)
    if color in ('B', 'b', 'Black', 'BLACK'):
        c_tuple = (0, 0, 0)
    # cv2.line(pic, (0, hcount), (width, hcount), c_tuple)
    # cv2.line(pic, (wcount, 0), (wcount, height), c_tuple)
    while True:
        if height >= hcount >= 0:
            cv2.line(pic, (0, hcount), (width, hcount), c_tuple, 5)
            hcount += u_height
        else:
            break
    while True:
        if width >= wcount >= 0:
            cv2.line(pic, (wcount, 0), (wcount, height), c_tuple, 5)
            wcount += u_width
        else:
            break
    cv2.imshow("MAIN PICTURE", pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_choice = input("DO YOU WANT TO SAVE THE FINAL IMAGE? ")
    if save_choice in list_of_YES:
        Directory = input("ENTER PATH OF DIRECTORY WHERE IMAGE HAS TO BE SAVED : ")
        os.chdir(Directory)
        filename = input("Enter file name [WITHOUT extension] : ")
        filename += '.jpg'
        cv2.imwrite(filename, pic)
        print("IMG SAVED................EXECUTION SUCCESSFUL")
        return 0
    elif save_choice in list_of_NOs:
        print('IMAGE UNSAVED!!!!!!!!! EXIT')
        input()
        return 0
    else:
        print("INVALID CHOICE.........END OF EXECUTION....IMG UNSAVED")
        input()
        return 0

main()