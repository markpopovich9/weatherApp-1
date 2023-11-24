import modules.data_base as m_data
#import modules.ctk.start as c_start 
# ↑↓ 1⁰
from PIL import Image
import customtkinter as ctk
import os
import threading
screen = ctk.CTk()
m_data.width = 350
m_data.height  = 350
m_data.screen.geometry(f"{m_data.width}x{m_data.height}+{m_data.screen.winfo_screenwidth()//2-m_data.width//2}+{m_data.screen.winfo_screenheight()//2-m_data.width//2}")
# img1 = 
# img2 = 
font = ctk.CTkFont(family=m_data.path,size=28,weight=("bold"))
text1 = ctk.CTkLabel(font=font,master=m_data.screen,width=170,height=52,text="Дніпро",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text1.place(x = 180,y = 274)

screen.mainloop()