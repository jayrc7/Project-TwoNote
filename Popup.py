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
            self.entry.set_max_length(20)
            area.add(self.entry)

        else:
            self.entry = Gtk.Entry()
            self.entry.set_text("Notebook Name")
            self.entry.set_max_length(13)
            self.entry2 = Gtk.Entry()
            self.entry2.set_text("First Page")
            self.entry2.set_max_length(20)
            area.add(self.entry)
            area.add(self.entry2)

                
                
        self.show_all()

class Rename(Gtk.Dialog):
    def __init__(self, parent, notebook_name, page_name):

        Gtk.Dialog.__init__(self, "Rename", parent, Gtk.DialogFlags.MODAL, (
            "Cancel", Gtk.ResponseType.CANCEL, 
            Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(200, 100)
        self.set_border_width(30)
                
        area = self.get_content_area()
            
        #content
        self.notebook = Gtk.Notebook()
        self.entry_notebook = Gtk.Entry()
        self.entry_notebook.set_text(notebook_name)
        self.entry_notebook.set_max_length(13)
        self.notebook.insert_page(self.entry_notebook, Gtk.Label("Notebook"), -1)

        self.entry_page = Gtk.Entry()
        self.entry_page.set_text(page_name)
        self.entry_page.set_max_length(20)
        self.notebook.insert_page(self.entry_page, Gtk.Label("Page"), -1)



        area.add(self.notebook)
        area.show_all()

class Delete(Gtk.Dialog):
    def __init__(self, parent, notebook, name):
            
        Gtk.Dialog.__init__(self, "Delete", parent, Gtk.DialogFlags.MODAL, (
            "Cancel", Gtk.ResponseType.CANCEL, 
            Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(300,225)
        self.set_border_width(60)
        self.set_resizable(True)

        area = self.get_content_area()
                                    
        #content
        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(20)
        self.grid.set_column_spacing(60)
          
        self.check_buttons = []
        
        ''' 
        self.box = Gtk.ListBox()
        self.box.set_selection_mode(Gtk.SelectionMode.NONE)
        for i in range(len(notebook.pages)):
           row = Gtk.ListBoxRow()
           print(notebook.pages[i])
           box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 100)
           row.add(box)
           label = Gtk.Label(notebook.pages[i])
           self.page_button = Gtk.CheckButton()
           self.check_buttons.append(self.page_button)
           box.pack_start(label, True, True, 0)
           box.pack_start(self.page_button, True, True, 0)
           self.box.add(row)
           self.box.show_all()
        '''

        self.box1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        self.box2 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)


        label = Gtk.Label(name)
        self.button = Gtk.CheckButton()
        self.check_buttons.append(self.button)

        self.box1.pack_start(label, True, True, 0)
        self.box2.pack_start(self.button, True, True, 0)

        for i in range(len(notebook.pages)):
           label = Gtk.Label(notebook.pages[i])
           self.box1.pack_start(label, True, True, 0)

           self.button = Gtk.CheckButton()
           self.check_buttons.append(self.button)
           self.box2.pack_start(self.button, True, True, 0)

        label = Gtk.Label('Selecting "OK" Without Checking Any Boxes Will Only Delete Current Page. \n Deleting Notebook Will Delete Pages as Well.')
        self.grid.attach(self.box1, 2, 2, 2, 2)
        self.grid.attach_next_to(self.box2, self.box1, Gtk.PositionType.RIGHT, 2, 2)
        self.grid.attach_next_to(label, self.box2, Gtk.PositionType.BOTTOM, 2, 2)
        self.grid.show_all()
   
        area.add(self.grid)
        area.show_all()

                


