import gi
import TwoNote as note
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PopUp(Gtk.Dialog):
        
        def __init__(self, parent,boolean):
                
                if(boolean == True):
                    name = "New Page"

                else:
                    name = "New NoteBook"


                Gtk.Dialog.__init__(self, name, parent, Gtk.DialogFlags.MODAL, (
                    "Cancel", Gtk.ResponseType.CANCEL, 
                     Gtk.STOCK_OK, Gtk.ResponseType.OK))
                self.set_default_size(200, 100)
                self.set_border_width(30)
                
                area = self.get_content_area()

                if(boolean):
                    self.entry = Gtk.Entry()
                    self.entry.set_text("Page Name")
                    area.add(self.entry)

                else:
                    self.entry = Gtk.Entry()
                    self.entry.set_text("Notebook Name")
                    self.entry2 = Gtk.Entry()
                    self.entry2.set_text("First Page")
                    area.add(self.entry)
                    area.add(self.entry2)

                
                
                self.show_all()
                



