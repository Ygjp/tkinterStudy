import tkinter as tk
window=tk.Tk()
window.title("demo7")
window.geometry("200x200")
# 显示标签
l=tk.Label(window,bg='lightgreen',text='do')
l.pack()
counter=0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter+=1
# 在window上创建一个菜单栏（顶部横向细条）
menubar=tk.Menu(window)
# 在表面上显示的标签上添加容器（点开后的小页面）
filemenu=tk.Menu(menubar,tearoff=0)           # tearoff 为文字点开后是否有虚线分割（没什么用，了解,但是要写，默认是有虚线，需要更改为0）
# 表面上显示的标签（细条上的选项文字）---------
menubar.add_cascade(label='file',menu=filemenu)
# 在点开后的页面中添加内容（点开后的选项）
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
# 添加分割线
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)         # window.quit为退出程序
# 在表面上显示的标签上添加容器（点开后的小页面）
editmenu=tk.Menu(menubar,tearoff=0)
# 表面上显示的标签（细条上的选项文字）---------
menubar.add_cascade(label='Edit',menu=editmenu)
# 在点开后的页面中添加内容（点开后的选项）
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

# 添加多级目录同理
submenu = tk.Menu(editmenu)
editmenu.add_cascade(label='Import', menu=submenu)
submenu.add_command(label="Submenu1", command=do_job)
# 相当于刷新菜单页面，将刚刚创建好的菜单添加进窗口
window.config(menu=menubar)
window.mainloop()