from tkinter import *
class Card :
    def __init__(self,root):
        """
        Constructor
        """
        self.root = root 
        self.root.geometry("300x200")
        self.root.Label_1 = Label(self.root,text="Welcome\nEnter your card :",font=("Arial",12))
        self.root.Label_1.pack()

        self.root.Text_1 = Text(self.root,width=11,height=1,relief=GROOVE)
        self.root.Text_1.pack()

        self.root.Button_1 = Button(self.root,text="Submit",width=6,height=2,command= self.getCardID)
        self.root.Button_1.pack()
    
    def getCardID (self):
        nums = self.root.Text_1.get("1.0",END)
        print(nums)



if __name__ == "__main__":
    root = Tk ()
    Card(root)
    root.mainloop()