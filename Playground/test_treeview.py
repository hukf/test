from tkinter import *
from tkinter.ttk import *
class AddTreeView:
    def __init__(self, parent,symbs):
        self.tree=ttk.Treeview(parent)
        for symb in symbs:
           tree.insert("" , "end",  text=symb)
        tree.bind("<Double-1>", self.OnDoubleClick)
    def OnDoubleClick(self,event):
        item = self.tree.selection()[0]
        print("you clicked on", self.tree.item(item,"text"))
