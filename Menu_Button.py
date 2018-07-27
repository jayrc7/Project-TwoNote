import gi
import menu_functions as menu_func
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class NoteMenu(Gio.Menu):
	def __init__(self):
		Gio.Menu.__init__(self)
		self.new_item = Gio.MenuItem.new('New', 'win.new')
		self.new_book_item = Gio.MenuItem.new('New Notebook', 'win.new_notebook')
		self.open_item = Gio.MenuItem.new('Open', 'win.open')
		self.save_item = Gio.MenuItem.new('Save', 'win.save')
		self.save_as_item = Gio.MenuItem.new('Save as', 'win.save_as')
		self.settings_item = Gio.MenuItem.new('Preferences', 'win.settings')
		
		# appends items to drop down menu
		self.append_item(self.new_item)
		self.append_item(self.new_book_item)
		self.append_item(self.open_item)
		self.append_item(self.save_item)
		self.append_item(self.save_as_item)
		self.append_item(self.settings_item)
'''	
class NoteActionGroup(Gio.SimpleActionGroup):
	def __init__(self):
		Gio.SimpleActionGroup.__init__(self)
		self.new_action = Gio.SimpleAction.new("new", None)
		self.new_action.connect("activate", self.new_clicked)
		self.insert(self.new_action)
		
		self.new_book_action = Gio.SimpleAction.new("new_notebook", None)
		self.new_book_action.connect("activate", self.new_book_clicked)
		self.insert(self.new_book_action)
		
		self.open_action = Gio.SimpleAction.new("open", None)
		self.open_action.connect("activate", self.open_clicked)
		self.insert(self.open_action)
		
		self.save_action = Gio.SimpleAction.new("save", None)
		self.save_action.connect("activate", self.save_clicked)
		self.insert(self.save_action)
		
		self.save_as_action = Gio.SimpleAction.new("save_as", None)
		self.save_as_action.connect("activate", self.save_as_clicked)
		self.insert(self.save_as_action)
		
		self.settings_action = Gio.SimpleAction.new("settings", None)
		self.settings_action.connect("activate", self.settings_clicked)
		self.insert(self.settings_action)
		
		
		
	def open_clicked(self, action, none):
		menu_func.open_file(self)
	
	def new_clicked(self, action, none):
		print("new")
		
	def new_book_clicked(self, action, none):
		print("new notebook")
		
	def save_clicked(self, action, none):
		menu_func.save_file(self, self.text)
    
	def save_as_clicked(self, action, none):
		print("save as")  
    
	def settings_clicked(self, action, none):
		print("settings")	

			
'''
