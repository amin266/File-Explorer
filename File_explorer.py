from tkinter import *
#from tkinter import filedialog
from tkinter import filedialog as fd

def browseFiles():
	filename = fd.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*")))

	label_file_explorer.configure(text="File Opened: "+filename)

window = Tk()

#window.title("Run File")
window.title("File Explorer")
window.title("Open File")
window.geometry("705x850")

window.config(background = "skyblue")


label_file_explorer = Label(window,
							text = "File Explorer using Tkinter",
							width = 100, height = 4,
							fg = "blue")

#button_runfile = Button(window,
#                        text = "Run opend File",
#                        command = browseFiles)

button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(window,
					text = "Exit",
					command = exit)


label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)

window.mainloop()
