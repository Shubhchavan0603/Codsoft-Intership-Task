from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x275")
fond = ("Times New Roman", 30, "bold")

calculation = ""
def add_to_calculation(symbol):
    global calculation
    print(calculation)
    calculation+=str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,'end')
        text_result.insert(1.0,calculation)

    except:
        clear_field()
        text_result.insert(1.0,'Error')

def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

text_result = Text(root,height=2,width=20, font=("lucida 20 bold"))
text_result.grid(columnspan=5)

Button1 = Button(root,text='1', command=lambda: add_to_calculation(1),width=5,font=('arial 14'),bg="#00bfff")
Button1.grid(row=2,column=1)

Button2 = Button(root,text='2', command=lambda: add_to_calculation(2),width=5,font=('arial 14'),bg="#00bfff")
Button2.grid(row=2,column=2)

Button3 = Button(root,text='3', command=lambda: add_to_calculation(3),width=5,font=('arial 14'),bg="#00bfff")
Button3.grid(row=2,column=3)

Button4 = Button(root,text='4', command=lambda: add_to_calculation(4),width=5,font=('arial 14'),bg="#00bfff")
Button4.grid(row=3,column=1)

Button5 = Button(root,text='5', command=lambda: add_to_calculation(5),width=5,font=('arial 14'),bg="#00bfff")
Button5.grid(row=3,column=2)

Button6 = Button(root,text='6', command=lambda: add_to_calculation(6),width=5,font=('arial 14'),bg="#00bfff")
Button6.grid(row=3,column=3)

Button7 = Button(root,text='7', command=lambda: add_to_calculation(7),width=5,font=('arial 14'),bg="#00bfff")
Button7.grid(row=4,column=1)

Button8 = Button(root,text='8', command=lambda: add_to_calculation(8),width=5,font=('arial 14'),bg="#00bfff")
Button8.grid(row=4,column=2)

Button9 = Button(root,text='9', command=lambda: add_to_calculation(9),width=5,font=('arial 14'),bg="#00bfff")
Button9.grid(row=4,column=3)

Button0 = Button(root,text='0', command=lambda: add_to_calculation(0),width=5,font=('arial 14'),bg="#00bfff")
Button0.grid(row=5,column=2)

Button_plus = Button(root,text='+', command=lambda: add_to_calculation("+"),width=5,font=('arial 14'),bg="#00bfff")
Button_plus.grid(row=2,column=4)

Button_minus = Button(root,text='-', command=lambda: add_to_calculation("-"),width=5,font=('arial 14'),bg="#00bfff")
Button_minus.grid(row=3,column=4)

Button_mul = Button(root,text='*', command=lambda: add_to_calculation("*"),width=5,font=('arial 14'),bg="#00bfff")
Button_mul.grid(row=4,column=4)

Button_div = Button(root,text='/', command=lambda: add_to_calculation("/"),width=5,font=('arial 14'),bg="#00bfff")
Button_div.grid(row=5,column=4)

Button_open = Button(root,text='(', command=lambda: add_to_calculation("("),width=5,font=('arial 14'),bg="#00bfff")
Button_open.grid(row=5,column=1)

Button_close = Button(root,text=')', command=lambda: add_to_calculation(")"),width=5,font=('arial 14'),bg="#00bfff")
Button_close.grid(row=5,column=3)

Button_clear = Button(root,text='C', command=clear_field,width=12,font=('arial,14'),bg="#00bfff")
Button_clear.grid(row=6,column=1,columnspan=2)

Button_equal = Button(root,text='=', command=evaluate_calculation,width=12,font=('arial 14'),bg="#00bfff")
Button_equal.grid(row=6,column=3,columnspan=2)

root.mainloop()
