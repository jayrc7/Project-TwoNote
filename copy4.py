import gi
import TextSet as text_set
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk, Pango

class MainWindow(Gtk.Window):                   
	def __init__(self):
		Gtk.Window.__init__(self, title = "TwoNote")
		# size of window
		self.set_default_size(1920,1080)
		#self.set_border_width(10)


		## toolkit menu bar
		header = Gtk.HeaderBar()
		header.set_show_close_button(True)
		header.props.title = "TwoNote"
		header.set_name("header")
		self.set_titlebar(header)
		mb = Gtk.MenuBar()
		mb.set_name("menu")


		## left vbox for notebook name 
		vboxLeft = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
		vboxLeft.set_homogeneous(False)

		## frame for left vbox
		leftFrame = Gtk.Frame()
		leftFrame.add(vboxLeft)
		leftFrame.set_hexpand(True)
		leftFrame.set_vexpand(True)
		leftFrame.set_name("leftFrame")

		#right vbox for notes 
		vboxRight = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
		vboxRight.set_homogeneous(False)
		container = Gtk.ScrolledWindow()
		container.set_name("rightFrame")
		mytext = text_set.TextSet()
  
		container.add(mytext)
		vboxRight.pack_start(container, True, True, 0)

		#frame for right box
		rightFrame = Gtk.Frame()
		rightFrame.add(vboxRight)
		rightFrame.set_hexpand(True)
		rightFrame.set_vexpand(True)

		#creates grid and adds frames
		grid = Gtk.Grid()
		grid.attach(leftFrame,0,0,2,30)
		toolbar = Gtk.Toolbar()
		grid.attach(toolbar, 3, 0, 5, 1)
		grid.attach_next_to(rightFrame, leftFrame, Gtk.PositionType.RIGHT, 7,30)

		self.add(grid)


		#Create a box of linked items
		box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)

		# says whatever we put in this box, theyre going to be together
		Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        
		button_bold = Gtk.ToggleToolButton()
		button_bold.set_icon_name("format-text-bold-symbolic")
		toolbar.insert(button_bold, 0)

		button_italic = Gtk.ToggleToolButton()
		button_italic.set_icon_name("format-text-italic-symbolic")
		toolbar.insert(button_italic, 1)

		button_underline = Gtk.ToggleToolButton()

		button_underline.set_icon_name("format-text-underline-symbolic")
		toolbar.insert(button_underline, 2)

		button_bold.connect("clicked", mytext.on_button_clicked, "Bold")
		button_italic.connect("clicked", mytext.on_button_clicked, "Italic")
		button_underline.connect("clicked", mytext.on_button_clicked, "Underline")
		
		
window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

