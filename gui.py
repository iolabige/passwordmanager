import tkinter as tk
from tkinter import messagebox
import logic

def add_password() -> None:
    """
    Adds a new password entry to the storage.
    Retrieves the website, username, and password from the entry fields,
    then uses the logic module to save this data.
    """
    try:
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        logic.add_password(website, username, password)
        messagebox.showinfo("Success", "Password added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        clear_entries()

def retrieve_password() -> None:
    """
    Retrieves an existing password entry from the storage.
    Displays the username and password if found, otherwise shows an error.
    """
    try:
        website = website_entry.get()
        username, password = logic.get_password(website)
        if username:
            messagebox.showinfo("Password Retrieved", f"Website: {website}\nUsername: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Error", "No password found for this website.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        clear_entries()

def delete_password() -> None:
    """
    Deletes an existing password entry from the storage.
    Notifies the user whether the deletion was successful or not.
    """
    try:
        website = website_entry.get()
        if logic.delete_password(website):
            messagebox.showinfo("Success", "Password deleted successfully!")
        else:
            messagebox.showerror("Error", "No password found for this website.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        clear_entries()

def clear_entries() -> None:
    """
    Clears all input fields in the user interface.
    """
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def setup_ui(main_window: tk.Tk) -> None:
    """
    Sets up the user interface elements in the given window.

    Args:
        main_window (tk.Tk): The main application window.
    """
    global website_entry, username_entry, password_entry

    main_window.title("Key Manager")

    # Creating labels and entry fields for user inputs
    tk.Label(main_window, text="Website").grid(row=0)
    tk.Label(main_window, text="Username").grid(row=1)
    tk.Label(main_window, text="Password").grid(row=2)

    website_entry = tk.Entry(main_window)
    username_entry = tk.Entry(main_window)
    password_entry = tk.Entry(main_window, show="*")

    website_entry.grid(row=0, column=1)
    username_entry.grid(row=1, column=1)
    password_entry.grid(row=2, column=1)

    # Creating buttons for different operations
    tk.Button(main_window, text="Add Password", command=add_password).grid(row=3, column=0)
    tk.Button(main_window, text="Retrieve Password", command=retrieve_password).grid(row=3, column=1)
    tk.Button(main_window, text="Delete Password", command=delete_password).grid(row=4, column=0)
