**Python GUI – tkinter**
Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter outputs the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.
To create a tkinter:

Importing the module – tkinter
Create the main window (container)
Add any number of widgets to the main window
Apply the event Trigger on the widgets.
Importing tkinter is same as importing any other module in the python code. Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x is ‘tkinter’.

**import tkinter**
There are two main methods used you the user need to remember while creating the Python application with GUI.

**Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1):** To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, you can change the className to the desired one. The basic code used to create the main window of the application is:
m=tkinter.Tk() where m is the name of the main window object
mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
m.mainloop()
import tkinter 
m = tkinter.Tk() 
''' 
widgets are added here 
'''
m.mainloop() 
tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager classes class.

**pack()** method:It organizes the widgets in blocks before placing in the parent widget.
**grid()** method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
**place()** method:It organizes the widgets by placing them on specific positions directed by the programmer.
There are a number of widgets which you can put in your tkinter application. 

Tkinter Framework explained below videos
Here is the playlist.
\n
https://www.youtube.com/watch?v=MLfjAHEUww4&list=PLyjE_CyqGikr_Dao6QEmzc8JfOhLqgv2v

Thank You
Happy coding :)
