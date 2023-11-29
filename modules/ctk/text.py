import customtkinter as ctk
import modules.data_base as m_data
class Text:
    def __init__(self,text,x,y,height,width,size,master =m_data.screen):
        self.TEXT=text
        self.X=x
        self.Y=y
        self.HEIGNT=height
        self.WIDTH=width
        self.SIZE=size
        font = ctk.CTkFont(family=m_data.path,size=size)
        self.TEXT1=  ctk.CTkLabel(font=font ,master=master,width=width,height=height,text=text,text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
        self.TEXT1.place(x = x,y = y)
    def destroy(self):
        self.TEXT1.destroy()#я отойду не на долго