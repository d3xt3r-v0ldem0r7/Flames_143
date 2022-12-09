from cgitb import text
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter.font import BOLD
from tkinter import Tk, Menu
from tkinter.messagebox import showinfo

from setuptools import Command

#------------------------------FLAMES SECTION------------------#
def remove_letter(pl1, pl2):
	for i in range(len(pl1)):
		for j in range(len(pl2)):
			if pl1[i] == pl2[j]:
				c = pl2[j]
				pl1.remove(c)
				pl2.remove(c)
				t_list = pl1 + pl2
				return [t_list, True]
	t_list = pl1 + pl2
	return [t_list, False]

def tell_status() :
		your_name = Player1_field.get().lower().replace(" ", "")
		your_name = list(your_name)
		partner_name = Player2_field.get().lower().replace(" ", "")
		partner_name = list(partner_name)
		flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
		flag = True

		while flag:
			returnval = remove_letter(your_name, partner_name)
			check1 = returnval[0]
			flag = returnval[1]
		total_letters = len(check1)
		
		while len(flames) > 1:
			flindex = total_letters % len(flames) -1
			if flindex >= 0:
				remove1 = flames[flindex + 1:]
				remove2 = flames[: flindex]
				flames = remove1 + remove2
			else:
				flames = flames[:len(flames) -1]
		tempp = f'"{flames[0]}"'
		Status_field.insert(10, tempp)

def clear_all() :
	Player1_field.delete(0, END)
	Player2_field.delete(0, END)
	Status_field.delete(0, END)
	Player1_field.focus_set()

def about():
	abou_t=Tk()
	abou_t.iconbitmap('./icon_.ico')
	abou_t.configure(background = 'white')
	abou_t.geometry("560x565")
	abou_t.title("About")

	lbb1 = Label(abou_t, text = "\nFLAMES_143  --V1.0\n_________________________",
				fg = 'blue', bg='white',bd = 1, anchor = "w",font = ('conlas', 20, 'bold'))
	lbb2 = Label(abou_t, text = "\nVersion 1.0\nCopyright © 2022. All rights reserved.\n\tGNU Genral Public License.\n\nThis program is free software; you can redistribute it \nand/or modify it under the terms of the GNU General\n Public License as published by the Free Software     `\nFoundation;                                                               `\n\nThis program is distributed in the hope that it will be \n  useful, but WITHOUT ANY WARRANTY; without even \n  the implied warranty of MERCHANTABILITY or FITNESS\nFOR A PARTICULAR PURPOSE. See the GNU General\n  Public License for more details.                                     `\nYou should have received a copy of the GNU General \nPublic License along with this program. If not, see \n<https://www.gnu.org/licenses/>.",
				fg = 'black', bg='white',bd = 1, anchor = "w",font = ('conlas', 12, 'bold'))
	lbb1.grid(row=0,column=1)
	lbb2.grid(row=1,column=1)


if __name__ == "__main__" :
	root = Tk()
	root.configure(background = 'white')
	root.iconbitmap('./icon_.ico')
	root.geometry("880x640")
	root.title("Flames Game")

#-----------------------------Menu bar section---------------------------------#
	menubar = Menu(root)
	root.config(menu=menubar)

	file_menu = Menu(menubar, tearoff=0)
	file_menu.add_command(label='Exit', command=root.destroy)

	menubar.add_cascade(label="Menu", menu=file_menu, underline=0)
	help_menu = Menu(menubar, tearoff=0)
	help_menu.add_command(label='About...',command=about)
	menubar.add_cascade(label="Help", menu=help_menu, underline=0)


# ----------------------------Gui section--------------------------------------#
	label1 = Label(root, text = "Your Name     : ",
				fg = 'black', bg='white',bd = 1, anchor = "w",font = ('conlas', 12, 'bold'))
	label2 = Label(root, text = "Partner Name : ",
				fg = 'black', bg='white',bd = 1, anchor = "w",font = ('conlas', 12, 'bold'))

	label1.place(x=260, y=128)
	label2.place(x=260, y=185)

	Player1_field = Entry(root, font = ('arial', 12),bd = 1, insertwidth = 2,fg="blue",
				bg = "#D5D6D4", justify = 'left')
	Player2_field = Entry(root, font = ('arial', 12),bd = 1, insertwidth = 2,fg="blue",
				bg = "#D5D6D4", justify = 'left')
	Status_field = Entry(root, font = ('arial', 20), bd = 0, insertwidth = 2,
				bg = "white",fg='red' ,justify = 'left')
	Player1_field.place(x=450,y=128)
	Player2_field.place(x=450,y=185)
	Status_field.place(x=400,y=230,width=800,height=50)
                    
	lblInfo = Label(root,font = ('helvetica', 20, 'bold'),
		text = "FLAMES",bg="white",fg = "crimson", bd = 10, anchor='w')
	lblInfo.place(x=380, y=35)
	
	button1 = Button(root, text = "calculate", bg = "blue",fg = "white", command =tell_status,
					bd = 0, anchor = "w",font = ('conolas', 10, 'bold'),pady = 10, padx = 170)
	button2 = Button(root, text = "Clear", bg = "red",fg = "white", command = clear_all,
	                bd = 0, anchor = "w",font = ('corbel', 10, 'bold'),pady = 10, padx = 185)
	
	button1.place(x=260,y=290)
	button2.place(x=260,y=350)
	
	lblInfo3 = Label(root, font = ('helvetica', 10, 'bold'),
		text = "\ncreated by iniyavan.\ncopyrights 2022 @ all rights resevered",bg="white",fg = "black",)
	lblInfo3.place(x=300,y=450)

	root.mainloop()

# In[ ]:
print("created by iniyavan")
print("D3XT3R")
