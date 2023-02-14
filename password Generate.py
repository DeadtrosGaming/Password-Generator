import sys
import subprocess

for package in [['pyperclip'], ['customtkinter']]:
    try:
        __import__(package[-1])
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package[0]])

import customtkinter
import pyperclip
import random

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("450x325")  # The window size
app.title("")  # You set the title


def pass_gen(length: int, password_input_variable: customtkinter.CTkTextbox, text_variable: customtkinter.StringVar):
    password_input_variable.delete("1.0", "end-1c")
    chars = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=|\]}[{';:/?.>,<"

    def f(a, b):
        for char in a:
            if char in b:
                return True
        return False

    while True:
        password = ''
        for _ in range(length):
            password += random.choice(chars)
        if len(password) == length and f(password, chars):
            break

    password_input_variable.insert('0.0', text=str(password))
    text_variable.set("Copy password to clipboard")


def copy_password_to_clipboard(string_password: str, text_variable: customtkinter.StringVar):
    pyperclip.copy(string_password)
    text_variable.set("Password copied to clipboard")


Label = customtkinter.CTkLabel(master=app, text="Password Generator", font=customtkinter.CTkFont(size=25,
                                                                                                 weight="bold"))
Length = customtkinter.CTkSlider(master=app, to=256)
Password = customtkinter.CTkTextbox(master=app, width=315, height=108)
Button = customtkinter.CTkButton(master=app, text="Generate Password",
                                 command=lambda: pass_gen(int(Length.get()), Password,
                                                          password_copied_to_clipboard_button_text)
                                 )

Label.pack(padx=20, pady=(20, 10))
Button.pack(pady=10, padx=10)
Length.pack(padx=10, pady=10)
Length.set(12)
Password.pack(padx=10, pady=10)


password_copied_to_clipboard_button_text = customtkinter.StringVar()
password_copied_to_clipboard_button_text.set("Copy password to clipboard")

customtkinter.CTkButton(master=app, textvariable=password_copied_to_clipboard_button_text,
                        command=lambda: copy_password_to_clipboard(Password.get("1.0", "end-1c"),
                                                                   password_copied_to_clipboard_button_text)
                        ).pack(padx=10, pady=10)

app.mainloop()
