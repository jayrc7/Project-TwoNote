import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import TwoNote as app 
from bintrees import BinaryTree as btree

class Notebook:
    class Page:
        def __init__(self):
            print("page created")

    def __init__(self):
            print("notebook was created")
            self.tree = btree()
            
    def add(self,page):
        print("Page was added")

