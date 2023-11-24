import modules.ctk.start as c_start
import customtkinter as ctk
import modules.data_base as m_data
import modules.data.values as d_val
import modules.ctk.text as ct_text
def create():
    m_data.width = 1200
    m_data.height  = 800
    background = ctk.CTkButton(master=m_data.screen,width=m_data.width,height=m_data.height,text="",border_width=5,fg_color="#5DA7B1",border_color="#096C82",hover= False,corner_radius=20)
    background.place(x = 0,y = 0)
    m_data.screen.geometry(f"{m_data.width}x{m_data.height}+{m_data.screen.winfo_screenwidth()//2-m_data.width//2}+{m_data.screen.winfo_screenheight()//2-m_data.height//2}")
    font = ctk.CTkFont(family=m_data.path,size=28)
    
    background1 = ctk.CTkButton(master=m_data.screen,width=275,height=800,text="",border_width=3,fg_color="#096C82",border_color="#FFFFFF",hover= False,corner_radius=20)
    background1.place(x=0,y=0)
    text1 = ctk.CTkLabel(font=font,master=m_data.screen,width=314,height=61,text="Поточна позіція",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text1.place(x = 576 ,y = 101)
    text2 = ctk.CTkLabel(font=font,master=m_data.screen,width=87,height=31,text="Дніпро",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text2.place(x = 689, y = 162)
    text3 = ct_text.Text("11",683,203,71,79,80)
    text4 = ct_text.Text(text="о",x=754,y=203,height=16,width=16,size=30)
    text5 = ct_text.Text(text="Хмарно",x=663,y=284,height=53,width=140,size=30)
    # text6  = ct_text.Text(text="з проясненнями",x=754,y=203,height=16,width=16,size=16)
    text7 = ct_text.Text(text="↓5",x=689.84,y=348,height=27,width=19.48,size=30)
    text8 = ct_text.Text(text="о",x=711.37,y=345,height=11,width=10.25,size=15)

    text9 = ct_text.Text(text="↑11",x=754.44,y=348,height=27,width=30.76,size=30)
    text10 = ct_text.Text(text="о",x=785.25,y=345,height=11,width=10.25,size=15)
    
    text11 = ct_text.Text(text="Понеділок",x=956,y=191,height=31,width=105,size=18)
    text12 = ct_text.Text(text="24.11.23",x=936,y=227,height=47,width=146,size=40)
    text13 = ct_text.Text(text="21:23",x=974,y=274,height=47,width=70,size=30)
    
    text14 = ct_text.Text(text=">",x=1160,y=524,height=31,width=18,size=50)
    text15 = ct_text.Text(text="<",x=289,y=524,height=31,width=18,size=50)

    text16 = ct_text.Text(text="Name Surname",x=380,y=39,height=31,width=220,size=14)