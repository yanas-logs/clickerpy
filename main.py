import tkinter as tk
import time
import threading
import pyautogui
import random  
from settings import open_preferences
from about import show_about

class Clickerpy:
    def __init__(self, master):
        self.master = master
        self.master.title("Clickerpy")

        self.click_time = 10  
        self.click_type = 'default'  

        self.theme = 'light'

        self.menu_bar = tk.Menu(master)

        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.preferences_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.preferences_menu.add_command(label="Set Click Time", command=self.open_time_selection)
        self.preferences_menu.add_command(label="Set Click Type", command=self.open_click_type_selection)

        self.settings_menu.add_cascade(label="Preferences", menu=self.preferences_menu)

        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Appearance", command=self.open_appearance_menu)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)

        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label="About", command=show_about)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)

        master.config(menu=self.menu_bar)

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.test_count = 0

        self.label = tk.Label(master, text="00.00.00", font=("Helvetica", 48))
        self.label.pack()

        self.test_label = tk.Label(master, text="Test Count: 0", font=("Helvetica", 24))
        self.test_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.test_button = tk.Button(master, text="Test", command=self.test_click)
        self.test_button.pack()

        self.reset_test_button = tk.Button(master, text="Reset Test", command=self.reset_test)
        self.reset_test_button.pack()

        self.auto_click_thread = None

    def open_preferences(self):
        settings_window = tk.Toplevel(self.master)
        settings_window.title("Preferences")

        open_preferences(self, settings_window)

    def open_time_selection(self):
        time_selection_window = tk.Toplevel(self.master)
        time_selection_window.title("Click Time")

        tk.Label(time_selection_window, text="Click Time (seconds)").pack(pady=10)

        self.custom_time_entry = tk.Entry(time_selection_window)
        self.custom_time_entry.pack(pady=10)

        self.current_time_label = tk.Label(time_selection_window, text=f"Current : {self.click_time} seconds")
        self.current_time_label.pack(pady=10)

        save_button = tk.Button(time_selection_window, text="Save", command=self.save_click_time)
        save_button.pack(pady=10)

    def save_click_time(self):
        try:
            self.click_time = int(self.custom_time_entry.get())
            self.current_time_label.config(text=f"Current: {self.click_time} seconds")  
            print(f"Click time set to: {self.click_time} seconds")  
        except ValueError:
            print("Invalid input. Please enter a number.")  

    def open_click_type_selection(self):
        click_type_window = tk.Toplevel(self.master)
        click_type_window.title("Click Type")

        tk.Label(click_type_window, text="Select Click Type:").pack(pady=10)

        click_type_var = tk.StringVar(value=self.click_type)
        tk.Radiobutton(click_type_window, text="Default Click", variable=click_type_var, value="default").pack() # i Click/Set Click Time
        tk.Radiobutton(click_type_window, text="Custom Click", variable=click_type_var, value="custom").pack() # Custom Click/s
        tk.Radiobutton(click_type_window, text="Randomize Click", variable=click_type_var, value="random").pack() # Random/Set Click Time

        save_button = tk.Button(click_type_window, text="Save", command=lambda: self.save_click_type(click_type_var.get()))
        save_button.pack(pady=10)

    def save_click_type(self, click_type):
        self.click_type = click_type
        print(f"Click type set to: {self.click_type}")

    def open_appearance_menu(self):
        appearance_window = tk.Toplevel(self.master)
        appearance_window.title("Appearance Settings")

        tk.Label(appearance_window, text="Background :").pack(pady=10)

        background_var = tk.StringVar(value=self.theme)
        tk.Radiobutton(appearance_window, text="Light", variable=background_var, value="light", command=lambda: self.set_theme('light')).pack()
        tk.Radiobutton(appearance_window, text="Dark", variable=background_var, value="dark", command=lambda: self.set_theme('dark')).pack()

    def set_theme(self, theme):
        self.theme = theme
        if self.theme == 'light':
            self.master.config(bg="white")
            self.label.config(bg="white", fg="black")
            self.test_label.config(bg="white", fg="black")
        elif self.theme == 'dark':
            self.master.config(bg="black")
            self.label.config(bg="black", fg="white")
            self.test_label.config(bg="black", fg="white")

    def toggle_clicker(self):
        if self.label.winfo_ismapped():
            self.label.pack_forget()  
        else:
            self.label.pack()  

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_stopwatch()
            self.auto_click_thread = threading.Thread(target=self.auto_click)
            self.auto_click_thread.start()

    def stop(self):
        self.running = False
        if self.auto_click_thread is not None:
            self.auto_click_thread.join()

    def reset(self):
        self.stop()
        self.elapsed_time = 0
        self.label.config(text="00.00.00")

    def test_click(self):
        self.test_count += 1
        self.test_label.config(text=f"Test Count: {self.test_count}")

    def reset_test(self):
        self.test_count = 0
        self.test_label.config(text="Test Count: 0")

    def update_clicker(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(self.elapsed_time, 60)
            milliseconds = (self.elapsed_time - int(self.elapsed_time)) * 100
            self.label.config(text=f"{int(minutes):02d}.{int(seconds):02d}.{int(milliseconds):02d}")
            self.master.after(10, self.update_stopwatch)

    def auto_click(self):
        while self.running:
            if self.click_type == 'default':
                time.sleep(self.click_time)  
                pyautogui.click()
            elif self.click_type == 'custom':
                clicks_per_second = 3  
                interval = 1 / clicks_per_second
                for _ in range(clicks_per_second):
                    pyautogui.click()
                    time.sleep(interval)
            elif self.click_type == 'random':
                random_interval = random.uniform(5, 15)  
                
                clicks_in_interval = random.choice([1, 2])  
                
                for _ in range(clicks_in_interval):
                    pyautogui.click()
                    time.sleep(random_interval / clicks_in_interval)  
            
            time.sleep(self.click_time)  

if __name__ == "__main__":
    root = tk.Tk()
    app = Clickerpy(root)
    root.mainloop()

