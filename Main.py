from tkinter import UNDERLINE
import PySimpleGUI as sg

sg.theme('DarkGray8') # This looks the best i think...


Heading_Font = "Times New Roman", 30

# I dont know why im doing it this way...

Body_Font = "arial"
Body_Size = str(14)
Body_Text = Body_Font + " " + Body_Size

Body_Text_Underline = Body_Text + " underline"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Layout of the window
Start_Up_Layout = [

    [sg.Text("Wellcum to DividedBy0's CBZ-Crafter\n", font=(Heading_Font))],
    [sg.Text('With this tool you can make CBZ (And other Comic book formats) with ease!\n')],
    [sg.Text('First you need a folder containing All the pages numbered correctly.\n')],
    [sg.Text('It is', pad=0), sg.Text('recommended', font=(Body_Text_Underline), pad=0), sg.Text('to number the pages like so:', pad=0), sg.Text('[ Page 001 ] [ P001 ] [ 001 ]', text_color='Yellow')],
    [sg.Text('  However, naming it like this'), sg.Text('[ page 1 ] [ 1 ]', text_color='Yellow', pad=0), sg.Text('Should be fine as well.')], 
    [sg.Button('Continue', size=(15,15), pad=50, font=("arial", 20, "underline"), button_color='Green', mouseover_colors='Gray')]    
    ]


# Create the Window
Start_Up_Window = sg.Window('Window Title', Start_Up_Layout,  size=(800,450), font=(Body_Text), element_justification='center')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = Start_Up_Window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        exit()
    if event == 'Continue':
        break

Start_Up_Window.close()


# Folder select



Folder_Browser_Layout = [
    [sg.Text("Please select a folder that contains the comic page's.")],
    [sg.Input(key="CBZ_Folder", default_text="C:/Example Folder/Volume 1"), sg.FolderBrowse('Browse')]
]

[sg.Text(':'), sg.Input(key="Metadata_", default_text="")],

Folder_Metadata_Layout = [
    [sg.Text('Title of the book:'), sg.Input(key="Metadata_Title", default_text="Comic Name")],
    [sg.Text('Summary for the book:'), sg.Input(key="Metadata_Summary", default_text="This is a cool comic")],
    [sg.Text(':'), sg.Input(key="Metadata_", default_text="")],
]


Folder_Window_Layout = [
    [sg.Text('Folder', font=(Heading_Font))],
    [sg.Column(Folder_Browser_Layout)],

    [sg.Text("\n", font=("arial 1"))], # <---- This just adds a little space between the 2 headings

    [sg.Text('Metadata', font=(Heading_Font))],
    [sg.Text('Do you want to use metadata? (Default "Yes")'), sg.Checkbox("Enable Metadata", default=True, key="CBZ_EnableMetadata", enable_events=True)], #Ask the user if they use metadata
    [sg.Column(Folder_Metadata_Layout, scrollable=True, vertical_scroll_only=True, key="CBZ_Metadata_Input_Layout", visible=True)],
    [sg.Button('Continue', pad=25, font=("arial", 20), button_color='Green', mouseover_colors='Gray', key="Next_Button")]    
]

Folder_Browser_And_MetaData_Window = sg.Window('CBZ-Crafter', Folder_Window_Layout, size=(700,600), font=(Body_Text), element_justification='center')

while True:
    event, values = Folder_Browser_And_MetaData_Window.read()
    if event == sg.WIN_CLOSED:
        exit()
    
    # Hide and shows the metadata Section
    elif values["CBZ_EnableMetadata"] == True:
        Folder_Browser_And_MetaData_Window.Element('CBZ_Metadata_Input_Layout').Update(visible=True)
    elif values["CBZ_EnableMetadata"] == False:
        Folder_Browser_And_MetaData_Window.Element('CBZ_Metadata_Input_Layout').Update(visible=False)

    if event == "Next_Button":
        if values["CBZ_EnableMetadata"] == True:
            Metadata_Enabled = True
            print("MetaData was true")
            # 
        else:
            Metadata_Enabled = False
        
        FolderDir = values["CBZ_Folder"]
        print(FolderDir)

        break
        