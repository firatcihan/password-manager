from tkinter import *
import json
from tkinter import messagebox
import random
import pyperclip   ### copy generated password
string_list = ""
# ------- PASSWORD GENERATOR ------- #
def password_generate():
    sayilar= ["0","1","2","3","4","5","6","7","8","9"]
    harfler = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","u","p","r","s","t","y","z","v"]
    semboller = ['!','+','%','&','/','?','=',]

    harf = random.randint(6,8)
    sayi = random.randint(1,2) 
    sembol = random.randint(1,2)
    sifre = []

    sifre += [random.choice(harfler) for _ in range(harf)]

    sifre += [random.choice(sayilar) for _ in range(sayi)]

    sifre += [random.choice(semboller) for _ in range(sembol)]

    random.shuffle(sifre)

    temp ="".join(sifre)
    
    password_girdi.delete(0, END)
    password_girdi.insert(0, temp)
    pyperclip.copy(temp)     ### copy generated password
# ------ SEARCH PASSWORD ----- #
def find_password():
    website = website_girdi.get()
    try:
        with open("100daysofcode/password manager/data.json" ,"r") as dosyake:
            datake = json.load(dosyake)
    except FileNotFoundError:
            messagebox.showinfo(title="Hata", message=f"aradiginiz {website} isimli website bulunamadi")
    else:
        if website in datake:
            messagebox.showinfo(title=website, message=f"email/username: {datake[website]["email"]}\npassword: {datake[website]["sifre"]}")
        else:
            messagebox.showinfo(title="Hata", message=f"aradiginiz {website} isimli website bulunamadi")
# ---- SAVE PASSWORD ------ #
def save_password():
    website = website_girdi.get()
    email = username_girdi.get()
    sifre = password_girdi.get()
    data_dic = {
        website: {
            "email": email,
            "sifre": sifre,
        }
    }

    if len(website) == 0 or len(sifre) == 0 or len(email) == 0:
        messagebox.showwarning(title="hatali kayit" , message="tum bosluklar eksiksiz olarak doldurulmalidir")
    else:
        try:
            with open("100daysofcode/password manager/data.json" ,"r") as dosya:
                data = json.load(dosya)   ### dosya read komutu
        except FileNotFoundError:
            with open("100daysofcode/password manager/data.json", "w") as dosya:
                json.dump(data_dic, dosya , indent=4)
        else:
            data.update(data_dic)

            with open("100daysofcode/password manager/data.json" ,"w") as dosya:
                json.dump(data, dosya, indent=4) ### write komutu
        finally:
            website_girdi.delete(0, END)
            password_girdi.delete(0, END)
            label4.config(text="kayit başari ile tamamlandi")
# ------ UI SETUP ----- #
win = Tk()
win.title("Password Manager")
win.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)

first_image = PhotoImage(file="100daysofcode/password manager/logo.png")
canvas.create_image(100, 100 , image=first_image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:", font=("arial", 10, "normal"))
label1.grid(column=0,row=1)

label2 = Label(text="Email/Username:", font=("arial", 10, "normal"))
label2.grid(column=0,row=2)

label3 = Label(text="Password:", font=("arial", 10, "normal"))
label3.grid(column=0,row=3)

label4 = Label(text="", font=("arial", 10, "normal"))
label4.grid(column=1,row=5)


website_girdi = Entry(width=21)
website_girdi.grid(column=1, row=1)
website_girdi.focus()

username_girdi = Entry(width=35)
username_girdi.grid(column=1, row=2, columnspan=2)
username_girdi.insert(0, "firatcihan18@hotmail.com")

password_girdi = Entry(width=21)
password_girdi.grid(column=1, row=3)

password_button = Button(text="Gen Password", width=11, command=password_generate)
password_button.grid(column=2, row=3)

button1 = Button(text="Add", width=36, command=save_password)
button1.grid(column=1, row=4, columnspan=2, pady=10)

button2 = Button(text="Search", width=11, command=find_password)
button2.grid(column=2, row=1)

win.mainloop()
