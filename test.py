from tkinter import *
import webbrowser

root = Tk()
root.title("Smart Search")
root.geometry("400x300")
root.configure(bg="#1e1e1e") 

def on_focus_in(event):
    if search_entry.get() == "Type URL or Search...":
        search_entry.delete(0, "end")
        search_entry.config(fg="white")

def on_focus_out(event):
    if search_entry.get() == "":
        search_entry.insert(0, "Type URL or Search...")
        search_entry.config(fg="grey")

def search(event=None):
    text = search_entry.get()

    if text == "" or text == "Type URL or Search...":
        return
    
    if "." in text and not text.startswith("http"):
        text = "https://" + text

    webbrowser.open(text if text.startswith("http") else f"https://www.google.com/search?q={text}")

title_label = Label(root, text="Smart Search", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#00c8ff")
title_label.pack(pady=20)

search_entry = Entry(root, width=35, font=("Arial", 14), bg="#2d2d2d", fg="grey",
                     justify="center", bd=2, relief="flat")
search_entry.pack(pady=10)
search_entry.insert(0, "Type URL or Search...")

search_entry.bind("<FocusIn>", on_focus_in)
search_entry.bind("<FocusOut>", on_focus_out)

root.bind("<Return>", search)

search_button = Button(root, text="Search", command=search,font=("Arial", 12, "bold"), bg="#00c8ff", fg="black", activebackground="#009ec7", activeforeground="white",
 bd=0, relief="flat", padx=20, pady=8)
search_button.pack(pady=15)

footer_label = Label(root, text="Made with ❤️", bg="#1e1e1e", fg="#777777", font=("Arial", 10))
footer_label.pack(side="bottom", pady=10)

root.mainloop()