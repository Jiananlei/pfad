import tkinter as tk
from PIL import Image, ImageTk
import os
import math

# 创建主窗口
root = tk.Tk()
root.geometry("2000x1000")

# 获取图片的绝对路径
image_path = os.path.abspath("/Users/leijianan/Downloads/4ac6e68f6743bfb03f5dd88b2952195f.jpeg")  # 替换为你的图片路径

# 加载图片
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# 初始化点击计数
click_count = 0

def on_click(event):
    global click_count
    click_count += 1

    # 获取屏幕宽高
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取图片宽高
    img_width, img_height = image.size

    # 计算螺旋位置
    angle = click_count * 30  # 每次点击增加的角度
    radius = 20 * click_count  # 每次点击增加的半径
    x = screen_width // 2 + int(radius * math.cos(math.radians(angle))) - img_width // 2
    y = screen_height // 2 + int(radius * math.sin(math.radians(angle))) - img_height // 2

    # 在计算位置弹出图片
    popup = tk.Toplevel(root)
    popup.geometry(f"{img_width}x{img_height}+{x}+{y}")
    popup.overrideredirect(True)  # 去掉窗口边框

    img_label = tk.Label(popup, image=photo)
    img_label.pack()

# 绑定鼠标点击事件
root.bind("<Button-1>", on_click)

root.mainloop()