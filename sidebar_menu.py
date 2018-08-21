import gi
import Notebook as note
import BinaryTree as tree
from gi.repository import Gtk, Gio

gi.require_version('Gtk', '3.0')


class SidebarWindow(Gtk.Frame):
    def __init__(self, textbuffer, win):
        Gtk.Frame.__init__(self, )
        self.buff = textbuffer
        self.popup = None
        self.win = win
        # keeps track of notebooks
        self.notebook_list = []

        # keeps track of buttons
        self.notebook_buttons = []

        '''
        set character limit on page
        make delete and remove buttons work
        made thread work activate one at a time
        '''

        # current notebook instance variable
        self.notebookname = None
        self.pagename = None

        # for binary trees
        self.notebook = None
        self.page = None

        # for gui
        self.gui_notebook = None

        # grid to hold everything on the side menu
        self.menu_grid = Gtk.Grid()
        self.menu_grid.set_hexpand(True)

        # left vbox for notebook name
        self.hboxLeft = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        # self.gridLeft = Gtk.Grid()
        self.hboxLeft.set_homogeneous(False)
        self.notebook_layout = Gtk.Notebook()
        self.hboxLeft.set_property("width-request", 20)
        self.hboxLeft.set_hexpand(True)

        # adds notebook
        self.notebook_layout.set_tab_pos(Gtk.PositionType.LEFT)

        # sidebar buttons
        self.rename_button = Gtk.Button(label="Rename")
        self.delete_button = Gtk.Button(label="Delete")
        self.rename_button.connect("clicked", win.rename)
        self.delete_button.connect("clicked", win.delete)

        # adds notebook to vbox
        self.hboxLeft.pack_start(self.notebook_layout, True, True, 0)

        # creates hbox for rename notebook and delete button
        self.buttons_Left = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.rename_button.set_property("width-request", 20)
        self.delete_button.set_property("width-request", 20)
        self.buttons_Left.pack_start(self.rename_button, False, True, 0)
        self.buttons_Left.pack_start(self.delete_button, False, True, 0)

        # frame for left vbox

        self.leftFrame = Gtk.Frame()
        self.leftFrame.add(self.hboxLeft)
        self.leftFrame.set_hexpand(True)
        self.leftFrame.set_vexpand(True)
        self.leftFrame.set_property("width-request", 50)

        # adds frame and buttons to side bar
        self.menu_grid.attach(self.leftFrame, 0, 0, 2, 1)
        self.menu_grid.attach_next_to(self.buttons_Left, self.leftFrame, Gtk.PositionType.BOTTOM, 2, 2)
        self.add(self.menu_grid)

    def new_book(self, popup):
        self.popup = popup
        client_response = self.popup.entry.get_text()
        if (not self.contains_notebook(client_response)):
            # save current work (new notebook will clear textview)
            self.buff.set_text("")
            self.notebookname = self.popup.entry.get_text()
            self.notebook = note.Notebook(self.notebookname)
            self.pagename = self.popup.entry2.get_text()
            self.page = tree.BinaryTree.Page(self.pagename)
            self.notebook.add(self.page)
            self.notebook_list.append(self.notebook)

            # adds notebook to gui
            self.notebook.add_notebook_gui(self.notebook_layout, self.notebookname)

            ##makes new page current page
            self.gui_notebook_page = self.notebook.set_current_section(self.notebook_layout)
            # adds page to gui
            self.notebook.add_page_gui(self.gui_notebook_page, self.pagename)

            self.notebook_layout.show_all()

        else:
            self.win.duplicate_false()

    def new_page(self, popup):
        self.popup = popup
        client_response = self.popup.entry.get_text()
        if (not self.notebook.contains_page(client_response)):
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
            self.win.duplicate_true()

    def rename(self, popup):
        self.rename_pop = popup
        temp = self.pagename
        response = self.rename_pop.entry_notebook.get_text()
        response2 = self.rename_pop.entry_page.get_text()

        note_boolean = True
        if (self.contains_notebook(response)):
            note_boolean = False
            if (response == self.notebookname):
                note_boolean = True
            else:
                self.win.duplicate_false()

        if (self.notebook.contains_page(response2)):
            self.win.duplicate_true()

        # if(not self.notebook.contains_page(response2) and not self.contains_notebook(response)):
        if (not self.notebook.contains_page(response2) and note_boolean):
            # changes name instance variables
            self.notebookname = self.rename_pop.entry_notebook.get_text()
            self.pagename = self.rename_pop.entry_page.get_text()

            # updates binary tree name and page name
            self.notebook.set_name(self.notebookname)
            self.page.set_name(self.pagename)

            # updates notebook tab gui
            self.gui_notebook_page = self.notebook.get_current_page(self.notebook_layout)
            label = Gtk.Label(self.notebookname)
            self.notebook_layout.set_tab_label(self.gui_notebook_page, label)

            # updates notebook page
            self.notebook.set_page_name(temp, self.pagename)

    def delete(self, popup):
        buttons = popup.check_buttons
        if(buttons[0].get_active() == True):
           print("yes")
         

    def contains_notebook(self, name):
        for i in range(len(self.notebook_list)):
            if (self.notebook_list[i].NotebookName == name):
                return True

        return False
