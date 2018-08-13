import gi
import TextSet as text_set
import Popup as pop
import Menu_Button as menu_button
import sidebar_menu as sidebar
import Notebook as note
import BinaryTree as tree
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
                
                self.count = 0

                #keeps track of notebooks
                self.notebook_list = []

		'''
		when app opens, have it open up first notebook using page open method and first page that comes with it
		edge case: if no notebooks then ask the user to create their first one and first page 
		'''
                ## current notebook instance variable
                self.notebookname = None
                self.pagename = None
                
                #for binary trees
                self.notebook = None
                self.page = None

                #for gui
                self.gui_notebook = None

                
		# men button on right
		self.menuButton = Gtk.MenuButton()
		# drop menu
		self.menu = menu_button.NoteMenu()
		self.menuButton.set_menu_model(self.menu)
    
		self.header.pack_start(self.menuButton)
        	
		## left vbox for notebook name 
		self.vboxLeft = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 20)
		self.vboxLeft.set_homogeneous(False)
                self.notebook_layout = Gtk.Notebook()

                #adds notebook
                self.notebook_layout.set_tab_pos(Gtk.PositionType.LEFT)
                self.vboxLeft.pack_start(self.notebook_layout, True, True, 0)


		## frame for left vbox
	       	#self.leftFrame = sidebar.SidebarWindow()
                self.leftFrame = Gtk.Frame()
                self.leftFrame.add(self.vboxLeft)
		self.leftFrame.set_hexpand(True)
		self.leftFrame.set_vexpand(True)
		
                #buttons for toolbar
		self.button_bold = Gtk.ToggleToolButton()
		self.button_italic = Gtk.ToggleToolButton()
		self.button_underline = Gtk.ToggleToolButton()
		
		## right vbox for notes 
		self.vboxRight = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
		self.vboxRight.set_homogeneous(False)
		self.scroll_container = Gtk.ScrolledWindow()
		self.mytext = text_set.TextSet(self.button_bold, self.button_italic, self.button_underline)
		self.buff = self.mytext.get_buffer()
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
		
		 
		
		self.button_bold.set_icon_name("format-text-bold-symbolic")
		self.toolbar.insert(self.button_bold, 0)

		
		self.button_italic.set_icon_name("format-text-italic-symbolic")
		self.toolbar.insert(self.button_italic, 1)

		

		self.button_underline.set_icon_name("format-text-underline-symbolic")
		self.toolbar.insert(self.button_underline, 2)

		self.button_bold.connect("toggled", self.mytext.on_button_clicked, "Bold", self.button_italic, self.button_underline)
		self.button_italic.connect("toggled", self.mytext.on_button_clicked, "Italic", self.button_bold, self.button_underline)
		self.button_underline.connect("toggled", self.mytext.on_button_clicked, "Underline", self.button_bold, self.button_italic)

      


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
		menu_button.open_file(self, self.mytext)
	

        


		'''
		binary search tree will be used to create notebook (tree itself will be notebook and first node is the first page)
		pro of binary tree is opening pages will take less time compared to any other data structure 
		nodes will be sorted by alphabetical order
		'''
	


        '''
        when clicked, notebook section and page has to stay active until another one is clicked
        when the user clicks another, it should open the file for them and apply it to textview
        look into list of buttons
        '''
	def new_clicked(self,  action, none):
		self.popup = pop.PopUp(self, True)
		self.response = self.popup.run()

		if(self.response == Gtk.ResponseType.OK):
			## save before doing next step 
			self.buff.set_text("")   ##method can be placed inside page constructor 
                        self.pagename = self.popup.entry.get_text()
                        self.page = tree.BinaryTree.Page(self.pagename)
                        self.notebook.add(self.page)

			## update gui
                        self.gui_notebook = self.notebook.get_current_section(self.notebook_layout)
                        self.notebook.add_page_gui(self.gui_notebook, self.pagename)

                        self.notebook_layout.show_all()
                        self.count = self.count + 1
                        if(self.count is 3):
                            self.notebook.notebook_iterator()



		self.popup.destroy()  
			
   

	def new_book_clicked(self, action, none):

		self.popup = pop.PopUp(self, False) 
		self.response = self.popup.run()

		if(self.response == Gtk.ResponseType.OK):
			#save current work (new notebook will clear textview)
			self.buff.set_text("")
                        self.notebookname = self.popup.entry.get_text()
                        self.notebook = note.Notebook(self.notebookname)
                        self.pagename = self.popup.entry2.get_text()
                        self.page = tree.BinaryTree.Page(self.pagename)
                        self.notebook.add(self.page)
                        self.notebook_list.append(self.notebook)
                        self.count = self.count + 1
                        if(self.count is 3):
                            self.notebook.notebook_iterator()
                        
                        #adds notebook to gui
                        self.notebook.add_notebook_gui(self.notebook_layout, self.notebookname)

                        ##makes new notebook current notebook 
                        self.gui_notebook = self.notebook.set_current_section(self.notebook_layout)
                        
                        #adds page to gui 
                        self.notebook.add_page_gui(self.gui_notebook, self.pagename)
                        
                        self.notebook_layout.show_all()

		self.popup.destroy()
	

	def save_clicked(self, action, none):
		menu_button.save_file(self, self.mytext)
    
	def save_as_clicked(self, action, none):
		print("save as")  
    
	def settings_clicked(self, action, none):
		print("settings")
        
        def update_gui(self):
            	## left vbox for notebook name 
		self.vboxLeft = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
		self.vboxLeft.set_homogeneous(False)
                self.notebook_layout = Gtk.Notebook()

                #notebook tab
                self.tab1 = Gtk.Box()
                self.tab1.set_border_width(10)
                for i in range(len(self.notebook_list)):
                    self.notebook_layout.append_page(self.tab1, Gtk.Label(self.notebook_list[i]))

                self.leftFrame = Gtk.Frame()
                self.leftFrame.add(self.vboxLeft)
		self.leftFrame.set_hexpand(True)
		self.leftFrame.set_vexpand(True)

                self.grid.attach(self.leftFrame,0,0,2,30)






	
		  

	

if __name__ == '__main__':
    win = MainWindow()
    Gtk.main()

