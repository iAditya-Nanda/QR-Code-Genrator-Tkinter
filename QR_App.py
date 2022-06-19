import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import qrcode

# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Qr Code Generator')

# store qr text and file name
qrtxt = tk.StringVar()
file_name = tk.StringVar()


def save_clicked():
    img = qrcode.make(qr_entry.get())
    name = filename_entry.get() + ".png"
    img.save(name)
    showinfo(title="Qr Code Generator", message="Qr is saved successfully")
    img.show()

# QR frame
qr = ttk.Frame(root)
qr.pack(padx=10, pady=10, fill='x', expand=True)


# qr
qr_label = ttk.Label(qr, text="Enter QR code text:")
qr_label.pack(fill='x', expand=True)

qr_entry = ttk.Entry(qr, textvariable=qrtxt)
qr_entry.pack(fill='x', expand=True)
qr_entry.focus()

# filename
filename_label = ttk.Label(qr, text="Enter File Name:")
filename_label.pack(fill='x', expand=True)

filename_entry = ttk.Entry(qr, textvariable=file_name)
filename_entry.pack(fill='x', expand=True)

# save button
save_button = ttk.Button(qr, text="Save", command=save_clicked)
save_button.pack(fill='x', expand=True, pady=10)

root.mainloop()