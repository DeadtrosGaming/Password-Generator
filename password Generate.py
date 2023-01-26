import random
import os

try:
    import customtkinter
except:
    os.system('pip install customtkinter')
    import customtkinter

try:
    import pyperclip
except:
    os.system('pip install pyperclip')
    import pyperclip

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk() # create CTk window like you do with the Tk window
app.geometry("450x325") # The window size
app.title("") # You set set the title 

def pass_gen():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=|\]}[{';:/?.>,<"

    length = int(Length.get())

    def f(a, b):
        for char in a:
            if char in b:
                return True
        return False

    flag = True
    while flag: 
        password = ''
        for _ in range(length):
            password += random.choice(chars)
        if len(password) == length and f(password, chars):
            flag = False
    Password.insert('0.0',text=str(password))
    pyperclip.copy(password)

Label = customtkinter.CTkLabel(master=app, text="Password Generator", font=customtkinter.CTkFont(size=25, weight="bold"))
Label.pack(padx=20, pady=(20, 10))

Length = customtkinter.CTkSlider(master=app, from_=0, to=256)
Length.pack(padx=10, pady=10)
Length.set(12)

Button = customtkinter.CTkButton(master=app, text="Generate Password", command=pass_gen)
Button.pack(pady=10, padx=10)

Password = customtkinter.CTkTextbox(master=app, width=315, height=108)
Password.pack(padx=10, pady=10)

Label = customtkinter.CTkLabel(master=app, text="Copyed To Clipbord", font=customtkinter.CTkFont(size=20, weight="bold"))
Label.pack(padx=10, pady=10)

app.mainloop()
