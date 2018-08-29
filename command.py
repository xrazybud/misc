#!/usr/bin/env python3

import gi
import os
import os.path
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

	def load(self):
		ret = {}
		try:
			fset = open(os.path.expanduser("~/.cOM"), "r")
			ret["path"] = fset.readline().strip()
			ret["command"] = fset.readline().strip()
			#return ret
		except:
			ret["path"] = "path"
			ret["command"] = "command"

		self.cmdtxt = ret["command"] + "\n"
		self.pathxt = ret["path"]  + "\n"

		return ret


	def __init__(self):
		Gtk.Window.__init__(self, title="Command clicker")

		grid = Gtk.Grid()
		self.add(grid)

		self.button = Gtk.Button(label="RUN")
		self.button.connect("clicked", self.on_button_clicked)

		self.label = Gtk.Label(label="LOPL", angle=30, halign=Gtk.Align.END)

		self.command = Gtk.Entry(text="command")
		self.command.set_max_width_chars(100)
		self.path = Gtk.Entry(text="path")

		grid.add(self.button)
		grid.attach_next_to(self.label, self.button, Gtk.PositionType.RIGHT, 1, 1)
		grid.attach_next_to(self.command, self.button, Gtk.PositionType.TOP, 1, 1)
		grid.attach_next_to(self.path, self.command, Gtk.PositionType.TOP, 1, 1)

		stuff = self.load()
		self.path.set_text(stuff["path"])
		self.command.set_text(stuff["command"])

	def on_button_clicked(self, widget):
		os.system("cd " + self.path.get_text() + "; " + self.command.get_text() )
		self.cmdtxt = self.command.get_text() + '\n'
		self.pathxt = self.path.get_text() + '\n'

	def close(self):
		#super().close()
		#save("~/.cOM", path=win.path.get_text(), command=win.command.get_text() )
		try:
			cfile = open(os.path.expanduser("~/.cOM"), "w")
			cfile.write(self.pathxt)
			cfile.write(self.cmdtxt)
		except:
			print("unable to save file")

	#Gtk.main_quit()

win = MyWindow()
win.connect("delete-event", Gtk.main_quit )
win.show_all()
win.set_keep_above(True)
Gtk.main()
win.close()
#print("heya")
