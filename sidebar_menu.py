import gi
from gi.repository import Gtk, GLib
import BinaryTree as tree
import Notebook as note
import threading

gi.require_version('Gtk', '3.0')


class SidebarWindow(Gtk.Frame):
    def __init__(self, textbuffer, win):
        Gtk.Frame.__init__(self)

        self.buff = textbuffer
        self.popup = None
        self.win = win
        # keeps track of notebooks
        self.notebook_list = []
        self.notebook_names = []

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

        #button
        self.active_button = None 
        self.previous_button = None

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
        
        try:
          self.f = open("NotebookMaster.txt", 'r')
          if '^' in self.f.read():
            self.get_notebook_contents()
            self.save_notebook_contents()
        except IOError as e:
          self.f = open("NotebookMaster.txt", 'w+')

        note.pressed = True
        
    
    def new_book(self, popup):
        self.popup = popup
        client_response = self.popup.entry.get_text()
        if(not self.contains_notebook(client_response)):
            # save current work (new notebook will clear textview)
            self.buff.set_text("")
            self.notebookname = self.popup.entry.get_text()
            self.notebook_names.append(self.notebookname)
            self.notebook = note.Notebook(self.notebookname, self)
            self.pagename = self.popup.entry2.get_text()
            self.page = tree.BinaryTree.Page(self.pagename)
            GLib.file_set_contents(self.pagename, '')
            self.notebook.add(self.page)
            self.notebook_list.append(self.notebook)

            # adds notebook to gui
            self.notebook.add_notebook_gui(self.notebook_layout, self.notebookname)

            ##makes new page current page
            self.gui_notebook_page = self.notebook.set_current_section(self.notebook_layout)
            # adds page to gui
            self.notebook.add_page_gui(self.gui_notebook_page, self.pagename, self.buff)

            #sets new button active
            for i in range(len(self.notebook.buttons)):
                if(self.notebook.buttons[i].get_label() == self.pagename):
                    self.previous_button = self.active_button
                    self.active_button = self.notebook.buttons[i]
                    self.notebook.buttons[i].set_active(True)
                    if(self.previous_button != None):
                        self.previous_button.set_active(False)
                    print("change")

            self.save_notebook_contents()
            self.notebook_layout.show_all()

        else:
            self.win.check = False
            self.win.duplicate_false()

    def new_book_nopop(self, notebookname):
        self.notebookname = notebookname
        self.notebook_names.append(self.notebookname)
        self.notebook = note.Notebook(self.notebookname, self)
        self.notebook.add_notebook_gui(self.notebook_layout, self.notebookname)
        self.notebook_list.append(self.notebook)
        self.gui_notebook_page = self.notebook.set_current_section(self.notebook_layout)
        return self.notebook

    def new_page_nopop(self, pagename , notebook):
        self.pagename = pagename
        self.page = tree.BinaryTree.Page(self.pagename)
        notebook.add(self.page)
        ## update gui
        self.gui_notebook_page = self.notebook.get_current_page(self.notebook_layout)
        notebook.add_page_gui(self.gui_notebook_page, self.pagename, self.buff)
        self.notebook_layout.show_all()



    def new_page(self, popup):
        self.popup = popup
        client_response = self.popup.entry.get_text()
        if (not self.notebook.contains_page(client_response)):
            ##SAVE
            self.buff.set_text("")
            self.pagename = self.popup.entry.get_text()
            self.page = tree.BinaryTree.Page(self.pagename)
            GLib.file_set_contents(self.pagename, '')
            ## update gui
            self.gui_notebook_page = self.notebook.get_current_page(self.notebook_layout)
            self.notebookname = self.notebook_layout.get_tab_label_text(self.gui_notebook_page)
            self.notebook = self.notebook_check(self.notebookname)
            self.notebook.add(self.page)

            self.notebook.add_page_gui(self.gui_notebook_page, self.pagename, self.buff)

            self.notebook_layout.show_all()
            self.save_notebook_contents()
        else:
            self.win.duplicate_true()

        for i in range(len(self.notebook.buttons)):
            if(self.notebook.buttons[i].get_label() == self.pagename):
                self.previous_button = self.active_button
                self.active_button = self.notebook.buttons[i]
                
                self.notebook.buttons[i].set_active(True)
                self.previous_button.set_active(False)
                
                print("change")

    def notebook_check(self, notebook_name):
        for i in range(len(self.notebook_list)):
            if(self.notebook_list[i].NotebookName == notebook_name):
              return self.notebook_list[i]

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

        page_boolean = True
        if(self.notebook.contains_page(response2)):
            page_boolean = False
            if(response2 == self.pagename):
                page_boolean = True

            else:
                self.win_duplicate_true()

        self.save_notebook_contents()

        #if (self.notebook.contains_page(response2)):
            #self.win.duplicate_true()

        # if(not self.notebook.contains_page(response2) and not self.contains_notebook(response)):
        if ( page_boolean and note_boolean):
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
        #delete file
        if(buttons[0].get_active() == True):
            self.notebook_names.remove(self.notebookname)
            self.notebook_list.remove(self.notebook)
            page = self.notebook_layout.get_current_page()
            self.notebook_layout.remove_page(page)

            self.gui_notebook_page = self.notebook.get_current_page(self.notebook_layout)
            self.notebookname = self.notebook_list[-1].NotebookName
            self.notebook = self.notebook_check(self.notebookname)
            self.pagename = self.notebook.pages[-1]
            #for i in range

            

        self.save_notebook_contents()




            

    def contains_notebook(self, name):
        for i in range(len(self.notebook_list)):
            if (self.notebook_list[i].NotebookName == name):
                return True

        return False

    def save_notebook_contents(self):
        #for i in range(len(self.notebook_list)):
            #print(self.notebook_list[i].NotebookName)

        self.string = ""
        for i in range(len(self.notebook_names)):
            if i == 0:
                self.string = self.string + self.notebook_names[i]
            else:
                self.string = self.string + "~" + self.notebook_names[i]

            for k in range(len(self.notebook_list[i].pages)):
                self.string = self.string + "^" + self.notebook_list[i].pages[k]

        self.f = open("NotebookMaster.txt", 'w+')
        self.f.write(self.string)
        self.f.close()


    def get_notebook_contents(self):
        self.f = open("NotebookMaster.txt", 'r')
        contents = self.f.read()
        self.twonote_structure = contents.split("~")
        for i in range(len(self.twonote_structure)):

            self.notebook_structure = self.twonote_structure[i].split("^")
            for k in range(len(self.notebook_structure)):
                if "\n" in self.notebook_structure[k]:
                    temp = self.notebook_structure[k].split("\n")
                    self.notebook_structure[k] = temp[0]

                if k == 0:
                    notebook = self.new_book_nopop(self.notebook_structure[k])

                else:
                    self.new_page_nopop(self.notebook_structure[k], notebook)

        self.gui_notebook_page = self.notebook.get_current_page(self.notebook_layout)
        self.notebookname = self.notebook_layout.get_tab_label_text(self.gui_notebook_page)
        self.notebook = self.notebook_check(self.notebookname)
        self.pagename = self.notebook.pages[-1]
        

        #special character in the end of current notebook and name
        for i in range(len(self.notebook.buttons)):
            if(self.notebook.buttons[i].get_label() == self.pagename):
                self.active_button = self.notebook.buttons[i]
                self.notebook.buttons[i].set_active(True)
                tmpname = self.active_button.get_label()
                self.load_current_page(tmpname)

    def load_current_page(self, name):
        file = open(name, 'r')
        contents = file.read()
        self.buff.set_text(contents)

    def save_current_page(self, prev_name):
        prev_file = open(prev_name, 'w+')
        start, end = self.buff.get_bounds()
        buff_content = self.buff.get_text(start, end, True)
        prev_file.write(buff_content)


        


