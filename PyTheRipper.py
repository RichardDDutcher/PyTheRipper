#Imports
import PySimpleGUI as sg
import os.path

#PytheRipper GUI
sg.Window(title=PyTheRipper, layout=[[sg.Text("Welcome To PyTheRipper"][sg.Button("Start")][]sg.Button("Shutdown")], margins=(100, 50)).read()

while True:
    event, values = window.read()
																			
		if event == "Start":
	
		if event == "Shutdown" OR event == sg.WIN_CLOSED:
			break
                 


#code check
print("Hello World")
