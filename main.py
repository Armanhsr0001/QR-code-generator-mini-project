"""
QR Code Generator GUI - Mini Project
Uses Tkinter + pyqrcode + Pillow
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import pyqrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry_data.get()
    file_name = entry_filename.get()
    
    if not data:
        messagebox.showerror("Error", "Please enter text or URL.")
        return
    
    if not file_name:
        messagebox.showerror("Error", "Please enter file name.")
        return

    scale = scale_var.get()
    qr = pyqrcode.create(data)
    qr.png(f"{file_name}.png", scale=scale)

    # Load and show preview
    img = Image.open(f"{file_name}.png")
    img = img.resize((200, 200))
    qr_img = ImageTk.PhotoImage(img)

    qr_label.config(image=qr_img)
    qr_label.image = qr_img

    messagebox.showinfo("Success", f"QR Code saved as {file_name}.png")


def browse_save_location():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        entry_filename.delete(0, tk.END)
        entry_filename.insert(0, file_path.split("/")[-1].replace(".png", ""))


# 🖥 GUI Window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.config(bg="#e3f2fd")

# Heading
title = tk.Label(root, text="QR Code Generator", font=("Arial", 18, "bold"), bg="#e3f2fd")
title.pack(pady=10)

# Input field for data
tk.Label(root, text="Enter Text/URL:", bg="#e3f2fd", font=("Arial", 12)).pack()
entry_data = tk.Entry(root, width=40)
entry_data.pack(pady=5)

# File name input
tk.Label(root, text="File Name:", bg="#e3f2fd", font=("Arial", 12)).pack()
entry_filename = tk.Entry(root, width=30)
entry_filename.pack(pady=5)

# Browse button
browse_btn = tk.Button(root, text="Browse", command=browse_save_location)
browse_btn.pack(pady=3)

# Scale
tk.Label(root, text="Select Size:", bg="#e3f2fd", font=("Arial", 12)).pack()
scale_var = tk.IntVar(value=6)
scale_slider = tk.Scale(root, from_=3, to=10, orient=tk.HORIZONTAL,
                        variable=scale_var, bg="#e3f2fd")
scale_slider.pack(pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate QR Code", bg="#2196f3", fg="white",
                         font=("Arial", 12, "bold"), command=generate_qr)
generate_btn.pack(pady=10)

# QR Preview area
qr_label = tk.Label(root, bg="#e3f2fd")
qr_label.pack(pady=10)

root.mainloop()
