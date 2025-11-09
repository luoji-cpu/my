#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
爱心告白弹窗程序
使用Python内置库实现多线程爱心弹窗效果
"""

import tkinter as tk
import random as ra
import threading as td
import time as ti
import sys

# 核心配置参数
# 爱心文案列表
love_messages = [
    "遇见你，是我最美的意外",
    "你是我藏在心底的温柔",
    "想和你一起看遍世间繁华",
    "你的名字，是我读过最短的情诗",
    "余生很长，想和你一起浪费",
    "你是我绕过山河，才遇见的人间烟火",
    "喜欢你，胜于昨日，略匮明朝",
    "想和你有以后",
    "你是我疲惫生活的解药",
    "遇见你之前，爱情只是个词",
    "遇见你之后，爱情有了名字",
    "想牵你的手，敬各方来宾的酒",
    "你是我所有的不动声色中，最盛大的欢喜",
    "我喜欢你，像风走了八千里，不问归期",
    "你是我眼里的星辰大海",
    "想和你一起走过四季，看尽人间烟火",
    "你是我心中最柔软的地方",
    "遇见你，是所有故事的开始",
    "想和你有以后，想和你有未来",
    "你是我此生最美的遇见"
]

# 柔和颜色列表 (RGB格式)
soft_colors = [
    "#FFE4E1", "#FFF0F5", "#FFE4E6", "#FCE4EC", "#F8BBD9",
    "#FBB6CE", "#F9A8D4", "#F472B6", "#EC4899", "#DB2777",
    "#BE185D", "#9D174D", "#831843", "#FED7D7", "#FEB2B2",
    "#FC8181", "#F56565", "#E53E3E", "#C53030", "#9B2C2C"
]

# 字体列表
fonts = [
    "微软雅黑", "宋体", "楷体", "黑体", "仿宋",
    "Arial", "Times New Roman", "Helvetica", "Comic Sans MS", "Verdana"
]

class LovePopup:
    def __init__(self):
        self.running = True
        self.popup_count = 0
        self.max_popups = 50  # 最大弹窗数量
        
    def create_popup(self):
        """创建单个爱心弹窗"""
        if not self.running or self.popup_count >= self.max_popups:
            return
            
        self.popup_count += 1
        
        # 创建新窗口
        popup = tk.Toplevel()
        popup.title("❤")
        
        # 随机窗口大小
        width = ra.randint(100, 250)
        height = ra.randint(50, 100)
        
        # 获取屏幕尺寸
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        
        # 随机位置
        x = ra.randint(0, screen_width - width)
        y = ra.randint(0, screen_height - height)
        
        # 设置窗口属性
        popup.geometry(f"{width}x{height}+{x}+{y}")
        popup.configure(bg=ra.choice(soft_colors))
        popup.attributes('-topmost', True)
        popup.attributes('-alpha', ra.uniform(0.8, 1.0))
        
        # 移除窗口装饰
        popup.overrideredirect(True)
        
        # 随机选择文案和字体
        message = ra.choice(love_messages)
        font_family = ra.choice(fonts)
        font_size = ra.randint(10, 16)
        
        # 创建标签
        label = tk.Label(
            popup,
            text=message,
            font=(font_family, font_size),
            bg=popup.cget('bg'),
            fg="#8B0000",
            wraplength=width-20,
            justify='center'
        )
        label.pack(expand=True, fill='both', padx=10, pady=10)
        
        # 添加爱心符号
        heart_label = tk.Label(
            popup,
            text="❤",
            font=("Arial", 20),
            bg=popup.cget('bg'),
            fg="#FF1493"
        )
        heart_label.place(relx=0.5, rely=0.1, anchor='center')
        
        # 点击关闭功能
        def close_popup(event=None):
            try:
                popup.destroy()
                self.popup_count -= 1
            except:
                pass
                
        popup.bind("<Button-1>", close_popup)
        label.bind("<Button-1>", close_popup)
        
        # 自动关闭时间
        close_time = ra.randint(3000, 8000)  # 3-8秒后自动关闭
        popup.after(close_time, close_popup)
        
    def popup_generator(self):
        """弹窗生成器线程"""
        while self.running and self.popup_count < self.max_popups:
            # 随机间隔生成弹窗
            interval = ra.uniform(0.5, 2.0)
            ti.sleep(interval)
            
            if self.running:
                # 在主线程中创建弹窗
                root.after(0, self.create_popup)
                
    def start(self):
        """启动程序"""
        global root
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        
        # 创建控制面板
        control = tk.Toplevel()
        control.title("爱心告白控制器")
        control.geometry("300x200")
        control.configure(bg="#FFE4E1")
        control.attributes('-topmost', True)
        
        # 标题
        title = tk.Label(
            control,
            text="💝 爱心告白弹窗 💝",
            font=("微软雅黑", 16, "bold"),
            bg="#FFE4E1",
            fg="#8B0000"
        )
        title.pack(pady=20)
        
        # 状态标签
        status = tk.Label(
            control,
            text=f"已生成: {self.popup_count}/{self.max_popups}",
            font=("微软雅黑", 12),
            bg="#FFE4E1",
            fg="#666666"
        )
        status.pack()
        
        # 更新状态函数
        def update_status():
            if self.running:
                status.config(text=f"已生成: {self.popup_count}/{self.max_popups}")
                control.after(1000, update_status)
        
        # 开始按钮
        def start_love():
            if not hasattr(self, 'generator_thread') or not self.generator_thread.is_alive():
                self.generator_thread = td.Thread(target=self.popup_generator, daemon=True)
                self.generator_thread.start()
            start_btn.config(state='disabled')
            update_status()
        
        start_btn = tk.Button(
            control,
            text="开始告白",
            command=start_love,
            font=("微软雅黑", 12),
            bg="#FF69B4",
            fg="white",
            padx=20,
            pady=5
        )
        start_btn.pack(pady=10)
        
        # 停止按钮
        def stop_love():
            self.running = False
            control.destroy()
            root.quit()
            sys.exit()
            
        stop_btn = tk.Button(
            control,
            text="停止程序",
            command=stop_love,
            font=("微软雅黑", 12),
            bg="#FFB6C1",
            fg="#8B0000",
            padx=20,
            pady=5
        )
        stop_btn.pack(pady=5)
        
        # 说明文字
        note = tk.Label(
            control,
            text="点击弹窗可立即关闭",
            font=("微软雅黑", 10),
            bg="#FFE4E1",
            fg="#999999"
        )
        note.pack(pady=5)
        
        # 启动主循环
        try:
            root.mainloop()
        except KeyboardInterrupt:
            self.running = False
            sys.exit()

if __name__ == "__main__":
    love_app = LovePopup()
    love_app.start()