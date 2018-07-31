import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class SidebarWindow(Gtk.Frame):
	def __init__(self):
		Gtk.Frame.__init__(self)

		hbox = Gtk.Box(spacing=6)
		self.add(hbox)

		listbox = Gtk.ListBox()
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		hbox.pack_start(listbox, True, True, 0)

		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, True, True, 0)

		label1 = Gtk.Label("Automatic Data & Time", xalign=0)
		label2 = Gtk.Label("Requires internet access", xalign=0)
		vbox.pack_start(label1, True, True, 0)
		vbox.pack_start(label2, True, True, 0)

		listbox.add(row)

		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		row.add(hbox)
		label = Gtk.Label("Enable Automatic Update", xalign=0)
		hbox.pack_start(label, True, True, 0)
      
		listbox.add(row)

		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		row.add(hbox)
		label = Gtk.Label("Date Format", xalign=0)
		hbox.pack_start(label, True, True, 0)
      
		listbox.add(row)


