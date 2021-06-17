from tkinter import *
from PIL import ImageTk, Image

actualImage = 0

root = Tk()
root.title("Photo Viver")
#root.iconbitmap("")

img = ImageTk.PhotoImage(Image.open("gruby\gruby1.png"))
img1 = ImageTk.PhotoImage(Image.open("gruby\gruby2.png"))
img2 = ImageTk.PhotoImage(Image.open("gruby\gruby3.png"))
img3 = ImageTk.PhotoImage(Image.open("gruby\gruby5.png"))

zdjecia_grubaska = [img, img1, img2 , img3]

def go_back():
    global actualImage
    global MainPhoto
    global button_back
    global button_forward
    button_forward = Button(root, text=">>", command = go_forward)

    if actualImage == 1:
        button_back = Button(root, text = "<<" , state = DISABLED)

    actualImage -= 1
    MainPhoto.grid_forget()
    MainPhoto = Label(root, image = zdjecia_grubaska[actualImage])

    MainPhoto.grid_forget()
    status = Label(root, text="Image %s of %s images" % (actualImage + 1, len(zdjecia_grubaska)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=E + W)
    MainPhoto.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def go_forward():
    global actualImage
    global MainPhoto
    global button_back
    global button_forward
    button_back = Button(root, text = "<<" , command = go_back)

    if actualImage == len(zdjecia_grubaska) - 2:
        button_forward = Button(root, text=">>", state=DISABLED)

    MainPhoto.grid_forget()
    actualImage += 1
    MainPhoto = Label(root, image=zdjecia_grubaska[actualImage])
    status = Label(root, text="Image %s of %s images" % (actualImage + 1, len(zdjecia_grubaska)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=E + W)

    MainPhoto.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


MainPhoto = Label(root, image = zdjecia_grubaska[actualImage])
button_back = Button(root, text = "<<" , state = DISABLED)
button_exit = Button(root, text= "Exit Button", command = root.quit)
button_forward = Button(root, text = ">>" , command = go_forward)

MainPhoto.grid(row = 0, column = 0, columnspan = 3)
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)
status = Label(root, text = "Image %s of %s images" % (actualImage + 1, len(zdjecia_grubaska)), bd = 1, relief = SUNKEN, anchor = E)
status.grid(row = 2, column = 0,columnspan = 3, sticky = E + W)

button_back.grid()
root.mainloop()


