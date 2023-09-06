from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """
    Generates a random password consisting of letters, numbers, and symbols.

    Parameters:
    None

    Returns:
    str: The randomly generated password.

    Algorithm:
    1. Create a list of letters, numbers, and symbols.
    2. Generate random lengths for the number of letters, symbols, and numbers in the password.
    3. Generate a list of characters for the password.
    4. Shuffle the characters in the password list.
    5. Concatenate the characters in the password list to form the final password.

    Complexity Analysis:
    - Time Complexity: O(n), where n is the maximum length of the password.
    - Space Complexity: O(n), where n is the maximum length of the password.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    """
    Saves the password for a website.

    This function retrieves the values from the website_entry, email_entry, and password_entry,
    and writes them to a file named "data.txt" in the format "{website} | {email} | {password}\n".

    Parameters:
    None
    Returns:
        None
    """
    website = website_entry.get()  # o metodo get() retorna o valor digitado
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:  # checa se o usuário deixou algum campo em branco
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    else:

        is_ok = messagebox.askokcancel(title=website,
                                       message=f"This info will be saved:\nEmail: {email}\nPassword: {password}\n"
                                               f"Do you want to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)  # padding

#  setting the logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#  setting the labels
website_label = Label(text="Website:", padx=5, pady=5)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", padx=5, pady=5)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", padx=5, pady=5)
password_label.grid(column=0, row=3)
#  setting the entries

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "jsepdrofnasc@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

#  setting the buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
