import tkinter as tk
window=tk.Tk()
window.geometry('450x300')
window.title('demo11')
# 创建一个画布对象
canvas=tk.Canvas(window,height=200,width=500)
# 创建一个照片对象
image_file=tk.PhotoImage(file='image_path') #image_path为图片的路径
# 把照片对象放进画布里面
image=canvas.create_image(0,0,anchor='nw',image=image_file)  # 第一个参数为放置的坐标，anchor=‘nw’ 代表依据左上角放置
# 放置画布对象
canvas.pack(side='top')
window.mainloop()