import modules.data_base as m_data
import customtkinter as ctk

def registration():
    global button,name_entry,surname_entry,country_entry,place_entry
    #get бере текст який ми вказуємо у текстовому полі
    name = name_entry.get()
    surname = surname_entry.get()
    country = country_entry.get()
    place =  place_entry.get()
    print(name,surname,country,place)
# створюємо кнопку при натисканні на неї викликається функція registration
button = ctk.CTkButton(master=m_data.screen,width=100,height=50,text="зарегистрируваться",border_width=5,fg_color="green",command=registration)

button.place(x = m_data.width/2,y = m_data.height/2+120,anchor=ctk.CENTER)
#ctk.Entry - текстовое поле
name_entry = ctk.CTkEntry(master=m_data.screen,width = 200,height = 50,placeholder_text="ім'я",border_width=5,fg_color="white",text_color="black")
surname_entry = ctk.CTkEntry(master=m_data.screen,width = 200,height = 50,placeholder_text="фамілія",border_width=5,fg_color="white",text_color="black")
country_entry = ctk.CTkEntry(master=m_data.screen,width = 200,height = 50,placeholder_text="страна",border_width=5,fg_color="white",text_color="black")
place_entry = ctk.CTkEntry(master=m_data.screen,width = 200,height = 50,placeholder_text="місто",border_width=5,fg_color = "white",text_color="black")

name_entry.place(x=m_data.width/2,y=m_data.height/2-120,anchor=ctk.CENTER)
surname_entry.place(x=m_data.width/2,y=m_data.height/2-60,anchor=ctk.CENTER)
country_entry.place(x=m_data.width/2,y=m_data.height/2,anchor=ctk.CENTER)
place_entry.place(x=m_data.width/2,y=m_data.height/2+60,anchor=ctk.CENTER)