import tkinter as tk
window=tk.Tk()
window.title("demo4")
window.geometry("600x300")
var=tk.StringVar()
l=tk.Label(window,width=30,bg='green',text='empty')
l.pack()

def print_selection():
    # config可以对应组件里面的参数
    l.config(text='you have selection'+var.get())
# variable与va绑定r，variable的值设置为‘A’即->var的值设置为‘A’
r1=tk.Radiobutton(window,text='Option A',variable=var,value='A',command=print_selection)
r1.pack()
r2=tk.Radiobutton(window,text='Option B',variable=var,value='B',command=print_selection)
r2.pack()
r3=tk.Radiobutton(window,text='Option C',variable=var,value='C',command=print_selection)
r3.pack()
window.mainloop()