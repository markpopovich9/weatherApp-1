import customtkinter as ctk
import os
import sqlite3
data = sqlite3.connect(os.path.abspath(__file__+"/../../data_base/data.db"))
cursor = data.cursor()
screen = ctk.CTk()
height = 0
width = 0

path = os.path.abspath(__file__+"/../../fonts/RobotoSlap-bold.ttf")