import modules.data_base as m_data
import customtkinter as ctk
import modules.data.values as d_values
# m_data.screen.geometry(f"{m_data.width}x{m_data.height}+{m_data.screen.winfo_screenwidth()//2-m_data.width//2}+{m_data.screen.winfo_screenheight()//2-m_data.width//2}")
m_data.screen.title("Особистий кабінет")


font = ctk.CTkFont(family=m_data.path,size=28,weight=("bold"))

text1 = ctk.CTkLabel(font=font,master=m_data.screen,width=380,height=55,text="Особисий кабінет",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text1.place(x = 38,y = 42)
# text2 = ctk.CTkLabel(font= font,master=m_data.screen,width=121,height=31,text="прівище:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
# text2.place(x = 46,y = 405)

# text3 = ctk.CTkLabel(font= font, master=m_data.screen,width=87,height=31,text="ім'я:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
# text3.place(x = 46,y = 306)


# text4 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text="місто:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
# text4.place(x = 46,y = 207)

# text5 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text="країна:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
# text5.place(x = 46,y = 108)



text6 = ctk.CTkLabel(font= font,master=m_data.screen,width=121,height=31,text=d_values.get_value("Users",m_data.cursor,"surname"),text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text6.place(x = 119,y = 455)

text7 = ctk.CTkLabel(font= font, master=m_data.screen,width=87,height=31,text=d_values.get_value("Users",m_data.cursor,"name"),text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text7.place(x = 121,y = 352)


text8 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text=d_values.get_value("Users",m_data.cursor,"place"),text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text8.place(x = 121,y = 256)

text9 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text=d_values.get_value("Users",m_data.cursor,"country"),text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text9.place(x = 119,y = 157)


font = ctk.CTkFont(family=m_data.path,size=18,weight=("bold"))

button = ctk.CTkButton(font= font,master=m_data.screen,width=218,height=46,text="Перейти до додатку",border_width=3,fg_color="#096C82", border_color= "#FFFFFF",text_color="#FFFFFF",corner_radius=20,bg_color="#5DA7B1")
button.place(x = 119,y = 546)