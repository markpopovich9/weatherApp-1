import customtkinter as ctk
import os
import sqlite3
import modules.data.values as d_values

cities = ["Dnipro", "Kiev", "Rome", "London", "Warsaw", "Prague"]
cities_Ua = ["Дніпро","Київ","Рим","Лондон","Варшава","Прага"]
print(os.path.abspath(__file__+"/../../../data_base/data.db"),'\n',__file__)
data = sqlite3.connect(os.path.abspath(__file__+"/../../auto/data_base/data.db"))
cursor = data.cursor()
try:
    city = d_values.get_value("Users",cursor,"place")[0][0]
except:
    city= "Дніпро"
screen = ctk.CTk()
height = 0
width = 0
reg = False
path = os.path.abspath(__file__+"/../../fonts/RobotoSlap-bold.ttf")
