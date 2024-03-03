import tkinter as tk
import random

def create_loh_window():
    loh_window = tk.Toplevel(root)
    loh_window.title("LOSER")

    window_width = random.randint(200, 800)
    window_height = random.randint(200, 600)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = random.randint(0, screen_width - window_width)
    y_position = random.randint(0, screen_height - window_height)

    loh_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    label_text = "LOSER"
    label = tk.Label(loh_window, text=label_text, font=("Arial", 24))  # You can adjust the font size
    label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main title")

    for _ in range(1000):
        create_loh_window()

    root.mainloop()
