import random
from tkinter import *
import tkinter as tk
from pygame import mixer
from datetime import time
from time import sleep
import cv2
import winsound
import requests
import os
import subprocess
import webbrowser
import json
from PIL import ImageTk, Image
import datetime
import pyperclip
import threading
import re
from tkinter import messagebox


mixer.init()

counter = 0
running = True

def stop():
	global running
	running = False





# ----------------------------------------------------YOUTUBE App --------------------------------------------------------#
def Downloader():

        import cv2, time
        face_cascade = cv2. CascadeClassifier('haarcascade_frontalface_default.xml')
        video = cv2.VideoCapture(0)

        while True:
            check,frame=video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #for face
            face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
            for x,y,w,h in face:
                img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
                img[y:y+h,x:x+w]=cv2.medianBlur(img[y:y+h,x:x+w],35)

            cv2.imshow("blur_face",frame)
            key=cv2.waitKey(1)
            if key==ord('q'):
                break    
        video.release()
        cv2.destroyAllWindows()    




        






# ----------------------------------------------------motion App -------------------------------------------------------#
def motion():
        import threading
        import pyttsx3
        import cv2
        import time
        # new


        def thread_voice_alert(engine):
            engine.say("Motion")
            engine.runAndWait()


        # new
        status_list = [None, None]
        video = cv2.VideoCapture(0)
        #result, image=video.read()

        # voice engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        first_frame = None

        while True:
            check, frame = video.read()
            # new
            status = 0
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            if first_frame is None:
                first_frame = gray
                continue
            delta_frame = cv2.absdiff(first_frame, gray)
            threshold_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
            threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

            (cntr, _) = cv2.findContours(threshold_frame.copy(),
                                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in cntr:
                if cv2.contourArea(contour) < 1000:
                    continue
                status = 1
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            status_list.append(status)

            if status_list[-1] == 1 and status_list[-2] == 0:
                t = threading.Thread(target=thread_voice_alert, args=(engine,))
                t.start()

            cv2.imshow("cvghj", frame)


            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        engine.stop()
        video.release()
        cv2.destroyAllWindows()


# ----------------------------------------------------weather App --------------------------------------------------------#
def weather():
        root = tk.Tk()
        root.minsize(width = 300, height = 300)
        root.maxsize(width = 300, height = 300)

        canvas1 = tk.Canvas(root, width = 300, height= 420, bg = 'black',
                            relief = 'raised')
        canvas1.pack()

        ## Create label
        label1 = tk.Label(root, text = "Image convertor", bg = 'white')
        label1.config(font = ('helvetica', 20))
        canvas1.create_window(150, 20, window = label1)

        ## Get image
        # ----------
        def getImage():
            global im1
            import_file_path = filedialog.askopenfilename()
            im1 = Image.open(import_file_path)

            messagebox.showinfo("Information", "Image is uploaded")

        browsImage = tk.Button(text = "Import Image", 
                                    command = getImage, 
                                    bg = 'grey',
                                    fg = 'white',
                                    font = ('helvetixa', 12, 'bold'),
                                    border = 0,
                                    activebackground = "green")
        canvas1.create_window(150, 60, window = browsImage)
        # -------------------------------------------------

        ## Convert jpg
        # ------------
        def convertJPG():
            global im1

            try:
                print("Image info")
                print(im1)
                export_file_path = filedialog.asksaveasfilename(defaultextension = '.jpg')
                im1.save(export_file_path)

                messagebox.showinfo("Information", "Converted into JPG")
            except NameError:
                messagebox.showwarning("Warning", "Import image first")

        jpg_button = tk.Button(text = "Convert to JPG", 
                                command = convertJPG,
                                bg = 'grey',
                                fg = 'white',
                                font = ('helvetica', 12, 'bold'),
                                border = 0)
        canvas1.create_window(150, 100, window = jpg_button)
        # --------------------------------------------------

        ## Conert to jpeg
        # ---------------
        def convertJPEG():
            global im1
            try:
                print("Image info")
                print(im1)
                export_file_path = filedialog.asksaveasfilename(defaultextension = '.jpeg')
                im1.save(export_file_path)

                messagebox.showinfo("Information", "Converted into JPEG")
            except NameError:
                messagebox.showwarning("Warning", "Import image first")

        jpeg_button = tk.Button(text = "Convert to JPEG", 
                                command = convertJPEG,
                                bg = 'grey',
                                fg = 'white',
                                font = ('helvetica', 12, 'bold'),
                                border = 0)
        canvas1.create_window(150, 140, window = jpeg_button)
        # ---------------------------------------------------

        ## Convert to png
        # ---------------
        def convertPNG():
            global im1
            try:
                print("Image info")
                print(im1)
                export_file_path = filedialog.asksaveasfilename(defaultextension = '.png')
                im1.save(export_file_path)

                messagebox.showinfo("Information", "Converted into PNG")
            except NameError:
                messagebox.showwarning("Warning", "Import image first")

        png_button = tk.Button(text = "Convert to PNG", 
                                command = convertPNG,
                                bg = 'grey',
                                fg = 'white',
                                font = ('helvetica', 12, 'bold'),
                                border = 0)
        canvas1.create_window(150, 180, window = png_button)
        # --------------------------------------------------



        ## Convert gif
        # ------------
        def convertGIF():
            global im1
            try:
                print("Image info")
                print(im1)
                export_file_path = filedialog.asksaveasfilename(defaultextension = '.gif')
                im1.save(export_file_path)

                messagebox.showinfo("Information", "Converted into GIF")
            except:
                messagebox.showwarning("Warning", "Import image first")

        gif_button = tk.Button(text = "Convert to GIF", 
                                command = convertGIF,
                                bg = 'grey',
                                fg = 'white',
                                font = ('helvetica', 12, 'bold'),
                                border = 0)
        canvas1.create_window(150, 220, window = gif_button)



        root.mainloop()






# ----------------------------------------------------WIFI App -----------------------------------------------------#
def wifi():
        import subprocess
        data = (
            subprocess.check_output(["netsh", "wlan", "show", "profiles"])
            .decode("utf-8")
            .split("\n")
        )
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = (
                subprocess
                .check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
                .decode("utf-8")
                .split("\n")
            )
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print("{:<30}|  {:<}".format(i, ""))



# ----------------------------------------------------Home Page UI ----------------------------------------------------#

window = Tk()
window.title("UTILITY ")
window.configure()
photo = tk.PhotoImage(
    file=r"Background.png")
background_label = tk.Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
w = photo.width()
h = photo.height()
window.geometry('%dx%d+0+0' % (w, h))

# Creating the display label
label = Label(text=" UTILITY  ",font=("Monetarist", 50, "bold"))
label.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

# Creating all the images for logos
youtube_buttone_logo = PhotoImage(file="images/youtube_button.png")
motion_button = PhotoImage(file="images/motion_button.png")
weather_button = PhotoImage(file="images/weather_button.png")
ocr_button = PhotoImage(file="images/ocr_button.png")

# Yes and No button images
yes_img = PhotoImage(file="images/yes_button.png")
no_img = PhotoImage(file="images/no_button.png")

# Creating the buttons
YT_img = PhotoImage(file="images/youtube_button.png")
YT_button = Button(image=YT_img, highlightbackground="black", command=Downloader)
YT_button.grid(row=3, column=0)

motion_img = PhotoImage(file="images/motion_button.png")
motion_button = Button(image=motion_img, highlightbackground="black", command=motion)
motion_button.grid(row=3, column=2)

temp_img = PhotoImage(file="images/weather_button.png")
temp_button = Button(image=temp_img, highlightbackground="black", command=weather)
temp_button.grid(row=10, column=0)

voltage_img = PhotoImage(file="images/ocr_button.png")
voltage_button = Button(image=voltage_img, highlightbackground="black", command=wifi)
voltage_button.grid(row=10, column=2)


window.mainloop()
