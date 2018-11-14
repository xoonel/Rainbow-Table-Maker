# Rainbow Table Maker GUI

from tkinter import *

class Application(Frame): 
    def __init__(self, master):
        # Initialize frame.
        super(Application, self).__init__(master)    
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Creates text entry for user defined character set
        self.chr_txt = Text(self, width = 35, height = 5, borderwidth = 1, relief = GROOVE,  wrap = CHAR)
        self.chr_txt.grid(row = 0, column = 1)

        # Select all possible permutations
        self.radbttn1 = Radiobutton(self, text = "All Permuations")
        self.radbttn1.grid()
        self.radbttn1.grid(row = 1, column = 0, columnspan = 1)

        # Select for fixed length
        self.radbttn2 = Radiobutton(self, text = "Fixed Length")
        self.radbttn2.grid()
        self.radbttn2.grid(row = 1, column = 1, columnspan = 1)

        # Select for ranged length
        self.radbttn3 = Radiobutton(self, text = "Ranged Length")
        self.radbttn3.grid()
        self.radbttn3.grid(row = 1, column = 2, columnspan = 1)

        # Select for MD5 hash
        self.chkbttn1 = Checkbutton(self, text = "MD5  ")
        self.chkbttn1.grid()
        self.chkbttn1.grid(row = 2, column = 0, columnspan = 1)

        # Select for SHA1 hash
        self.chkbttn2 = Checkbutton(self, text = "SHA1")
        self.chkbttn2.grid()
        self.chkbttn2.grid(row = 2, column = 1, columnspan = 1)

        # Select for LM hash
        self.chkbttn3 = Checkbutton(self, text = "LM")
        self.chkbttn3.grid()
        self.chkbttn3.grid(row = 2, column = 2, columnspan = 1)

        # Select for NLTM hash
        self.chkbttn4 = Checkbutton(self, text = "NTLM")
        self.chkbttn4.grid()
        self.chkbttn4.grid(row = 3, column = 0, columnspan = 1)

        # Output display for when rainbow table is being calculated
        self.otpt_txt = Text(self, width = 35, height = 5, borderwidth = 1, relief = GROOVE,  wrap = CHAR)
        self.otpt_txt.grid(row = 4, column = 1)

        # Begins computing rainbow table
        self.bttn1 = Button(self, text = "Generate Rainbow Table", width = 20)
        self.bttn1.grid()
        self.bttn1.grid(row = 5, column = 0, columnspan = 1)

        # Saves rainbow table
        self.bttn2 = Button(self, text = "Save Rainbow Table", width = 20)
        self.bttn2.grid()
        self.bttn2.grid(row = 5, column = 1, columnspan = 1)

        # Quits application
        self.bttn3 = Button(self)
        self.bttn3.grid()	
        self.bttn3.configure(text = "Quit", width = 20)
        self.bttn3.grid(row = 5, column = 2, columnspan = 1)

# Main. Keep at bottom so root.mainloop() keeps application window open and app=Application(root) does not return an undefined error.
root = Tk()
root.title("Rainbow-Table-Maker")
root.geometry("675x300")
app = Application(root)
root.mainloop()
