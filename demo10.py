import tkinter as tk
window=tk.Tk()
window.geometry('300x300')
window.title('demo9')

# tk.Label(window,text=1).pack(side='top')
# tk.Label(window,text=1).pack(side='left')
# tk.Label(window,text=1).pack(side='bottom')
# tk.Label(window,text=1).pack(side='right')

# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text=1).grid(row=i,column=j,padx=10,pady=10) # row意为行数，即第几行，column意为列数，即第几列
#         # padx 横向间隔宽度，pady 纵向间隔宽度


# 最常用的：
# 窗口的左上角为坐标原点，向右x轴，向下y轴
tk.Label(window,text=1).place(x=10,y=20)

# 根据情况选择最为简单合适的布局方式

window.mainloop()
