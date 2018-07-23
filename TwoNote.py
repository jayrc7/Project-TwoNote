import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.Window): 
   def __init__(self):
      Gtk.Window.__init__(self, title = "TwoNote")
      # size of window
      self.set_default_size(1920,1080)
      #self.set_border_width(10)
	    
      header = Gtk.HeaderBar()
      header.set_show_close_button(True)
      header.props.title = "TwoNote"
      self.set_titlebar(header)
      
      # men button on right
      menuButton = Gtk.MenuButton()
      
      # drop menu
      menu = Gio.Menu()
      menu.append("New", "app.new")
      menu.append("Save", "app.save")
      menu.append("Open", "app.open")

      menu.append("Undo", "app.undo")
      menu.append("Redo", "app.redo")

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
      
      # adds left frame to window

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



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

