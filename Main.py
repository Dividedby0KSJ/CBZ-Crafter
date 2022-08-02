from tkinter import UNDERLINE
import PySimpleGUI as sg

sg.theme('DarkGray8') # This looks the best i think...


# Layout of the window
Start_Up_Layout = [

    [sg.Text("Wellcum to DividedBy0's CBZ-Crafter\n", font=("arial", 25))],
    [sg.Text('With this tool you can make CBZ (And other Comic book formats) with ease!\n')],
    [sg.Text('First you need a folder containing All the pages numbered correctly.\n')],
    [sg.Text('It is', pad=0), sg.Text('recommended', font=("arial", 16, "underline"), pad=0), sg.Text('to number the pages like so:', pad=0), sg.Text('[ Page 001 ] [ P001 ] [ 001 ]', text_color='Yellow')],
    [sg.Text('  However, naming it like this'), sg.Text('[ page 1 ] [ 1 ]', text_color='Yellow', pad=0), sg.Text('Should be fine as well.')], 
    [sg.Button('Continue', size=(15,15), pad=50, font=("arial", 20, "underline"), button_color='Green', mouseover_colors='Gray')]    
    ]



# Create the Window
Start_Up_Window = sg.Window('Window Title', Start_Up_Layout,  size=(800,450), font=("arial", 16), element_justification='center')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = Start_Up_Window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Continue':
        print('Next Page')

Start_Up_Window.close()