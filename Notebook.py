import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import TwoNote as app 
from bintrees import BinaryTree as btree
import BinaryTree as btree

class Notebook:
    def __init__(self, string):
        self.NotebookName = string
        self.tree = btree.BinaryTree()
        self.pages = []
            
    def add(self,page):
        self.tree.insert(page)
        self.pages.append(page.val)

    def list_pages(self):
        if(len(self.pages) == 0):
            print "[]"

        else:
            for i in range(len(self.pages)):
                print(self.pages[i])

    def add_notebook_gui(self, layout, name):
        layout.insert_page(Gtk.ListBox(), Gtk.Label(name), -1)
        layout.show_all()
    
    def notebook_iterator(self):
        page_list = []
        self.iterator = btree.BinaryTree.Iterator(self.tree)
        for i in range(self.tree.size):
            print(self.iterator.next())

    
    ##makes newly made notebook tab to current 
    def set_current_section(self, layout):
        layout.set_current_page(-1)
        current = layout.get_current_page()
        currentpage = layout.get_nth_page(current)
        return currentpage

    def add_page_gui(self, page, name):
        row = Gtk.ListBoxRow()
        toggleButton = Gtk.ToggleButton(label = name)

        toggleButton.set_active(True)
        box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 100)
        row.add(box)
        box.pack_start(toggleButton, True, True, 0)
        page.add(row)

    def get_current_section(self, layout):
        return layout.get_nth_page(layout.get_current_page())

        
    




