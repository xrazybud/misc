#!/usr/bin/env python3

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
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

	def on_button_clicked(self, widget):
		os.system("cd " + self.path.get_text() + "; " + self.command.get_text() )


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
win.set_keep_above(True)
Gtk.main()

