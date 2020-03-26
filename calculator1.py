# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:28:19 2020

@author: user
"""

import tkinter
from tkinter import*
root=tkinter.Tk()
root.geometry("350*500+600+200")
root.resizable(0,0)
root.title("Calculator")
data=StringVar()
operator=""
def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     data.set(operator)

def equlbut(): 
    try:
        global operator
        res=str(eval(operator))
        data.set(res)
        operator=str(res)
    except:
        data.set("ヽ(ಠ_ಠ)ノErrorヽ(ಠ_ಠ)ノ")
        operator=''
     
     
def clrbut():
    global operator
    operator=''
    data.set('')
     

# the label that shows the result

lbl = Label(
    root,
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#393e46",
)
lbl.pack(expand = True, fill = "both")



btnrow1=Frame(root)
btnrow1.pack(expand=True,fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

btnrow5 = Frame(root)
btnrow5.pack(expand = True, fill = "both")
#====================================================
btn7=Button(
        btnrow1,
        text = "7",
        font = ("Verdana", 20),  
        command=lambda:clickbut(7),
        )
btn7.pack(side=LEFT,expand=True,fill="both")

btn8=Button(
        btnrow1,
        text = "8",
        font = ("Verdana", 20),
        command=lambda:clickbut(8),
        )
btn8.pack(side=LEFT,expand=True,fill="both")

btn9=Button(
        btnrow1,
        text = "9",
        font = ("Verdana", 20),
        command=lambda:clickbut(9),
        )
btn9.pack(side=LEFT,expand=True,fill="both")

btn_div=Button(
        btnrow1,
        text = "/",
        font = ("Verdana", 20),
        command=lambda:clickbut("/"),
        )
btn_div.pack(side=LEFT,expand=True,fill="both")

#========================================================================
btn4=Button(
        btnrow2,
        text = "4",
        font = ("Verdana", 20),
        command=lambda:clickbut(4),
        )
btn4.pack(side=LEFT,expand=True,fill="both")

btn5=Button(
        btnrow2,
        text = "5",
        font = ("Verdana", 20),
        command=lambda:clickbut(5),
        )
btn5.pack(side=LEFT,expand=True,fill="both")

btn6=Button(
        btnrow2,
        text = "6",
        font = ("Verdana", 20),
        command=lambda:clickbut(6),
        )
btn6.pack(side=LEFT,expand=True,fill="both")

btn_mul=Button(
        btnrow2,
        text = "*",
        font = ("Verdana", 18),
        command=lambda:clickbut("*"),
        )
btn_mul.pack(side=LEFT,expand=True,fill="both")

#========================================================================
btn1=Button(
        btnrow3,
        text = "1",
        font = ("Verdana", 20),
        command=lambda:clickbut(1),
        )
btn1.pack(side=LEFT,expand=True,fill="both")

btn2=Button(
        btnrow3,
        text = "2",
        font = ("Verdana", 20),
        command=lambda:clickbut(2),
        )
btn2.pack(side=LEFT,expand=True,fill="both")

btn3=Button(
        btnrow3,
        text = "3",
        font = ("Verdana", 20),
        command=lambda:clickbut(3),
        )
btn3.pack(side=LEFT,expand=True,fill="both")

btn_sub=Button(
        btnrow3,
        text = "-",
        font = ("Verdana", 20),
        command=lambda:clickbut("-"),
        )
btn_sub.pack(side=LEFT,expand=True,fill="both")
#========================================================================
btn_ce=Button(
        btnrow4,
        text = "CE",
        font = ("Verdana", 14),
        command=clrbut
        )
btn_ce.pack(side=LEFT,expand=True,fill="both")

btn0=Button(
       btnrow4,
        text = "0",
        font = ("Verdana", 22),
        command=lambda:clickbut(0),
        )
btn0.pack(side=LEFT,expand=True,fill="both")

btn_dot=Button(
        btnrow4,
        text = ".",
        font = ("Verdana",25),
        command=lambda:clickbut("."),
        )
btn_dot.pack(side=LEFT,expand=True,fill="both")
btn_plus=Button(
        btnrow4,
        text = "+",
        font = ("Verdana", 17),
        command=lambda:clickbut("+"),
        )
btn_plus.pack(side=LEFT,expand=True,fill="both")
#=======================================================
btn_equal=Button(
        btnrow5,
        text = "=",
        font = ("Verdana", 20),
        command=equlbut
        )
btn_equal.pack(expand=True,fill="both")



root.mainloop()

