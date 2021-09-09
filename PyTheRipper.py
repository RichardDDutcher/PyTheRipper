#Imports
import PySimpleGUI as sg
import tk
import os.path

#Global Variables
frame = frame(self, borderwidth=10)
frame.pack()
title = "PyTheRipper"
layout = [[sg.Text("Welcome To PyTheRipper")],[,[sg.Button(Text="Start")],[sg.Button(Test="Cancel")]

#PytheRipper GUI
sg.Window(title, layout, margins=(100, 50)).read()

while True:
    event, values = Window.read()
    
    if event == "Start":
        print("Hello World")
