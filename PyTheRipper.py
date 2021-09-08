#Imports
import PySimpleGUI as sg
import tk
import os.path

#Global Variables
title = "PyTheRipper"
layout = [[sg.Text("Welcome To PyTheRipper")],[,[sg.Button(Text="Start")],[sg.Exit]]

#PytheRipper GUI
sg.Window(title, layout, margins=(100, 50)).read()

frame = frame(self, borderwidth=10)
frame.pack()

btn1 = Button(frame, text="Start")
btn1.pack(side=LEFT, padx=5)
btn2 = Button(frame, text="Shutdown")
btn2.pack(side=RIGHT, padx=5)


while True:
    event, values = Window.read()
    
    if event == "Start":
        print("Hello World")
