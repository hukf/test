import tkinter as tk

i = 0
def text_mod(name):
    btn['text'] =name  # the global object that is modified
  
root = tk.Tk()

btn = tk.Button(root, text="My Button",command=lambda: text_mod('test'))


btn.pack(fill='both', expand=True)

root.mainloop()