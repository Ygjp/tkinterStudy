import tkinter as tk
window=tk.Tk()
window.title("demo5")
window.geometry("600x300")
var=tk.StringVar()
var.set('empty')
l=tk.Label(window,width=30,bg='green',textvariable=var)
l.pack()
def print_selection(v):
    var.set('you have selection'+v)
# showvalue----------------------------------------为是否在头上显示数值，0（False）为不显示，1（True）为显示
# label--------------------------------------------为在开头显示的名字，（标签/名字）
# from_---------------------------------------------为开始值（闭区间）
# to-----------------------------------------------为结束值（闭区间）
# orient-------------------------------------------为显示的样式，默认（不写）为竖着的，tk.HORIZONTAL为横向显示
# length-------------------------------------------为长度，单位是px（像素）
# tickinterval-------------------------------------为跨多少个单位显示一次长度（刻度），在这里显示的刻度为5,7,9,11
# resolution---------------------------------------为精确度，0.01为精确到小数点后两位，0.1为一位
# command------------------------------------------这里的command绑定的函数有一个参数，这个参数是滑动的地方的刻度值
s=tk.Scale(window,length=400,showvalue=1,label='try me',tickinterval=2,from_=5,to=11,
           resolution=0.01,orient=tk.HORIZONTAL,command=print_selection)
s.pack()
window.mainloop()