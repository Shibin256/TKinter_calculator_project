import tkinter
from tkinter import *
import tkinter.font as font
oldvalue = None
newvalue = None
window=Tk()
window.title("CALCULATOR")
window.geometry("400x500")


t=tkinter.Entry(window,width=20,font=("",25,""))
t.place(x=30,y=0)
t.pack()









def nine():
    s = t.get()
    if (s == "x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "9")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue + "9")
def eight():
    s = t.get()
    if (s == "x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "8")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue + "8")
def seven():
    s = t.get()
    if (s == "x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "7")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue + "7")





def six():
    s = t.get()
    if (s == "x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "6")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue + "6")
def five():
    s=t.get()
    if(s=="x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "5")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue+"5")

def four():
    s=t.get()
    if(s=="x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "4")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue+"4")






def three():
    s = t.get()
    if (s == "x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "3")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue + "3")
def two():
    s = t.get()
    if (s == "x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "2")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue + "2")

def one():
    s = t.get()
    if (s=="x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "1")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue + "1")






def zero():
    s=t.get()
    if(s=="x" or s=="+" or s=="-" or s=="/" or s=="%"):
        t.delete(0, "end")
        t.insert(0, "0")
    else:
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, oldvalue+"0")
def dot():
    oldvalue = t.get()
    t.delete(0, "end")
    t.insert(0, oldvalue+".")


def clear():
    t.delete(0,"end")
    t.insert(0,"")
    global oldvalue
    oldvalue=None







def plus():
    global operatorvalue
    operatorvalue = t.get()
    if (
            operatorvalue == "x" or operatorvalue == "+" or operatorvalue == "-" or operatorvalue == "/" or operatorvalue == "%"):
        t.delete(0, "end")
        t.insert(0, "+")
        global check
        check = 1
    else:
        global oldvalue
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, "+")
        check = 1




def minus():
    global operatorvalue
    operatorvalue = t.get()
    if (
            operatorvalue == "x" or operatorvalue == "+" or operatorvalue == "-" or operatorvalue == "/" or operatorvalue == "%"):
        t.delete(0, "end")
        t.insert(0, "-")
        global check
        check = 2
    else:
        global oldvalue
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, "-")
        check = 2


def divide():
    global operatorvalue
    operatorvalue = t.get()
    if (
            operatorvalue == "x" or operatorvalue == "+" or operatorvalue == "-" or operatorvalue == "/" or operatorvalue == "%"):
        t.delete(0, "end")
        t.insert(0, "/")
        global check
        check = 3
    else:
        global oldvalue
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, "/")
        check = 3


def multiply():
    global operatorvalue
    operatorvalue=t.get()
    if(operatorvalue=="x" or operatorvalue=="+" or operatorvalue=="-" or operatorvalue=="/" or operatorvalue=="%"):
        t.delete(0, "end")
        t.insert(0, "x")
        global check
        check=4
    else:
        global oldvalue
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, "x")
        check = 4


def reminder():
    global operatorvalue
    operatorvalue = t.get()
    if (operatorvalue == "x" or operatorvalue == "+" or operatorvalue == "-" or operatorvalue == "/" or operatorvalue == "%"):
        t.delete(0, "end")
        t.insert(0, "%")
        global check
        check = 5
    else:
        global oldvalue
        oldvalue = t.get()
        t.delete(0, "end")
        t.insert(0, "%")
        check = 5


def pi():
    global operatorvalue
    operatorvalue = t.get()
    if (operatorvalue == "x" or operatorvalue == "+" or operatorvalue == "-" or operatorvalue == "/" or operatorvalue == "%"):
        global oldvalue
        result=float(oldvalue)*3.141592
        t.delete(0, "end")
        t.insert(0, result)
    else:
        oldvalue = t.get()
        result = float(oldvalue) * 3.141592
        t.delete(0, "end")
        t.insert(0, result)





def equals():
    if(oldvalue==None):
        t.delete(0, "end")
        t.insert(0, "")

    else:
        if(check==1):
            newvalue = t.get()
            result = float(oldvalue) + float(newvalue)
            t.delete(0, "end")
            t.insert(0, result)


        elif (check == 2):
            newvalue = t.get()
            result = float(oldvalue) - float(newvalue)
            t.delete(0, "end")
            t.insert(0, result)

        elif (check == 3):
            try:
                newvalue = t.get()
                result = float(oldvalue) / float(newvalue)
                t.delete(0, "end")
                t.insert(0, result)
            except ZeroDivisionError:
                t.delete(0, "end")
                t.insert(0, "division not possible")

        elif(check==4):
            newvalue=t.get()
            result=float(oldvalue)*float(newvalue)
            t.delete(0,"end")
            t.insert(0,result)

        elif(check==5):
            newvalue = t.get()
            result = float(oldvalue) % float(newvalue)
            t.delete(0, "end")
            t.insert(0, result)




btn9 = Button(window, text='9',width=7,height=4,command=nine,bg="gray")
btn9.place(x=30, y=70)


btn8 = Button(window, text='8',width=7,height=4,command=eight,bg="gray")
btn8.place(x=90, y=70)

btn7 = Button(window, text='7',width=7,height=4,command=seven,bg="gray")
btn7.place(x=150, y=70)




btn6 = Button(window, text='6',width=7,height=4,command=six,bg="gray")
btn6.place(x=30, y=150)

btn5 = Button(window, text='5',width=7,height=4,command=five,bg="gray")
btn5.place(x=90, y=150)

btn4 = Button(window, text='4',width=7,height=4,command=four,bg="gray")
btn4.place(x=150, y=150)




btn3 = Button(window, text='3',width=7,height=4,command=three,bg="gray")
btn3.place(x=30, y=230)

btn2 = Button(window, text='2',width=7,height=4,command=two,bg="gray")
btn2.place(x=90, y=230)

btn1 = Button(window, text='1',width=7,height=4,command=one,bg="gray")
btn1.place(x=150, y=230)





dotbtn = Button(window, text='.',width=7,height=4,command=dot)
dotbtn.place(x=30, y=310)

btn0 = Button(window, text='0',width=7,height=4,command=zero,bg="gray")
btn0.place(x=90, y=310)

equalto = Button(window, text='=',width=7,height=4,command=equals)
equalto.place(x=150, y=310)








clearbtn = Button(window, text='clear',width=15,height=4,bg="orange",command=clear)
clearbtn.place(x=30, y=390)

reminderbtn = Button(window, text='%',width=7,height=4,command=reminder)
reminderbtn.place(x=150, y=390)


pibtn = Button(window, text='π',width=7,height=4,command=pi)
pibtn.place(x=210, y=390)









plusbtn = Button(window, text='+',width=7,height=4,command=plus)
plusbtn.place(x=210, y=70)

minusbtn = Button(window, text='-',width=7,height=4,command=minus)
minusbtn.place(x=210, y=150)

multibtn = Button(window, text='x',width=7,height=4,command=multiply)
multibtn.place(x=210, y=230)


divisionbtn = Button(window, text='/',width=7,height=4,command=divide)
divisionbtn.place(x=210, y=310)



window.mainloop()


