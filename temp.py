import tkinter as tk

main_v = 0
root = tk.Tk()
def ret_yes():
    main_v = 1
def ret_no():
    main_v = 1
label1 = tk.Label(root, text='Hello or Hola')
label1.pack()
button1 = tk.Button(root, text="Yes", command=ret_yes())
button1.pack()
button2 = tk.Button(root, text="No", command=ret_no())
button2.pack()

if main_v:
    print("YES was selected")
else:
    print("NO was selected")
root.mainloop()


