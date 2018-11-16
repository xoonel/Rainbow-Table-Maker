from tkinter import *
 
master = Tk()

def RUNIT():
    import itertools
    chrs = 'XYZ'

    cnt = 0

    # Creates the rainbow table text document; overwrites previous ones if program is run.
    rnbwtbl_file = open("rainbow_table.txt", "w")

    while cnt <= len(chrs):

        for i in itertools.product(chrs, repeat=cnt):
            # Prints all possible character permutations in the shell.
            print(''.join(i)) 
            # Concurrently writes all possible possible character permutations to text document () contiguously with no formatting.
            rnbwtbl_file.write(''.join(i))
        cnt = cnt+1

# Creates text entry for user defined character set.
chr_txt = Text(master, width = 35, height = 5, borderwidth = 1, relief = GROOVE,  wrap = CHAR)
chr_txt.grid(row = 0, column = 1)

# Next three radio buttons used to select how many iterations/permutations of password possiblities will be calculated.
radbttn1 = Radiobutton(master, text = "All Permuations")
radbttn1.grid(row = 1, column = 0, columnspan = 1)

radbttn2 = Radiobutton(master, text = "Fixed Length")
radbttn2.grid(row = 1, column = 1, columnspan = 1)

radbttn3 = Radiobutton(master, text = "Ranged Length")
radbttn3.grid(row = 1, column = 2, columnspan = 1)

# Next four check boxes used to select which hash algorithms to calculate for each password
chkbttn1 = Checkbutton(master, text = "MD5  ")
chkbttn1.grid(row = 2, column = 0, columnspan = 1)

chkbttn2 = Checkbutton(master, text = "SHA1")
chkbttn2.grid(row = 2, column = 1, columnspan = 1)

chkbttn3 = Checkbutton(master, text = "LM")
chkbttn3.grid(row = 2, column = 2, columnspan = 1)

chkbttn4 = Checkbutton(master, text = "NTLM")
chkbttn4.grid(row = 3, column = 0, columnspan = 1)

# Next three are the action buttons that Start the calculation, save to the output or quit the application.
bttn1 = Button(master, text = "Generate Rainbow Table", width = 20, command = RUNIT)
bttn1.grid(row = 5, column = 0, columnspan = 1)

bttn2 = Button(master, text = "Save Rainbow Table", width = 20)
bttn2.grid(row = 5, column = 1, columnspan = 1)

bttn3 = Button(master, text = "Quit", width = 20)
bttn3.grid(row = 5, column = 2, columnspan = 1)

mainloop()
