from tkinter import *
from tkinter import messagebox
#%%
class gui:
  def __init__(self,p1):
      self.top = Tk()
      self.p1=p1
      self.sma = Button(self.top, text ="sma", command = self.helloCallBack)
      self.sma.pack()
      self.B1 = Button(self.top, text ="Hello", command = self.helloCallBack1)
      self.B1.pack()
      self.B2 = Button(self.top, text ="Hello", command = self.helloCallBack2)
      self.B2.pack()
      self.B3 = Button(self.top, text ="Hello", command = self.helloCallBack3)
      self.B3.pack()
      self.p1=p1
      self.top.mainloop()
  def helloCallBack(self):
      print('B1')
  def helloCallBack1(self):
      print('B1')
  def helloCallBack2(self):
      print('B1')
  def helloCallBack3(self):
      print('B1')
  
      
b=gui(p1)