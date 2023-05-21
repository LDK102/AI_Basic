from email.mime import message
import cv2
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk ,Image
from matplotlib.pyplot import show
import numpy as np
from tkinter import messagebox
from tensorflow import keras
from tkinter import filedialog
from keras.utils import load_img
from keras.utils.image_utils import img_to_array
# Load model
model = keras.models.load_model('Final.h5') 

window = tk.Tk()
window.title("FINAL REPORT")
window.geometry("950x600")

#Load hình 
imgLogo = Image.open("HCMUTE.png")
resizeimage=imgLogo.resize((85,95),Image.ANTIALIAS)
imgShowHCMUTE =  ImageTk.PhotoImage(resizeimage)

imgkhoa = Image.open("CKM.png").resize((90,90),Image.ANTIALIAS)
imgShowkhoa = ImageTk.PhotoImage(imgkhoa)

imgLOGO = Image.open("LOGO.png").resize((600,110),Image.ANTIALIAS)
imgShowLOGO = ImageTk.PhotoImage(imgLOGO)

imgApple = Image.open("apple.png").resize((200,300),Image.ANTIALIAS)
imgShowApple = ImageTk.PhotoImage(imgApple)

imgAppleTree = Image.open("AppleTree.png").resize((200,300),Image.ANTIALIAS)
imgShowAppleTree = ImageTk.PhotoImage(imgAppleTree)

imgAppleLeaf = Image.open("AppleLeaf.png").resize((200,300),Image.ANTIALIAS)
imgShowAppleLeaf = ImageTk.PhotoImage(imgAppleLeaf)

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

# Create chuong trinh con
def show_frame(frame):
    frame.tkraise() 

# Function to perform leaf disease prediction
def Disease_Predict(image_path):
    img = Image.open(image_path).resize((240, 240))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction using the loaded model
    prediction = model.predict(img_array)
    # Assuming the model outputs one-hot encoded labels, convert prediction to class labels
    class_labels = [' Tomato_BacterialSpot_Disease',
                     'Tomato_EarlyBlight_Disease',
                     'Tomato_Healthy',
                     'Tomato_LateBlight_Disease',
                     'Tomato_LeafMold_Disease',
                     'Tomato_MosaicVirus_Disease ',
                     'Tomato_Septoria_LeafSpot_Disease ',
                     'Tomato_SpiderMites TwoSpotted_Disease',
                     'Tomato_TargetSpot_Disease',
                     'Tomato_YellowLeaf_CurlVirus_Disease']
    predicted_label = class_labels[np.argmax(prediction)]

    result_label.config(text="Predicted Label for the image is: " + predicted_label, font=("Arial",18,'bold'),fg="#000080")
    result_label.place(x = 100,y= 400)
# Function to handle button click event
def Browse_image():
    file_path = filedialog.askopenfilename(initialdir="test_images", title="Select Image",
                                            filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))
    Disease_Predict(file_path)
    
    # Display the selected image in the GUI
    img = Image.open(file_path).resize((256,256))
    img_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(window, image=img_tk)
    img_label.image = img_tk
    img_label.place(x=350,y=120)
def confirm_exit():
    result = messagebox.askyesno("Confirmation", "Are you sure you want to exit?")
    if result:
        window.quit()
# End chương trình con ========================
login = tk.Frame(window)
frame1 = tk.Frame(window)
login.grid(row=0,column=0,sticky='nsew')
frame1.grid(row=0,column=0,sticky='nsew')

show_frame(login)
# Frame Login
login_img = tk.Label(login,text="",image=imgShowLOGO)
login_img.place(x = 0,y= 0)

login_img_1 = tk.Label(login,text="",image=imgShowAppleTree)
login_img_1.place(x = 10,y=270)

login_img_1 = tk.Label(login,text="",image=imgShowApple)
login_img_1.place(x = 210,y=270)

login_img_1 = tk.Label(login,text="",image=imgShowAppleLeaf)
login_img_1.place(x = 410,y=270)

lblNameID3 = tk.Label(login,text = "Báo Cáo Cuối Kì",font=("Aria",22,'bold'),fg="#000080")
lblNameID3.place(x=400,y=110)
lblNameID5 = tk.Label(login,text = "Đề Tài: Tomato Leaf Disease Detection",font=("Arial",18,"bold"),fg="#000080")
lblNameID5.place(x=300,y=150)
lblNameID9 = tk.Label(login,text = "GVHD: PGS.TS Nguyễn Trường Thịnh",font=("Arial",14,"bold"),fg="#000080")
lblNameID9.place(x=10,y=180)
lblNameID6 = tk.Label(login,text = "SVTH: Lê Đăng Khoa ",font=("Arial",14,"bold"),fg="#000080")
lblNameID6.place(x=10,y=210)
lblNameID7 = tk.Label(login,text = "MSSV: 20146497 ",font=("Arial",14,"bold"),fg="#000080")
lblNameID7.place(x=10,y=240)

Button(login,text="Start",height=2,width=12,bd=9,command=lambda:show_frame(frame1),bg="blue",font=('Arial',11,'bold')).place(x=700, y = 380 )

# frame 1 
frame1_btn = tk.Button(frame1,text = "Choose Test File",height=2,width=18,bd=9,command=Browse_image,bg="green",font=('Arial',11,'bold'))
frame1_btn.place(x = 400,y = 510)

frame1_btnLogout = tk.Button(frame1, text = "Back",height=1,width=10,bd=9, command=lambda:show_frame(login), bg="red")
frame1_btnLogout.place(x = 860,y = 0)

frame1_exitBtn = tk.Button(frame1, text="Exit",height=1,width=10,bd=9, command=lambda: confirm_exit(), bg="red")
frame1_exitBtn.place(x=860, y=30)

frame1_img = tk.Label(frame1,text="",image=imgShowLOGO)
frame1_img.place(x = 0,y= 0)

# Create a label to display the prediction result
result_label = tk.Label(frame1,justify=LEFT)
result_label.place(x=0,y=550)

####################################

window.mainloop()
