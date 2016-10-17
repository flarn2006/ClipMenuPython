#!/usr/bin/python
from Tkinter import *
import sys
import subprocess
import os

bottom_padding = 50

def setClipboard(text):
	p = subprocess.Popen(['xsel', '-ib'], stdin=subprocess.PIPE)
	p.communicate(input=text)

if len(sys.argv) >= 2:
	filename = sys.argv[1]
else:
	filename = os.path.expanduser('~/.config/clipmenu.txt')

try:
	with open(filename) as f:
		items = f.readlines()
except IOError as ex:
	print 'An error occurred while opening file {}:'.format(filename)
	print ex
	sys.exit(1)

# Event handlers

def btnEdit_Click():
	top.destroy()
	subprocess.call(['xdg-open', filename])

def btnClose_Click():
    top.destroy()

def lb_DblClick(e):
	sel = lb.curselection()[0]
	text = items[sel]
	print 'Selected item {}: "{}"'.format(sel, text)
	setClipboard(text)
	top.destroy()

# UI construction

top = Tk()
top.title('ClipMenu')

scr_width = top.winfo_screenwidth()
scr_height = top.winfo_screenheight()
x = scr_width - 400
y = scr_height - 600 - bottom_padding
top.geometry('400x600+{}+{}'.format(x, y))

lb = Listbox(bg='White')
for i in xrange(len(items)):
	items[i] = items[i].rstrip('\r\n')
	lb.insert(i, items[i])

btnEdit = Button(text='Edit List', command=btnEdit_Click)
btnClose = Button(text='Close', command=btnClose_Click)

lb.bind('<Double-1>', lb_DblClick)

lb.grid(row=0, column=0, columnspan=2, sticky=N+S+W+E)
btnEdit.grid(row=1, column=0, sticky=W+E)
btnClose.grid(row=1, column=1, sticky=W+E)

top.grid_rowconfigure(0, weight=1)
top.grid_columnconfigure(0, weight=1)
top.grid_columnconfigure(1, weight=1)

top.mainloop()
