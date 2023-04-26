from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image

root = Tk()

root.title("Image Viewer")
root.geometry("1000x1000")
root.configure(background="wheat")

lbl_image = Label(root,bg="white")
lbl_image.place(relx=0.5,rely=0.5,anchor=CENTER)

image_path = ""

def openFile():
    global image_path
    image_path = filedialog.askopenfilename(title="Open Image File",filetypes=[("Image Files","*.jpg *.gif *.png *.jpeg")])
    print(image_path)
    
    img= Image.open(image_path)
    img1 = ImageTk.PhotoImage(img)
    lbl_image["image"]=img1
    img1.close()

btn_oi = Button(root,text="Open Image",command=openFile)
btn_oi.place(relx=0.5,rely=0.1,anchor=CENTER)

def rotateImage():
    global image_path
    img = Image.open(image_path)
    img1 = ImageTk.PhotoImage(img.rotate(180))
    lbl_image["image"]=img1
    img1.close()
    
btn_rot = Button(root,text="Rotate Image",command=rotateImage)
btn_rot.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()