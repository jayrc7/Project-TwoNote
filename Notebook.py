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

