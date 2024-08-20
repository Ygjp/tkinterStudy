import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.geometry('300x300')
window.title('demo9')
def hit_me():
    # tk.messagebox.showwarning(title='Hi',message=' ! 提示警告的弹窗')

    # tk.messagebox.showinfo(title='Hi',message=' i 提示信息的弹窗')

    # tk.messagebox.showerror(title='Hi',message=' i 提示错误的弹窗')

    info=tk.messagebox.askquestion(title='Hi',message='弹窗中有两个选择（yes no），选择会返回信息(yes no)，图标是？')
    print(info,type(info))

    # info=tk.messagebox.askyesno(title='Hi',message='弹窗中有两个选择（yes no），选择会返回信息(True False),图标是？')
    # print(info,type(info))

    # info = tk.messagebox.askretrycancel(title='Hi', message='弹窗中有两个选择（yes no），选择会返回信息(True False)，图标是！')
    # print(info, type(info))

    # info = tk.messagebox.askokcancel(title='Hi', message='弹窗中有两个选择（yes no），选择会返回信息(True False)，图标是？')
    # print(info, type(info))
tk.Button(window,text='hit me',command=hit_me).pack()

window.mainloop()