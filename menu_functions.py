import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

filename = "Untitled"
def open_file(window):
		open_dialog = Gtk.FileChooserDialog("Open an existing file", window, Gtk.FileChooserAction.OPEN,(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		open_response = open_dialog.run()
    
		if open_response == Gtk.ResponseType.OK:
			filename = open_dialog.get_filename()
			dialog.destroy()
          
		elif open_response == Gtk.ResponseType.CANCEL:
			print("Cancel clicked")
			open_dialog.destroy()

def save_file(window, widget):
		print('saveButton clicked')
		savechooser = Gtk.FileChooserDialog('Save File', window, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
		allfilter = Gtk.FileFilter()
		allfilter.set_name('All files')
		allfilter.add_pattern('*')
		savechooser.add_filter(allfilter)

		txtFilter = Gtk.FileFilter()
		txtFilter.set_name('Text file')
		txtFilter.add_pattern('*.txt')
		savechooser.add_filter(txtFilter)
		response = savechooser.run()
        
		if response == Gtk.ResponseType.OK:
			filename = savechooser.get_filename()
			print(filename, 'selected.')

            
			buf = widget.get_buffer()
			text = buf.get_text(buf.get_start_iter(), buf.get_end_iter(), True)
			try:
				open(filename, 'w').write(text)
			except SomeError as e:
				print('Could not save %s: %s' % (filename, err))
			savechooser.destroy()
        	
		elif response == Gtk.ResponseType.CANCEL:
			print('Closed, file not saved.')
			savechooser.destroy()
        
        
        
        
        
        
        
