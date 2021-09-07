#Imports
import PySimpleGUI as sg
import os.path

#Global Variables
title = "PyTheRipper"

layout = [[sg.Text("Welcome To PyTheRipper")][sg.Button("Start")][sg.Button("Shutdown")]]

#PytheRipper GUI
sg.Window(title, layout, margins=(100, 50)).read()

while True:
    event, values = Window.read()

    if event == "Start":
        print("Hello World")
