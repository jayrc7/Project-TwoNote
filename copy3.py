import gi, MenuManager
import call
import funct as myText
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk, Pango

class MainWindow(Gtk.Window):                   
    def __init__(self, myText):
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

        css =  '''
            #menu{ background: Turquoise;}
            #label {color: black;}
            #header {background: DodgerBlue;}
            #leftFrame {background: Silver;}
            #rightFrame{background: White;}
    
        '''

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)  

 
      
        #men button on right
        #menuButton = Gtk.MenuButton()
      
        #drop menu
        #menu = Gio.Menu()
      
        #menu.append("New", "app.new")
        #menu.append("Save", call.open())
        #menu.append("Click", "win.click_here")
        #menu.append("Open", "open")

        #menu.append("Undo", "app.undo")
        #menu.append("Redo", "app.redo")

        #menuButton.set_menu_model(menu)
    
        #header.pack_start(menuButton)
      

        ## left vbox for notebook name 
        vboxLeft = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
        vboxLeft.set_homogeneous(False)

        ## frame for left vbox
        leftFrame = Gtk.Frame()
        leftFrame.add(vboxLeft)
        leftFrame.set_hexpand(True)
        leftFrame.set_vexpand(True)
        leftFrame.set_name("leftFrame")
      
        #adds left frame to window

        #right vbox for notes 
        vboxRight = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
        vboxRight.set_homogeneous(False)
        container = Gtk.ScrolledWindow()
        container.set_name("rightFrame")
        text = myText.funct()
'''
        #text.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1))
        text.modify_text(Gtk.StateFlags.NORMAL, Gdk.Color(0,0,0))
        text.set_vexpand(True);
        text.set_indent(10)
        text.set_top_margin(90)
        text.set_left_margin(20)
        self.textbuffer = text.get_buffer()
        self.tag_bold = self.textbuffer.create_tag("bold", weight = Pango.Weight.BOLD)
        self.tag_italic = self.textbuffer.create_tag("italic", style=Pango.Style.ITALIC)
        self.tag_underline = self.textbuffer.create_tag("underline", underline=Pango.Underline.SINGLE)
 '''     
        container.add(text)
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

        # left arrow
        #leftArrow = Gtk.Button()
        #leftArrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        #box.add(leftArrow)

        
        button_bold = Gtk.ToggleToolButton()
        button_bold.set_active(False)
        button_bold.set_icon_name("format-text-bold-symbolic")
        toolbar.insert(button_bold, 0)

        button_italic = Gtk.ToggleToolButton()
        button_italic.set_icon_name("format-text-italic-symbolic")
        toolbar.insert(button_italic, 1)

        button_underline = Gtk.ToggleToolButton()

        button_underline.set_icon_name("format-text-underline-symbolic")
        toolbar.insert(button_underline, 2)

        button_bold.connect("clicked", myText.on_button_clicked(self, button_bold, myText.tag_bold)
      '''
        button_italic.connect("clicked", myText.on_button_clicked)
        button_underline.connect("clicked", myText.on_button_clicked)
      '''
      
      
        header.pack_start(box)
'
    def on_button_clicked(self, widget, tag):
      name = widget.get_icon_name()
      value = widget.get_active()
      bounds = self.textbuffer.get_selection_bounds()
      if len(bounds) != 0:
         start, end = bounds
         self.textbuffer.apply_tag(tag, start, end)
'''
         


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

