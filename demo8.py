import tkinter as tk
window=tk.Tk()
window.geometry('300x300')
window.title('demo8')

tk.Label(window,text='on the window').pack()

# 定义一个Frame框架，放在window上面，（相当于一个大的容器），在这里放在了第一个定义的Label标签的下面
frm=tk.Frame(window)
frm.pack()

# 在第一个定义的大的Frame框架里面再定义两个Frame框架
frm_l=tk.Frame(frm)
frm_r=tk.Frame(frm)

# 将这两个小的Frame框架放在第一个大的Frame框架的里面
frm_l.pack(side='left')#用pack里面的side参数来决定放的位置（小框架在大框架里面的位置）
frm_r.pack(side='right')

# 定义标签放在Frame框架里面
tk.Label(frm_l,text='on the frm_l').pack()
tk.Label(frm_l,text='on the frm_l').pack()
tk.Label(frm_r,text='on the frm_r').pack()
window.mainloop()