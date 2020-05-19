import os
import PySimpleGUIQt as sg
import re

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\ProgramData\Anaconda3\Lib\site-packages\PySide2\plugins\platforms'

sg.ChangeLookAndFeel('System Default')

dbSettings_input_keys=['_dbSettings__dbname__',
                       '_dbSettings__dbserver__',
                       '_dbSettings__dbschema__',
                       '_dbSettings__dbuser__',
                       '_dbSettings__dbpassword__']

menu_def = [
            ['&Settings', 
                ['---',
                 '&DbSettings::__dbSettings__menu__',
                 '---', 
                 '&BranchSettings::__branchSettings__menu__', 
                 '---',
                 '&WindowSettings::__windowSettings__menu__',
                 '---', 
                 '&Properties::__properties__menu__',
                 '---']
            ],
            ['&Tools', 
                ['---',
                 '&Compare', 
                 '---',
                 '&Upgrade',
                 '---',
                 '&GenerateSQL',
                 '---']
            ],
            ['&About...', 
                ['---',
                 '&Preferences',
                 '---',
                 'E&xit',
                 '---']
            ]
           ]  

# ----------- Create the 3 layouts this Window will display -----------

layout1 = [[sg.Text('%-17s%+3s' %("Database Name    ",":-"),size=(15,1),justification="left",text_color="green"), sg.Input(key='_dbSettings__dbname__')],
           [sg.Text('%-17s%+3s' %("Database Server  ",":-"),size=(15,1),justification="left",text_color="green"), sg.Input(key='_dbSettings__dbserver__')],
           [sg.Text('%-17s%+3s' %("Database Schema",":-"),size=(15,1),justification="left",text_color="green"), sg.Input(key='_dbSettings__dbschema__')],
           [sg.Text('%-17s%+3s' %("Database User",":-"),size=(15,1),justification="left",text_color="green"), sg.Input(key='_dbSettings__dbuser__')],
           [sg.Text('%-17s%+3s' %("Database Password",":-"),size=(15,1),justification="left",text_color="green"), sg.Input(key='_dbSettings__dbpassword__')],
           [sg.Button("Save", key="_dbSettings__dbsave__"),sg.Button("Reset", key="_dbSettings__dbreset__")]
           ]

layout2 = [[sg.Text('Source Branch   :-',size=(15,1),justification="left",text_color="green"), sg.Input(key='_branchSettings__sourceBranch__')],
           [sg.Text('Target Branch   :-',size=(15,1),justification="left",text_color="green"), sg.Input(key='_branchSettings__targetBranch__')],
           [sg.Text('SVN Path        :-',size=(15,1),justification="left",text_color="green"), sg.Input(key='_branchSettings__svnPath__')],
           [sg.Text(),sg.Text()],
           [sg.Text(),sg.Text()],
           [sg.Button("Save", key="_branchSettings__save__"),sg.Button("Reset", key="_branchSettings__reset__")]
           ]

column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1            ))],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]
          ] 
            
layout3 = [[sg.Text('Development in Progress. Watch this space for update.')]]

layout4 = [[sg.Text('Development in Progress. Watch this space for update.')]]
table_layout=[[sg.Table(sg.Text("Row1"))]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Menu(menu_def)],
          [sg.Frame("Database Settings",layout1,font=('Any 12','25','Bold','Italic'), title_color='blue',key="__dbSettings__menu__", visible=True,size=(400,200))],
          [sg.Frame("Branch Settings",layout2,key="__branchSettings__menu__", visible=False,size=(400,200))],
          [sg.Frame("Windows Settings",layout3,key="__windowSettings__menu__", visible=False,size=(400,200))],
          [sg.Frame("Properties Settings",layout4,key="__properties__menu__", visible=False,size=(400,200))],
          # [sg.Output(size=(450,200),pad=((10,10),(10,10)),text_color='red',background_color='yellow')],
          [sg.Frame("Table",table_layout)]
         ]
         


window = sg.Window('Agora Database Schema Tool', layout, size=(400,100),icon="C:\PARAG\PythonProgramms\PySimpleGUIProgramms\Flickr.ico",resizable=False,grab_anywhere=True)

visibleColumnKey =  "__dbSettings__menu__" # The currently visible layout

while True:
    event, values = window.read()
    # print("Events = %s" % event)
    # print("Values = %s" % values)
    if event in (None, 'Exit'):
        break
    match = re.search(r"^(.*)::(.*)$",event)
    if event == "_dbSettings__dbreset__":
        for key in dbSettings_input_keys:
            window[key]('')
    if match:
        key=match.group(2)
        window[visibleColumnKey].update(visible=False)
        window[key].update(visible=True)
        visibleColumnKey=key
window.close()


