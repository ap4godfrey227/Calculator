# Calculator
import Tkinter as tk
import tkMessageBox as messagebox
import math

# Global variables
win = tk.Tk()           # our main window

#Set up the main window
win.title('CALCULATOR')

    
#creat containers for my controls
field = tk.Frame(win)
controls = tk.Frame(win)

#add the calculator buttons
zero = tk.Button(text="0")
one = tk.Button(text="1")
two = tk.Button(text="2")
three = tk.Button(text="3")
four = tk.Button(text="4")
five = tk.Button(text="5")
six = tk.Button(text="6")
seven = tk.Button(text="7")
eight = tk.Button(text="8")
nine = tk.Button(text="9")
add = tk.Button(text="+")
subtract = tk.Button(text="-")
multiply = tk.Button(text="X")
divide = tk.Button(text="/")
equal = tk.Button(text="=")
decimal = tk.Button(text=".")
negative = tk.Button(text="(-)")
clear = tk.Button(text="C")
backspace = tk.Button(text="<-")
fun = tk.Button(text="FUN")

equation = tk.StringVar()


#placement of buttons
zero.grid(row=5, column=1, ipadx=10, ipady=10)
one.grid(row=4, column=1, ipadx=10, ipady=10)
two.grid(row=4, column=2, ipadx=10, ipady=10)
three.grid(row=4, column=3, ipadx=10, ipady=10)
four.grid(row=3, column=1, ipadx=10, ipady=10)
five.grid(row=3, column=2, ipadx=10, ipady=10)
six.grid(row=3, column=3, ipadx=10, ipady=10)
seven.grid(row=2, column=1, ipadx=10, ipady=10)
eight.grid(row=2, column=2, ipadx=10, ipady=10)
nine.grid(row=2, column=3, ipadx=10, ipady=10)
add.grid(row=4, column=4, ipadx=10, ipady=10)
subtract.grid(row=3, column=4, ipadx=10, ipady=10)
multiply.grid(row=2, column=4, ipadx=10, ipady=10)
divide.grid(row=1, column=4, ipadx=10, ipady=10)
equal.grid(row=5, column=4, ipadx=10, ipady=10)
decimal.grid(row=5, column=2, ipadx=10, ipady=10)
negative.grid(row=5, column=3, ipadx=7, ipady=10)
clear.grid(row=1, column=2, ipadx=10, ipady=10)
backspace.grid(row=1, column=3, ipadx=7, ipady=10)
fun.grid(row=1, column=1, ipadx=3, ipady=10)


v = tk.StringVar()
expression_field = tk.Entry(win, textvariable=v)
expression_field.grid(row=1, column=0)

#create lists for the functions
global a
global s
global m
global d
a = []
s = []
m = []
d = []

def oneclk():
    v.set(v.get() + str(1))
def twoclk():
    v.set(v.get() + str(2))
def threeclk():
    v.set(v.get() + str(3))
def fourclk():
    v.set(v.get() + str(4))
def fiveclk():
    v.set(v.get() + str(5))
def sixclk():
    v.set(v.get() + str(6))
def sevenclk():
    v.set(v.get() + str(7))
def eightclk():
    v.set(v.get() + str(8))
def nineclk():
    v.set(v.get() + str(9))
def zeroclk():
    v.set(v.get() + str(0))
def backspaceclk():
    l = len(v.get())
    v.set(v.get()[0:a-1])
def clearclk():
    v.set(v.get()[0:0])

def addclk():
    global a
    a = []
    float(v.get())
    a.append(v.get())
    str(v.get())
    v.set(v.get()[0:0])
def subtractclk():
    global s
    s = []
    float(v.get())
    s.append(v.get())
    str(v.get())
    v.set(v.get()[0:0])
def multiplyclk():
    global m
    m = []
    float(v.get())
    m.append(v.get())
    str(v.get())
    v.set(v.get()[0:0])
def divideclk():
    global d
    d = []
    float(v.get())
    d.append(v.get())
    str(v.get())
    v.set(v.get()[0:0])
      
def equalclk():
    global a
    global s
    global m
    global d
    if a != []:
        float(v.get())
        a.append(v.get())
        str(v.get())
        v.set(v.get()[0:0])
        ans = 0
        for i in a:
            ans = ans + float(i)
        v.set(str(ans))
    if s != []:
        float(v.get())
        s.append(v.get())
        str(v.get())
        v.set(v.get()[0:0])
        ans = float(s[0])
        for i in s[1:]:
            ans = ans - float(i) 
        v.set(str(ans))
    if m != []:
        float(v.get())
        m.append(v.get())
        str(v.get())
        v.set(v.get()[0:0])
        ans = 1
        for i in m:
            ans = ans * float(i)
        v.set(str(ans))
    if d != []:
        float(v.get())
        d.append(v.get())
        str(v.get())
        v.set(v.get()[0:0])
        ans = float(d[0])
        for i in d[1:]:
            ans = ans / float(i)
        v.set(str(ans))
        
        
        
    
    
#Button commands
one['command'] = oneclk
two['command'] = twoclk
three['command'] = threeclk
four['command'] = fourclk
five['command'] = fiveclk
six['command'] = sixclk
seven['command'] = sevenclk
eight['command'] = eightclk
nine['command'] = nineclk
zero['command'] = zeroclk
backspace['command'] = backspaceclk
clear['command'] = clearclk
add['command'] = addclk
subtract['command'] = subtractclk
multiply['command'] = multiplyclk
divide['command'] = divideclk
equal['command'] = equalclk




# begin the event loop
win.mainloop()