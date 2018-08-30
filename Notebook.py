import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import BinaryTree as btree


class Notebook:
    def __init__(self, string, win):
        self.sidebar = win
        self.NotebookName = string
        self.tree = btree.BinaryTree()
        self.pages = []
        self.buttons = []
        self.boolean = True
        self.pressed = False

    def add(self, page):
        self.tree.insert(page)
        self.pages.append(page.val)

    def list_pages(self):
        if (len(self.pages) == 0):
            print("[]")

        else:
            for i in range(len(self.pages)):
                print(self.pages[i])

    def add_notebook_gui(self, layout, name):
        layout.insert_page(Gtk.ListBox(), Gtk.Label(name), -1)
        layout.show_all()

    def notebook_iterator(self):
        page_list = []
        self.iterator = btree.BinaryTree.Iterator(self.tree)
        #for i in range(self.tree.size):
            #print(self.iterator.next())

    ##makes newly made notebook tab to current and returns listbox(page)
    def set_current_section(self, layout):
        layout.set_current_page(-1)
        current = layout.get_current_page()
        currentpage = layout.get_nth_page(current)
        return currentpage

    def add_page_gui(self, page, name):
        row = Gtk.ListBoxRow()
        self.name = name
        toggleButton = Gtk.ToggleButton(label=name)
        toggleButton.connect("clicked", self.open_page, self)
        self.buttons.append(toggleButton)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row.add(box)
        box.pack_start(toggleButton, True, True, 0)
        page.add(row)

        toggleButton.set_active(True)

        if(self.boolean):
            self.activate(toggleButton) 
        

    # returns listbox(page),not notebook tab
    def get_current_page(self, layout):
        return layout.get_nth_page(layout.get_current_page())

    def set_name(self, name):
        self.NotebookName = name

    def get_name(self):
        return self.NotebookName

    def get_Children(self):
        return self.pages

    def get_child_at_index(self, num):
        return self.pages[num]

    def set_page_name(self, previous_name, new_name):
        for i in range(len(self.pages)):
            if (self.pages[i] == previous_name):
                widget = self.buttons[i]
                widget.set_label(new_name)
                self.pages[i] = new_name

    def contains_page(self, name):
        if (self.tree.find(name)):
            return True

        else:
            return False

    def open_page(signal, button, notebook):

        if(len(notebook.sidebar.notebook_list) == 1 and notebook.boolean):
            notebook.sidebar.active_button = button
            notebook.sidebar.active_button.set_active(True)
            notebook.sidebar.initial_button = False
            print("True")
            notebook.boolean = False

        else:
            print("False")
            notebook.sidebar.previous_button = notebook.sidebar.active_button
            notebook.sidebar.previous_button.set_active(False)

            notebook.sidebar.active_button = button
            notebook.boolean = False

    def activate(self, button

        #if(notebook.sidebar.active_button == notebook.sidebar.previous_button):
            #notebook.sidebar.active_button.set_active(True)


    #def remove_page(self, buttons):
         
