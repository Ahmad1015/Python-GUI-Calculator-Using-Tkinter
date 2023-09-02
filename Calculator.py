# Import the tkinter library for GUI
from tkinter import *
import re

# Create the main application window
root = Tk()
root.geometry("550x400")  # Set the initial window size

# Create labels for the calculator title and a note
Label(root, text="Calculator", font="Arial 12 bold", foreground='blue').grid(row=0, column=0)
Label(root, text="Note: Can not deal with negatives", font="Arial 9 bold", foreground='Red').grid(row=0, column=1)

# Create a label to display the calculator output
OutputScreen = Label(root, text="Screen", font="ar 10 bold")
OutputScreen.grid(row=2, column=0)

# Create a StringVar to hold the calculator input/output
Screen = StringVar()

# Create an Entry widget for user input
ScreenEntry = Entry(root, textvariable=Screen, width=39, font='ar 12 bold')
ScreenEntry.grid(row=2, column=1, pady=15)

# Initialize a flag for different calculator operations
Flag = 0

# Define a function to perform calculations
def Calculate():
    global Flag
    temp = Screen.get()
    Input = re.findall(r'\d+', temp)
    match Flag:
        case 1:
            var = 0
            for x in range(len(Input)):
                var = var + int(Input[x])
            var =  str(var)
            Screen.set(var)
        case 2:
            var = int(Input[0])
            for x in range(1, len(Input)):
                var = var - int(Input[x])
            var =  str(var)
            Screen.set(var)
        case 3:
            var = int(Input[0])
            for x in range(1, len(Input)):
                var = var * int(Input[x])
            var =  str(var)
            Screen.set(var)
        case 4:
            var = int(Input[0])
            for x in range(1, len(Input)):
                var = var / int(Input[x])
            var =  str(var)
            Screen.set(var)
        case 5:
            var = int(Input[0])
            for x in range(1, len(Input)):
                var = var % int(Input[x])
            var =  str(var)
            Screen.set(var)
        case 6:
            var = int(Input[0])
            for x in range(1, len(Input)):
                var = var // int(Input[x])
            var =  str(var)
            Screen.set(var)
        case other:
            print("Wrong input")
    shift_cursor()

# Define functions for various calculator operations
def Addition():
    global Flag
    Flag = 1
    temp = Screen.get()
    temp = temp + " + "
    Screen.set(temp)
    shift_cursor()

def Subtraction():
    global Flag
    Flag = 2
    temp = Screen.get()
    temp = temp + " - "
    Screen.set(temp)
    shift_cursor()

def Multiplication():
    global Flag
    Flag = 3
    temp = Screen.get()
    temp = temp + " * "
    Screen.set(temp)
    shift_cursor()

def Division():
    global Flag
    Flag = 4
    temp = Screen.get()
    temp = temp + " / "
    Screen.set(temp)
    shift_cursor()

# Define a function to shift the cursor in the input field
def shift_cursor(event=None):
    temp = Screen.get()
    position = ScreenEntry.index(INSERT)
    ScreenEntry.icursor(position + len(temp))

# Define functions for numbers and additional operations
def one():
    temp = Screen.get()
    temp = temp + " 1 "
    Screen.set(temp)
    shift_cursor()

def two():
    temp = Screen.get()
    temp = temp + " 2 "
    Screen.set(temp)
    shift_cursor()

def three():
    temp = Screen.get()
    temp = temp + " 3 "
    Screen.set(temp)
    shift_cursor()

def four():
    temp = Screen.get()
    temp = temp + " 4 "
    Screen.set(temp)
    shift_cursor()

def Five():
    temp = Screen.get()
    temp = temp + " 5 "
    Screen.set(temp)
    shift_cursor()

def Six():
    temp = Screen.get()
    temp = temp + " 6 "
    Screen.set(temp)
    shift_cursor()

def Seven():
    temp = Screen.get()
    temp = temp + " 7 "
    Screen.set(temp)
    shift_cursor()

def Eight():
    temp = Screen.get()
    temp = temp + " 8 "
    Screen.set(temp)
    shift_cursor()

def Nine():
    temp = Screen.get()
    temp = temp + " 9 "
    Screen.set(temp)
    shift_cursor()

def mod():
    global Flag
    Flag = 5
    temp = Screen.get()
    temp = temp + " % "
    Screen.set(temp)
    shift_cursor()

def clear():
    global Flag
    Flag = 6
    temp = ''
    Screen.set(temp)
    shift_cursor()

# Create buttons for calculator operations
Button(text="-", command=Subtraction, background='gray', foreground='blue', font='ar 20 bold').grid(row=9, column=1)
Button(text="+", command=Addition, background='gray', foreground='blue', font='ar 20 bold').grid(row=9, column=0)
Button(text="Clear", command=clear, background='gray', foreground='blue', font='ar 15 bold',height=1).grid(row=9, column=2)
Button(text="MOD", command=mod, background='gray', foreground='blue', font='ar 15 bold',height=1).grid(row=10, column=2)
Button(text="*", command=Multiplication, background='gray', foreground='blue', font='ar 20 bold').grid(row=10, column=1)
Button(text="/", command=Division, background='gray', foreground='blue', font='ar 20 bold').grid(row=10, column=0)

# Create buttons for numbers and the equals sign
Button(text="=", command=Calculate, background='gray', foreground='blue', font='ar 20 bold').grid(row=2, column=2)
Button(text="1", command=one, background='gray', foreground='blue', font='ar 20 bold').grid(row=21, column=0)
Button(text="2", command=two, background='gray', foreground='blue', font='ar 20 bold').grid(row=21, column=1)
Button(text="3", command=three, background='gray', foreground='blue', font='ar 20 bold').grid(row=21, column=2)
Button(text="4", command=four, background='gray', foreground='blue', font='ar 20 bold').grid(row=22, column=0)
Button(text="5", command=Five, background='gray', foreground='blue', font='ar 20 bold').grid(row=22, column=1)
Button(text="6", command=Six, background='gray', foreground='blue', font='ar 20 bold').grid(row=22, column=2)
Button(text="7", command=Seven, background='gray', foreground='blue', font='ar 20 bold').grid(row=23, column=0)
Button(text="8", command=Eight, background='gray', foreground='blue', font='ar 20 bold').grid(row=23, column=1)
Button(text="9", command=Nine, background='gray', foreground='blue', font='ar 20 bold').grid(row=23, column=2)

# Set focus to the input field
ScreenEntry.focus()

# Start the Tkinter main loop
root.mainloop()
