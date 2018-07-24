import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def open_file():
		dialog = Gtk.FileChooserDialog("Open an existing file", None, Gtk.FileChooserAction.OPEN,(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		response = dialog.run()
    
		if response == Gtk.ResponseType.OK:
			filename = dialog.get_filename()
			dialog.destroy()
          
		elif response == Gtk.ResponseType.CANCEL:
			print("Cancel clicked")
			dialog.destroy()

