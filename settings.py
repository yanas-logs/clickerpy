import tkinter as tk
from tkinter import messagebox

def open_settings(app):
    settings_window = tk.Toplevel(app.master)
    settings_window.title("Settings")

    preferences_button = tk.Button(
        settings_window, 
        text="Preferences", 
        command=lambda: open_preferences(app, settings_window)
    )
    preferences_button.pack(pady=10)

def open_preferences(app, settings_window):
    preferences_window = tk.Toplevel(settings_window)
    preferences_window.title("Preferences")

    time_button = tk.Button(
        preferences_window, 
        text="Time", 
        command=lambda: open_time_selection(app, preferences_window)
    )
    time_button.pack(pady=10)

def open_time_selection(app, preferences_window):
    time_window = tk.Toplevel(preferences_window)
    time_window.title("Time")

    time_options = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, "Custom"]
    time_listbox = tk.Listbox(time_window)
    for option in time_options:
        time_listbox.insert(tk.END, option)
    time_listbox.pack(pady=10)

    custom_time_entry = tk.Entry(time_window)

    def on_select(event):
        selected_time = time_listbox.get(time_listbox.curselection())
        if selected_time == "Custom":
            custom_time_entry.pack(pady=10)  
        else:
            custom_time_entry.pack_forget()  
            app.click_time = int(selected_time)  
            messagebox.showinfo("Preferences", f"Click Time set to {app.click_time} seconds.")

    time_listbox.bind('<<ListboxSelect>>', on_select)

    save_button = tk.Button(
        time_window, 
        text="Save", 
        command=lambda: save_settings(app, custom_time_entry)
    )
    save_button.pack(pady=10)

    close_button = tk.Button(
        time_window, 
        text="Close", 
        command=time_window.destroy
    )
    close_button.pack(pady=10)

def save_settings(app, custom_time_entry):
    custom_time = custom_time_entry.get()
    if custom_time.isdigit():
        app.click_time = int(custom_time)  
        messagebox.showinfo("Preferences", f"Custom Click Time set to {app.click_time} seconds.")
    else:
        messagebox.showerror("Error", "Please enter a valid number.")

# Main application
class MyApp:
    def __init__(self, master):
        self.master = master
        self.click_time = 10  

        settings_button = tk.Button(
            master, 
            text="Open Settings", 
            command=lambda: open_settings(self)
        )
        settings_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Application")
    app = MyApp(root)
    root.mainloop()

