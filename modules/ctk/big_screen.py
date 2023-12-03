import modules.ctk.start as c_start
import customtkinter as ctk
import modules.data_base as m_data
import modules.data.values as d_val
import modules.ctk.text as ct_text
from PIL import Image
import os
import modules.ctk.registration as ct_reg
import time
import modules.api as m_api
# print(time.)
def revision(city_name, text,y,text_1,color= "#096C82"):
    data1 = m_api.get_api(city_name)
    text_2 = m_api.text(data1)
    temp1 = data1["main"]
    temp2 = m_api.temp(temp1["temp"])
    temp3 = m_api.temp(temp1["temp_min"])
    temp4 = m_api.temp(temp1["temp_max"])
    label = ctk.CTkButton(master=m_data.screen,width=236,height=101,text="",border_color="#FFFFFF",bg_color="#096C82",fg_color=color,corner_radius=20,border_width=2,hover=False,)
    label.place(x=19,y=y)
    text1 = ct_text.Text(text=text,x=14+19,y=y+8,height=31,width=56,size=16,fg_color=color)
    text2 = ct_text.Text(text=text_1,x=14+19,y=y+33,height=31,width=56,size=12,fg_color =color)
    text3 = ct_text.Text(text=text_2,x=14+19,y=y+76,height=0,width=56,size=12,fg_color=color)
    text4 = ct_text.Text(text=temp2+"⁰",x=158+19,y=y+12,height=0,width=56,size=50,fg_color=color)
    text5 = ct_text.Text(text=f"макс.: {temp4}⁰, мин.: {temp3}⁰",x=122+19,y=y+76,height=0,width=56,size=12,fg_color=color)
def time1(text1,number,image,x):
    image = Image.open(os.path.abspath(__file__+f"/../../../images/{m_api.image(data)}.png"))
    image = ctk.CTkImage(dark_image=image,size=(54,50))
    image = ctk.CTkLabel(master=m_data.screen,width=50,height=52.08,text="",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1",image = image)
    image.place(x = x+325 ,y = 104+430)
    text4 = ct_text.Text(text=text1,x=x + 325,y=54 + 430,height=31,width=56,size=18)
    text8 = ct_text.Text(text=f"{number}⁰",x=325 + 7+x,y=173+430,height=30,width=41.02,size=30)
def delete():
    m_data.width = 460
    m_data.height  = 645
    background = ctk.CTkButton(master=m_data.screen,width=m_data.width,height=m_data.height,text="",border_width=5,fg_color="#5DA7B1",border_color="#096C82",hover= False,corner_radius=20)
    background.place(x = 0,y = 0)
    m_data.screen.geometry(f"{m_data.width}x{m_data.height}+{m_data.screen.winfo_screenwidth()//2-m_data.width//2}+{m_data.screen.winfo_screenheight()//2-m_data.height//2}")
    ct_reg.enter()
    ct_reg.name_entry.destroy()
    ct_reg.country_entry.destroy()
    ct_reg.place_entry.destroy()
    ct_reg.surname_entry.destroy()
    c_start.create()
    ct_reg.back()
    # ct_reg.text2.place(x = 46,y = 405)

    # ct_reg.text3.place(x = 46,y = 306)

    # ct_reg.text4.place(x = 46,y = 207)

    # ct_reg.text5.place(x = 46,y = 108)
data= m_api.get_api()
print(time.localtime())
def create():
    time_now = f"{time.localtime()[3]}:{time.localtime()[4]}"
    if time.localtime()[4]<10:
        time_now = f"{time.localtime()[3]}:0{time.localtime()[4]}"
    time_now1 =f"{time.localtime()[3]-1}:{time.localtime()[4]}"
    if time.localtime()[4]<10:
        time_now1 = f"{time.localtime()[3]-1}:0{time.localtime()[4]}"
    time_now2 = f"{time.localtime()[3]-2}:{time.localtime()[4]}"
    if time.localtime()[4]<10:
        time_now2 = f"{time.localtime()[3]-2}:0{time.localtime()[4]}"
    print(time_now)
    temp = m_api.temp(data["main"]["temp"])
    min_temp =  m_api.temp(data["main"]["temp_min"])
    max_temp =  m_api.temp(data["main"]["temp_min"])
    m_data.screen.title("big screen")
    m_data.width = 1200
    m_data.height  = 800
    background = ctk.CTkButton(master=m_data.screen,width=m_data.width,height=m_data.height,text="",border_width=5,fg_color="#5DA7B1",border_color="#096C82",hover= False,corner_radius=20)
    background.place(x = 0,y = 0)
    m_data.screen.geometry(f"{m_data.width}x{m_data.height}+{m_data.screen.winfo_screenwidth()//2-m_data.width//2}+{m_data.screen.winfo_screenheight()//2-m_data.height//2}")
    font = ctk.CTkFont(family=m_data.path,size=28)
    user_img = Image.open(os.path.abspath(__file__+"/../../../images/user_9970571.png"))
    name_image = data["weather"][0]["main"]
    # if name_image== "snow":

    img_cloudy = Image.open(os.path.abspath(__file__+f"/../../../images/{m_api.image(data)}.png"))
    img = Image.open(os.path.abspath(__file__+"/../../../images/line.png"))
    img = ctk.CTkImage(dark_image=img,size=(800,2))
    
    user_image = ctk.CTkImage(dark_image=user_img,size=(48.48,50))
    img_cloudu = ctk.CTkImage(dark_image=img_cloudy,size=(171,159))
    background1 = ctk.CTkButton(master=m_data.screen,width=275,height=800,text="",border_width=3,fg_color="#096C82",border_color="#FFFFFF",hover= False,corner_radius=20)
    
    background1.place(x=0,y=0)
    background2 = ctk.CTkButton(border_width=5,master=m_data.screen,width=818,height=240,text="",corner_radius=20,bg_color="#5DA7B1",fg_color="#5DA7B1",border_color = "#FFFFFF",hover= False)
    background2.place(x =325,y = 430)
    image = Image.open(os.path.abspath(__file__+"/../../../images/search.png"))
    image = ctk.CTkImage(dark_image=image,size=(27,27))
    enter = ctk.CTkEntry(font=font,master=m_data.screen,width = 218,height = 46,placeholder_text="   Пошук",border_width=3,fg_color = "#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")
    enter.place(x=918,y=31)
    label = ctk.CTkLabel(master=m_data.screen,width=27,height=27,text="",image=image,fg_color="#096C82")
    label.place(x=918+14,y=31+10)
    # transparent
    time1("Зараз",f"{temp}","cloudy",19)
    time1("15:00","12","sun",112)
    time1("16:00","10","sun",204)
    time1("16:05","9","sunset",296)
    time1("17:00","8","moon",388)
    time1("18:00","8","moon",480)
    time1("19:00","7","rain_moon",572)
    time1("20:00","5","rain_moon",664)
    time1("21:00","5","rain_moon",756)

    revision("Dnipro","Поточна позиція",31,"Дніпро","#4599A4")
    revision("Kiev","Київ",164,time_now)
    revision("Rome","Рим",297,time_now1)
    revision("London","Лондон",430,time_now2)
    revision("Warsaw","Варшава",563,time_now1)
    revision("Prague","Прага",696,time_now1)
    user = ctk.CTkButton(master=m_data.screen,width=48.48,height=50,text="",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="transparent",hover= False,image = user_image,command=delete)
    user.place(x = 318, y = 29)# сложный
    
    cloudy = ctk.CTkLabel(font=font,master=m_data.screen,width=171,height=159,text="",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1",image = img_cloudu)
    cloudy.place(x = 380 ,y = 171)

    text0 = ctk.CTkButton(master=m_data.screen,width=31,height=10,text=d_val.get_value(name_table="Users",cursor=m_data.cursor,name_column="name")+d_val.get_value(name_column="surname",name_table="Users",cursor=m_data.cursor),hover=False,fg_color="#5DA7B1",bg_color="#5DA7B1",command=delete)
    text0.place(x=380,y=39,)
    text1 = ctk.CTkLabel(font=font,master=m_data.screen,width=314,height=61,text="Поточна позіція",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text1.place(x = 576 ,y = 101)
    text2 = ctk.CTkLabel(font=font,master=m_data.screen,width=87,height=31,text="Дніпро",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text2.place(x = 689, y = 162)

    text3 = ct_text.Text(f"{temp}⁰",683,203,71,79,80)

    text4 = ct_text.Text(text="Зараз",x=19 + 325,y=54 + 430,height=31,width=56,size=18)
    text5 = ct_text.Text(text=m_api.text(data),x=663,y=284,height=37,width=140,size=30)
    # text6  = ct_text.Text(text="з проясненнями",x=663,y=321,height=16,width=140,size=16)
    text7 = ct_text.Text(text=f"↓{min_temp}⁰",x=673.43,y=345,height=27,width=19.48,size=30)
    
    

    text9 = ct_text.Text(text=f"↑{max_temp}⁰",x=738.03,y=345,height=27,width=30.76,size=30)
    text10 = ct_text.Text(text="Захід сонця о 16:05. Очікується дощова погода приблизно о 19:00",x=346,y=445,height=31,width=776,size=14)
    day = time.localtime()[-3]
    if day == 0:
        day = "Понеділок"
    elif day == 1:
        day = "Вівторок"
    elif day == 2:
        day = "Середа"
    elif day == 3:
        day = "Четверг"
    elif day == 4:
        day = "П'ятниця"
    elif day == 5:
        day = "Субота"
    elif day == 6:
        day = "Неділя"
    text11 = ct_text.Text(text=day,x=956,y=191,height=31,width=105,size=18)
    text12 = ct_text.Text(text=f"{time.localtime()[2]}.{time.localtime()[1]}.23",x=936,y=227,height=47,width=146,size=40)
    text13 = ct_text.Text(text=time_now,x=974,y=274,height=47,width=70,size=30)
    
    text14 = ct_text.Text(text=">",x=1160,y=524,height=31,width=18,size=50)
    text15 = ct_text.Text(text="<",x=289,y=524,height=31,width=18,size=50)
    # text16 = ct_text.Text(text=d_val.get_value(name_table="Users",cursor=m_data.cursor,name_column="name")+d_val.get_value(name_column="surname",name_table="Users",cursor=m_data.cursor) ,x=380,y=39,height=31,width=10,size=14)
    label = ctk.CTkLabel(master= m_data.screen,width=800,height=2,bg_color="#5DA7B1",fg_color="#5DA7B1",text="", image = img)
    label.place(x=19+325,y=46+430)
    # delete()