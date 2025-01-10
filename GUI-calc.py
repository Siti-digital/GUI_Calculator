import tkinter
from tkinter import*

cal=Tk()
cal.title("Calculator")

label1=Label(cal,text='KK-69 Instruments',height=2,font=('algerian',12)).grid(row=1,column=1,columnspan=2)
label3=Label(cal,text=' Input :- ',font=('algerian',12)).grid(row=3,column=0)
entry1=Entry(cal,font=('arial',20,'bold'),bd=15,insertwidth=4,width=22,bg="white",justify='right') 
entry1.grid(row=4,rowspan=3,pady=5,ipady=10,columnspan=4)
b=Label(cal,font=('arial',20,'bold'),text='                                     ',width=22,bg="white",justify='right')
b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)
label4=Label(cal,text=' Output :- ',font=('algerian',12)).grid(row=7,column=0,pady=6)
eq2=""

def eq2show():
    global eq2
    b=Label(cal,font=('arial',20,'bold'),text=eq2,width=22,bg="white",justify='right')
    b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)

def btn7():
    global eq2
    eq2=eq2+'7'
    eq2show()
def btn8():
    global eq2
    eq2=eq2+'8'   
    eq2show()
def btn9():
    global eq2
    eq2=eq2+'9'   
    eq2show()
def btn1():
    global eq2
    eq2=eq2+'1'   
    eq2show()
def btn0():
    global eq2
    eq2=eq2+'0'   
    eq2show()
def btn3():
    global eq2
    eq2=eq2+'3'   
    eq2show()
def btn4():
    global eq2
    eq2=eq2+'4'   
    eq2show()
def btn5():
    global eq2
    eq2=eq2+'5'   
    eq2show()
def btn6():
    global eq2
    eq2=eq2+'6'   
    eq2show()
def btn2():
    global eq2
    eq2=eq2+'2'   
    eq2show()
def btnadd():
    global eq2
    eq2=eq2+'+'   
    eq2show()
def btnsub():
    global eq2
    eq2=eq2+'-'   
    eq2show()
def btnmul():
    global eq2
    eq2=eq2+'*'   
    eq2show()
def btndiv():
    global eq2
    eq2=eq2+'/'   
    eq2show()
def btndot():
    global eq2
    eq2=eq2+'.'   
    eq2show()
def calc_equal():
    global eq1,eq2
    eq1=entry1.get()
    if eq1=="":
        if '/0' in eq2:
            b=Label(cal,font=('arial',20,'bold'),text="Cannot divide by 0",width=22,bg="white",justify='right')
            b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)
        else:
            equal1=eval(eq2)
            b=Label(cal,font=('arial',20,'bold'),text=equal1,width=22,bg="white",justify='right')
            b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)   
    else: 
        if '/0' in eq1:
            b=Label(cal,font=('arial',20,'bold'),text="Cannot divide by 0",width=22,bg="white",justify='right')
            b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)
        else:
            equal1=eval(eq1)
            b=Label(cal,font=('arial',20,'bold'),text=equal1,width=22,bg="white",justify='right')
            b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)
def clearall():
    global eq1,eq2
    eq1,eq2="",""
    entry1.delete(0,END)
    #entry1=Entry(cal,font=('arial',20,'bold'),bd=15,insertwidth=4,width=22,bg="white",justify='right') 
    #entry1.grid(row=4,rowspan=3,pady=5,ipady=10,columnspan=4)
    b=Label(cal,font=('arial',20,'bold'),text='                                     ',width=22,bg="white",justify='right')
    b.grid(row=8,rowspan=3,pady=5,ipady=10,columnspan=4,column=0)

#numerical buttons
btn7=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="7",bg="yellow",command=btn7).grid(row=13,pady=5,column=0)
btn8=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="8",bg="blue",command=btn8).grid(row=13,pady=5,column=1)
btn9=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="9",bg="yellow",command=btn9).grid(row=13,pady=5,column=2)
btn4=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="4",bg="lightgreen",command=btn4).grid(row=14,pady=5,column=0)
btn5=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="5",bg="red",command=btn5).grid(row=14,pady=5,column=1)
btn6=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="6",bg="lightgreen",command=btn6).grid(row=14,pady=5,column=2)
btn1=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="1",bg="yellow",command=btn1).grid(row=15,pady=5,column=0)
btn2=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="2",bg="blue",command=btn2).grid(row=15,pady=5,column=1)
btn3=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="3",bg="yellow",command=btn3).grid(row=15,pady=5,column=2)
btn0=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="0",bg="red",command=btn0).grid(row=16,pady=5,column=0)
btnpoint=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text=".",bg="yellow",command=btndot).grid(row=16,pady=5,column=1)

# mathematical operation buttons
Add=Button(cal,padx=16,pady=34,bd=8, fg="black",font=('arial',20,'bold'),text="+",bg="lightgreen",command=btnadd).grid(row=15,column=3,rowspan=2)
Sub=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="-",bg="lightgreen",command=btnsub).grid(row=13,column=3)
mul=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="x",bg="red",command=btnmul).grid(row=14,column=3)
div=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="፥",bg="blue",command=btndiv).grid(row=16,column=2)
equal=Button(cal,padx=48,bd=8, fg="black",font=('arial',20,'bold'),text="=",bg="red",command=calc_equal).grid(row=17,column=2,columnspan=2,pady=4)
clear_all=Button(cal,padx=48,bd=8, fg="black",font=('arial',16,'bold'),text="AC",bg="blue",command=clearall).grid(row=17,column=0,columnspan=2,pady=5)

cal.geometry("363x630")
cal.resizable(False,False)
cal.mainloop()
