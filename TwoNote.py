import gi
import TextSet as text_set
import Popup as pop
import Menu_Button as menu_button
import sidebar_menu as sidebar
import Notebook as note
import BinaryTree as tree
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
import threading
import time

class MainWindow(Gtk.ApplicationWindow):
   def __init__(self):
      Gtk.Window.__init__(self, title = "TwoNote")
      # size of window
      self.set_default_size(1920,1080)

      self.header = Gtk.HeaderBar()
      self.header.set_show_close_button(True)
      self.header.props.title = "TwoNote"
      self.set_titlebar(self.header)

      #keeps track of notebooks
      self.notebook_list = []

       ## current notebook instance variable
      self.notebookname = None
      self.pagename = None
                
      #for binary trees
      self.notebook = None
      self.page = None

      #for gui
      self.gui_notebook_page = None  #returns page (content) not tab 
      self.current_button  = None #rep

		# men button on right
      self.menuButton = Gtk.MenuButton()

		# drop menu
      self.menu = menu_button.NoteMenu()
      self.menuButton.set_menu_model(self.menu)
    
      self.header.pack_start(self.menuButton)
        	
      #grid to hold everything on the side menu
      self.menu_grid = Gtk.Grid()
      self.menu_grid.set_hexpand(True)

      ## left vbox for notebook name 
      self.hboxLeft = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
      #self.gridLeft = Gtk.Grid()
      self.hboxLeft.set_homogeneous(False)
      self.notebook_layout = Gtk.Notebook()
      self.hboxLeft.set_property("width-request", 20)
      self.hboxLeft.set_hexpand(True)

      #adds notebook 
      self.notebook_layout.set_tab_pos(Gtk.PositionType.LEFT)
                
      #sidebar buttons
      self.rename_button = Gtk.Button(label = "R")
      self.delete_button = Gtk.Button(label = "D")
      self.rename_button.connect("clicked", self.rename)
      self.delete_button.connect("clicked", self.delete)
                
      #adds notebook to vbox
      self.hboxLeft.pack_start(self.notebook_layout, True, True, 0)

      #creates hbox for rename notebook and delete button
      self.buttons_Left = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
      self.rename_button.set_property("width-request", 20)
      self.delete_button.set_property("width-request", 20)
      self.buttons_Left.pack_start(self.rename_button, False, True, 0)
      self.buttons_Left.pack_start(self.delete_button, False, True, 0)
                
      ## frame for left vbox
      #self.leftFrame = sidebar.SidebarWindow()
      self.leftFrame = Gtk.Frame()
      self.leftFrame.add(self.hboxLeft)
      self.leftFrame.set_hexpand(True)
      self.leftFrame.set_vexpand(True)
      self.leftFrame.set_property("width-request", 50)

      #adds frame and buttons to side bar
      self.menu_grid.attach(self.leftFrame, 0, 0, 2, 1)
      self.menu_grid.attach_next_to(self.buttons_Left, self.leftFrame, Gtk.PositionType.BOTTOM, 2, 2)

      #buttons for toolbar
      self.button_bold = Gtk.ToggleToolButton()
      self.button_italic = Gtk.ToggleToolButton()
      self.button_underline = Gtk.ToggleToolButton()
		
      # right vbox for notes 
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
      self.grid.attach(self.menu_grid,0,0,1,30)
      self.toolbar = Gtk.Toolbar()
      self.grid.attach(self.toolbar, 2, 0, 5, 1)
      self.grid.attach_next_to(self.rightFrame, self.menu_grid, Gtk.PositionType.RIGHT, 7,30)
		
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


      self.thread = threading.Thread(target = self.run, args = ())
      self.thread.daemon = True
      self.thread_bool = True

      self.thread.start()

      if(len(self.notebook_list) == 0):
            self.new_book()

                



   def open_clicked(self, action, none):
      menu_button.open_file(self, self.mytext)
        
   def new_clicked(self,  action, none):
      check = True
      self.popup = pop.PopUp(self, True)
      while(check):
         check = False
         self.response = self.popup.run()
         if(self.response == Gtk.ResponseType.OK):
            client_response = self.popup.entry.get_text()
            if(not self.notebook.contains_page(client_response)):
               ##SAVE
               self.buff.set_text("")
               self.pagename = self.popup.entry.get_text()
               self.page = tree.BinaryTree.Page(self.pagename)
               self.notebook.add(self.page)
               ## update gui
               self.gui_notebook_page = self.notebook.get_current_page(self.notebook_layout)
               self.notebook.add_page_gui(self.gui_notebook_page, self.pagename)
               self.notebook_layout.show_all()
            else:
               self.duplicate = pop.Duplicate(self, True)
               self.duplicate.run()
               self.duplicate.destroy()

               check = True
            
      self.popup.destroy()
               




   def new_book_clicked(self, action, none):
      self.new_book()

   def new_book(self):
      self.popup = pop.PopUp(self, False) 
      check = True
      while(check):
         check = False
         self.response = self.popup.run()
         if(self.response == Gtk.ResponseType.OK):
            client_response = self.popup.entry.get_text()
            if(not self.contains_notebook(client_response)):
               #save current work (new notebook will clear textview)
               self.buff.set_text("")
               self.notebookname = self.popup.entry.get_text()
               self.notebook = note.Notebook(self.notebookname)
               self.pagename = self.popup.entry2.get_text()
               self.page = tree.BinaryTree.Page(self.pagename) 
               self.notebook.add(self.page)
               self.notebook_list.append(self.notebook)
                        
               #adds notebook to gui
               self.notebook.add_notebook_gui(self.notebook_layout, self.notebookname)

               ##makes new page current page
               self.gui_notebook_page = self.notebook.set_current_section(self.notebook_layout)
                        
               #adds page to gui 
               self.notebook.add_page_gui(self.gui_notebook_page, self.pagename)
                        
               self.notebook_layout.show_all()

            else:
               self.duplicate = pop.Duplicate(self, False)
               self.duplicate.run()
               self.duplicate.destroy()
               check = True


      self.popup.destroy()

   def rename(self, signal):
      self.rename_pop = pop.Rename(self, self.notebookname, self.pagename)
      check = True

      while(check):
         check = False
         self.response = self.rename_pop.run()
         if(self.response == Gtk.ResponseType.OK):
            temp = self.pagename
            response = self.rename_pop.entry_notebook.get_text()
            response2 = self.rename_pop.entry_page.get_text()

            note_boolean = True
            if(self.contains_notebook(response)):
               note_boolean = False
               if(response == self.notebookname):
                  note_boolean = True
               else:
                  self.duplicate2 = pop.Duplicate(self, False)
                  self.duplicate2.run()
                  self.duplicate2.destroy()
                  check = True



            if(self.notebook.contains_page(response2)):
               self.duplicate = pop.Duplicate(self, True)
               self.duplicate.run()
               self.duplicate.destroy()
               check = True



            #if(not self.notebook.contains_page(response2) and not self.contains_notebook(response)): 
            if(not self.notebook.contains_page(response2) and note_boolean):
               #changes name instance variables
               self.notebookname = self.rename_pop.entry_notebook.get_text()
               self.pagename = self.rename_pop.entry_page.get_text()
                    
               #updates binary tree name and page name
               self.notebook.set_name(self.notebookname)
               self.page.set_name(self.pagename)

               #updates notebook tab gui
               self.gui_notebook_page = self.notebook.get_current_page(self.notebook_layout)                
               label = Gtk.Label(self.notebookname)
               self.notebook_layout.set_tab_label(self.gui_notebook_page, label)
                    
               #updates notebook page
               self.notebook.set_page_name(temp, self.pagename)
                    
      self.rename_pop.destroy()

   def delete(self, signal):
      self.delete_pop = pop.Delete(self, self.notebook, self.notebookname, self.pagename)
      self.response = self.delete_pop.run()

   def contains_notebook(self, name):
      for i in range(len(self.notebook_list)):
         if(self.notebook_list[i].NotebookName == name):
            return True

      return False	

   def save_clicked(self, action, none):
      menu_button.save_file(self, self.mytext)

   def save_as_clicked(self, action, none):
      print("save as")  
    
   def settings_clicked(self, action, none):
      print("settings")
        
   def run(self):
      while self.thread:
         print("do domething")
         self.thread = False

	
if __name__ == '__main__':
      win = MainWindow()
      Gtk.main()

