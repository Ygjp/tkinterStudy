import tkinter as tk
window=tk.Tk()
window.title("demo6")
window.geometry("600x300")
var=tk.StringVar()
var.set('empty')
l=tk.Label(window,width=30,bg='green',textvariable=var)
l.pack()
def print_selection():
    if var1.get()==1 and var2.get()==1:
        var.set('I love both')
    elif var1.get()==1 and var2.get()==0:
        var.set('I love only Python')
    elif var1.get()==0 and var2.get()==1:
        var.set('I love only C++')
    else:
        var.set('I do not love either')
# 定义整数类型的变量
var1=tk.IntVar()
var2=tk.IntVar()
# variable与var绑定，选中时variable为1，->var1为1，没选中时同理
c1=tk.Checkbutton(window,variable=var1,onvalue=1,offvalue=0,text='Python',command=print_selection)
c1.pack()
c2=tk.Checkbutton(window,variable=var2,onvalue=1,offvalue=0,text='C++',command=print_selection)
c2.pack()
window.mainloop()