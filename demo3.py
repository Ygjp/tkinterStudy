import tkinter as tk
window=tk.Tk()
window.title("demo1")
window.geometry("600x300")
var1=tk.StringVar()
l=tk.Label(window,width=4,bg='yellow',textvariable=var1)
l.pack()
def print_selection():
    #获取选中的格子的内容
    value=lb.get(lb.curselection())
    var1.set(value)
b=tk.Button(window,text='print selection',width=12,height=3,command=print_selection)
b.pack()

var2=tk.StringVar()
var2.set((11,22,33,44))
# listvariable设置列表值
lb=tk.Listbox(window,listvariable=var2)
lb.pack()

list=[1,2,3,4]
for item in list:
    lb.insert(1,item)
# 插入（有0行）
lb.insert(1,'rrrr')
# 删除
lb.delete(1)
window.mainloop()