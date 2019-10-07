import Tkinter
import tkMessageBox

#%%
class gui:
  def __init__(self):
      self.top = Tkinter.Tk()
      self.B = Tkinter.Button(top, text ="Hello", command = self.helloCallBack)
      self.B.pack()
      self.top.mainloop()
  def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

