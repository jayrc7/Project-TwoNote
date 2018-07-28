import gi
import TextSet as text_set
import Menu_Button as menu_button
import sidebar_menu as sidebar
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.ApplicationWindow):
	def __init__(self):
		Gtk.Window.__init__(self, title = "TwoNote")
        # size of window
		self.set_default_size(1920,1080)

		self.header = Gtk.HeaderBar()
		self.header.set_show_close_button(True)
		self.header.props.title = "TwoNote"
		self.set_titlebar(self.header)
		
       
		# men button on right
		self.menuButton = Gtk.MenuButton()
		# drop menu
		self.menu = menu_button.NoteMenu()
		self.menuButton.set_menu_model(self.menu)
    
		self.header.pack_start(self.menuButton)
        	
		## left vbox for notebook name 
		self.vboxLeft = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
		self.vboxLeft.set_homogeneous(False)

		## frame for left vbox
		self.leftFrame = sidebar.SidebarWindow()
		self.leftFrame.set_hexpand(True)
		self.leftFrame.set_vexpand(True)
		
		## right vbox for notes 
		self.vboxRight = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
		self.vboxRight.set_homogeneous(False)
		self.scroll_container = Gtk.ScrolledWindow()
		self.mytext = text_set.TextSet()
		self.scroll_container.add(self.mytext)
		self.vboxRight.pack_start(self.scroll_container, True, True, 0)

		# frame for right box
		self.rightFrame = Gtk.Frame()
		self.rightFrame.add(self.vboxRight)
		self.rightFrame.set_hexpand(True)
		self.rightFrame.set_vexpand(True)

		# creates grid and adds frames
		self.grid = Gtk.Grid()
		self.grid.attach(self.leftFrame,0,0,2,30)
		self.toolbar = Gtk.Toolbar()
		self.grid.attach(self.toolbar, 3, 0, 5, 1)
		self.grid.attach_next_to(self.rightFrame, self.leftFrame, Gtk.PositionType.RIGHT, 7,30)
		
		 
		self.button_bold = Gtk.ToggleToolButton()
		self.button_bold.set_icon_name("format-text-bold-symbolic")
		self.toolbar.insert(self.button_bold, 0)

		self.button_italic = Gtk.ToggleToolButton()
		self.button_italic.set_icon_name("format-text-italic-symbolic")
		self.toolbar.insert(self.button_italic, 1)

		self.button_underline = Gtk.ToggleToolButton()

		self.button_underline.set_icon_name("format-text-underline-symbolic")
		self.toolbar.insert(self.button_underline, 2)

		self.button_bold.connect("clicked", self.mytext.on_button_clicked, "Bold")
		self.button_italic.connect("clicked", self.mytext.on_button_clicked, "Italic")
		self.button_underline.connect("clicked", self.mytext.on_button_clicked, "Underline")

      


		self.add(self.grid)


		# Create a box of linked items
		self.box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)

		# says whatever we put in this box, theyre going to be together
		Gtk.StyleContext.add_class(self.box.get_style_context(), "linked")

		# left arrow
		self.leftArrow = Gtk.Button()
		self.leftArrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
		self.box.add(self.leftArrow)
      
		self.header.pack_start(self.box)
		
		Gio.SimpleActionGroup.__init__(self)
		self.new_action = Gio.SimpleAction.new("new", None)
		self.new_action.connect("activate", self.new_clicked)
		self.add_action(self.new_action)
		
		self.new_book_action = Gio.SimpleAction.new("new_notebook", None)
		self.new_book_action.connect("activate", self.new_book_clicked)
		self.add_action(self.new_book_action)
		
		self.open_action = Gio.SimpleAction.new("open", None)
		self.open_action.connect("activate", self.open_clicked)
		self.add_action(self.open_action)
		
		self.save_action = Gio.SimpleAction.new("save", None)
		self.save_action.connect("activate", self.save_clicked)
		self.add_action(self.save_action)
		
		self.save_as_action = Gio.SimpleAction.new("save_as", None)
		self.save_as_action.connect("activate", self.save_as_clicked)
		self.add_action(self.save_as_action)
		
		self.settings_action = Gio.SimpleAction.new("settings", None)
		self.settings_action.connect("activate", self.settings_clicked)
		self.add_action(self.settings_action)
		self.connect('destroy', Gtk.main_quit)
		self.show_all()  
		
		
	def open_clicked(self, action, none):
		menu_button.open_file(self)
	
	def new_clicked(self, action, none):
		print("new")
	
	def new_book_clicked(self, action, none):
		print("new notebook")
		
	def save_clicked(self, action, none):
		menu_button.save_file(self, self.mytext)
    
	def save_as_clicked(self, action, none):
		print("save as")  
    
	def settings_clicked(self, action, none):
		print("settings")
		
		  

	

if __name__ == '__main__':
    win = MainWindow()
    Gtk.main()

