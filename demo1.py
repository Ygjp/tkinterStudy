import tkinter as tk
window=tk.Tk()
window.title("demo1")
window.geometry("600x300")
# 定义一个可变的字符变量
var=tk.StringVar()
# 设置字符变量的值
var.set("hit me")
# 字符变量用textvariable存储
l=tk.Label(textvariable=var,font=('Arial',12),width=12,height=3,bg='green')
l.pack()
on_hit=False
def hit_t():
    global on_hit
    if on_hit==False:
        var.set("hit me")
        on_hit=True
    else:
        var.set("me")
        on_hit=False
# 利用command来绑定点击事件，点击后执行后面的函数
b=tk.Button(window,text='hit me',width=12,height=3,command=hit_t)
# 组件记得加pack（布局），后期还有其他的布局方式
b.pack()
window.mainloop()