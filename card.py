from tkinter import *
from tkinter import messagebox
import sys
import re
class Card :
    def __init__(self,root):
        """
        Constructor
        """
        self.root = root 
        self.root.title("Card Validator")
        self.root.geometry("300x230")
        self.root.configure(background = "gray")
        self.root.Label_1 = Label(self.root,text="Welcome\nEnter your card ",font=("Arial",12,"bold"),background="gray")
        self.root.Label_1.pack(pady=10)

        self.root.Text_1 = Text(self.root,width=16,height=1,relief=GROOVE)
        self.root.Text_1.pack(pady=10)

        self.root.Button_1 = Button(self.root,text="Submit",font="bold",width=6,height=2,command= self.getCardID)
        self.root.Button_1.pack(pady=5)

        self.root.Button_2 = Button(self.root,text="Exit",font="bold",width=6,height=2,command=lambda:quit())
        self.root.Button_2.pack()

    def getCardID (self):
        """
        Takes number from textbar and validates with
        functions. If total can divide with 10 and remains 0
        it is a valid card 
        """
        nums = self.root.Text_1.get("1.0",END).strip()
        if not nums.isdigit():
            messagebox.showerror("Warning","Please enter digits")
            return
        self.getEvenNum(nums)
        self.getOddNum(nums)

        cardtype = self.getCardType(nums)
        evenNums = self.getEvenNum(nums)
        oddNums = self.getOddNum(nums)
        total = evenNums + oddNums

        if total % 10 == 0 :
            messagebox.showinfo("Valid","It is valid. "+cardtype)
        else:
            messagebox.showwarning("Warning","It is not valid.")

    def getCardType(self,nums):
        """
        checks card's first number with regex module. Returns value
        with if-else statement

        """
        match = re.search(r'^4',nums)
        if match :
            return "Card type is visa."
        elif re.search(r'^5',nums):
            return "Card type is master card"
        elif re.search(r'^3',nums):
            return "Card type is american express"
        else :
            return "Card type is unknown"

    def getEvenNum(self,nums):
        """
        looks even numbers in card. Reaches with for loop and
        multiply with 2. If the number is two digit,takes as single.
        Finally assings it to temporary variable and returns it.
        """
        result = 0
        for i in range(len(nums)-2, -1, -2):
            num = int(nums[i])
            num *= 2
            if num > 9 :
                num = num % 10 + num // 10 
            result += num
        return result

    def getOddNum(self,nums):
        """
        Looks for odd numbers in card. Reaches with for loop.
        assigns each 'i' to temporary variable and returns temporary
        variable.
        """
        result = 0
        for i in range(len(nums)-1,-1,-2):
            num = int(nums[i])
            result += num
        return result

if __name__ == "__main__":
    root = Tk ()
    Card(root)
    root.mainloop()