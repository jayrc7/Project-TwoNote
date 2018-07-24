import gi
import menu_functions as menu_func
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.ApplicationWindow): 
	def __init__(self):
		Gtk.Window.__init__(self, title = "TwoNote")
		# size of window
		self.set_default_size(1920,1080)
		#self.set_border_width(10)
	    
		header = Gtk.HeaderBar()
		header.set_show_close_button(True)
		header.props.title = "TwoNote"
		self.set_titlebar(header)
		
		#Actions for Menu Button drop down
		new_action = Gio.SimpleAction.new("new", None)
		new_action.connect("activate", self.new_clicked)
		self.add_action(new_action)
		
		new_book_action = Gio.SimpleAction.new("new_notebook", None)
		new_book_action.connect("activate", self.new_book_clicked)
		self.add_action(new_book_action)
		
		open_action = Gio.SimpleAction.new("open", None)
		open_action.connect("activate", self.open_clicked)
		self.add_action(open_action)
		
		save_action = Gio.SimpleAction.new("save", None)
		save_action.connect("activate", self.save_clicked)
		self.add_action(save_action)
		
		save_as_action = Gio.SimpleAction.new("save_as", None)
		save_as_action.connect("activate", self.save_as_clicked)
		self.add_action(save_as_action)
		
		settings_action = Gio.SimpleAction.new("settings", None)
		settings_action.connect("activate", self.settings_clicked)
		self.add_action(settings_action)
		
		# men button on right
		menuButton = Gtk.MenuButton()
      
		# drop menu
		menu = Gio.Menu.new()
		
		# Creates items for drop Down Menu
		new_item = Gio.MenuItem.new('New', 'win.new')
		new_book_item = Gio.MenuItem.new('New Notebook', 'win.new_notebook')
		open_item = Gio.MenuItem.new('Open', 'win.open')
		save_item = Gio.MenuItem.new('Save', 'win.save')
		save_as_item = Gio.MenuItem.new('Save as', 'win.save_as')
		settings_item = Gio.MenuItem.new('Preferences', 'win.settings')
		
		# appends items to drop down menu
		menu.append_item(new_item)
		menu.append_item(new_book_item)
		menu.append_item(open_item)
		menu.append_item(save_item)
		menu.append_item(save_as_item)
		menu.append_item(settings_item)

		menuButton.set_menu_model(menu)
    
		header.pack_start(menuButton)
        	
		## left vbox for notebook name 
		vboxLeft = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
		vboxLeft.set_homogeneous(False)

		## frame for left vbox
		leftFrame = Gtk.Frame()
		leftFrame.add(vboxLeft)
		leftFrame.set_hexpand(True)
		leftFrame.set_vexpand(True)
		
		## right vbox for notes 
		vboxRight = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
		vboxRight.set_homogeneous(False)
		container = Gtk.ScrolledWindow()
		text = Gtk.TextView()
		text.set_indent(10)
		text.set_top_margin(20)
		text.set_left_margin(20)
		container.add(text)
		vboxRight.pack_start(container, True, True, 0)

		# frame for right box
		rightFrame = Gtk.Frame()
		rightFrame.add(vboxRight)
		rightFrame.set_hexpand(True)
		rightFrame.set_vexpand(True)

		# creates grid and adds frames
		grid = Gtk.Grid()
		grid.attach(leftFrame,0,0,2,10)
		grid.attach_next_to(rightFrame, leftFrame, Gtk.PositionType.RIGHT, 7,10)

		self.add(grid)


		# Create a box of linked items
		box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)

		# says whatever we put in this box, theyre going to be together
		Gtk.StyleContext.add_class(box.get_style_context(), "linked")

		# left arrow
		leftArrow = Gtk.Button()
		leftArrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
		box.add(leftArrow)
      
		header.pack_start(box)
		
		self.connect('destroy', Gtk.main_quit)
		self.show_all()
		
	# Functions that call functions for Menu Button from menu_functions.py
	def open_clicked(self, action, none):
		menu_func.open_file()
	
	def new_clicked(self, action, none):
		print("new")
		
	def new_book_clicked(self, action, none):
		print("new notebook")
		
	def save_clicked(self, action, none):
		print("save")	
    
	def save_as_clicked(self, action, none):
		print("save as")  
    
	def settings_clicked(self, action, none):
		print("settings")	    

	

if __name__ == '__main__':
    win = MainWindow()
    Gtk.main()

