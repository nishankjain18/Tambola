import wx
import wx.grid
import random

#creating app
app = wx.App()
#creating frame
frame = wx.Frame(parent = None, title = "Tambola")
#creating panel in frame
panel = wx.Panel(frame)
#adjusting size to panel and frame
sizer = wx.GridBagSizer()
#Creating Grid
mygrid = wx.grid.Grid(frame, 0)
#avoid duplicate nos
number_set = set()


def press_button(event):
    #pressing random no from 1-90
    random_int = random.randint(1, 90)
    #if no is already shown then it will show diff no
    while random_int in number_set:
        random_int = random.randint(1, 90)
    #adding 1-90 in set
    number_set.add(random_int)
    set_input_label(random_int)

def create_grid(mygrid):
    #creating my grid
    mygrid.CreateGrid(9, 10)      
    count = 0
    #iterating row
    for row in range(9):
        #iterating col
        for col in range(10):
            #increase by +1
            count = count + 1
            #setting value in grid cell
            mygrid.SetCellValue(row, col,"%d" % (count))

def set_input_label(random_int):
    result.SetLabel(str(random_int))
    #divmod is a function which shows quotient,remainder
    row,column = divmod(random_int, 10)
    if column == 0:
        row = row -1
        column = 10
    print(row,column - 1)
    #setting background color
    mygrid.SetCellBackgroundColour(row,column -1, wx.Colour(0, 170, 0))
    #refreshing grid to set colour
    mygrid.Refresh()  
        
#input button,label
input_label = wx.StaticText(panel, label = "Current Number: ")
result = wx.StaticText(panel, label = " ")
button = wx.Button(panel, label = "Generate")
button.Bind(wx.EVT_BUTTON, press_button)
create_grid(mygrid)


sizer.Add(mygrid, (3,4))
sizer.Add(input_label, (1,2))
sizer.Add(button, (3,2))
sizer.Add(result, (1,3))

#connecting panel program to sizer program
panel.SetSizerAndFit(sizer)
frame.SetSizerAndFit(sizer)


frame.Show()
app.MainLoop()
