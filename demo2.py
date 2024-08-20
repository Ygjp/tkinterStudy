import tkinter as tk
window=tk.Tk()
window.geometry("400x400")
window.title("demo2")
# Entry代表输入框，里面的show为输入的数据的显示样式，None就是普通的，*等等就是输入后显示的
e=tk.Entry(window,show='*')
e.pack()
def insert_point():
    # 获取输入框的数据
    var=e.get()
    # 在文本框中插入数据，插入位置为鼠标指针的所在位置
    t.insert('insert',var)
    # t.insert(1.1,var)         则在第一行（无0行）的第一列（有0列）插入数据
def insert_end():
    var=e.get()
    # 在文本框中插入数据，插入位置为文本末尾
    t.insert('end',var)
bt1=tk.Button(window,text='insert point',width=13,height=3,command=insert_point)
bt1.pack()

bt2=tk.Button(window,text='insert end',width=13,height=3,command=insert_end)
bt2.pack()
# 定义一个文本框，用于显示数据
t=tk.Text(window,height=2)
t.pack()
window.mainloop()
