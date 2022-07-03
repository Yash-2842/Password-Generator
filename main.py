import tkinter
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += ([random.choice(symbols) for _ in range(nr_symbols)])
    password_list += ([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if website_entry.get() == "" or Username_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \nEmail: "
                                                                          f"{Username_entry.get()} \nPassword: "
                                                                          f"{password_entry.get()} "
                                                                          f" \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_entry.get()} | {Username_entry.get()} | {password_entry.get()} \n")
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Generator")
window.config(padx=60, pady=60)

img = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:", pady=10)
website_label.grid(row=1, column=0)

username_label = tkinter.Label(text="Email/Username:", pady=10)
username_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:", pady=10)
password_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

Username_entry = tkinter.Entry(width=52)
Username_entry.grid(row=2, column=1, columnspan=2)
Username_entry.insert(0, "prajapatiyash916@gmail.com")

password_entry = tkinter.Entry(width=33)
password_entry.grid(row=3, column=1)

generate_password_btn = tkinter.Button(text="Generate Password", command=password_generate)
generate_password_btn.grid(row=3, column=2)

add_btn = tkinter.Button(width=44, text="Add", command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
