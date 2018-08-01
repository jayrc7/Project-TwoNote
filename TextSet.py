import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango


class TextSet(Gtk.TextView):
	def __init__(self):
		Gtk.TextView.__init__(self)
		self.set_vexpand(True)
		self.set_indent(10)
		self.set_top_margin(90)
		self.set_left_margin(20)
                self.tb = TextBuffer()
                self.set_buffer(self.tb)
    
	def on_button_clicked(self, widget, tagname, widget1, widget2):
		name = widget.get_icon_name()
		value = widget.get_active()
		bounds = self.tb.get_selection_bounds()

                #if(value == False and len(bounds) != 0):


		#highlighting
                if(value == True and len(bounds) != 0):
                    start, end = bounds
                    self.tb.apply_tag_by_name(tagname, start, end)

                self.tb.markup(widget, tagname)
	
	def mouse_clicked(self, window, event): 
		self.button_bold.set_active(False)
		self.button_italic.set_active(False)
		self.button_underline.set_active(False)



class TextBuffer(Gtk.TextBuffer):
    def __init__(self):
        Gtk.TextBuffer.__init__(self)
        self.connect_after('insert-text', self.text_inserted)
        # A list to hold our active tags
        self.taglist_on = []
        #self.taglist_None = []
        #self.taglist_Bold = []
        #self.taglist_Italic = []
        #self.taglist_Underline = []
        # Our Bold tag.
        self.tag_bold = self.create_tag("Bold", weight=Pango.Weight.BOLD)  
        self.tag_none = self.create_tag("None", weight=Pango.Weight.NORMAL)
        self.tag_italic = self.create_tag("Italic", style=Pango.Style.ITALIC)
	self.tag_underline = self.create_tag("Underline", underline=Pango.Underline.SINGLE)
        self.tag_name = "None"


    def get_iter_position(self):
        return self.get_iter_at_mark(self.get_insert())

    def markup(self, widget, tagname):
        self.tag_name = tagname
        self.check = True
        ''' add "bold" to our active tags list '''
        if(widget.get_active() == True):
            if(self.tag_name == 'Bold'):
                if 'Bold' in self.taglist_on:
                    del self.taglist_on[self.tags_on.index('Bold')]
                else:
                    self.taglist_on.append('Bold')


            if(self.tag_name == 'Italic'):
                if 'Italic' in self.taglist_on:
                    del self.taglist_on[self.tags_on.index('Italic')]
                else:
                    self.taglist_on.append('Italic')

            if(self.tag_name == 'Underline'):
                if 'Underline' in self.taglist_on:
                    del self.taglist_on[self.tags_on.index('Underline')]
                else:
                    self.taglist_on.append('Underline')      

        else:
            self.check = False
            self.taglist_on.append('None')

    def text_inserted(self, buffer, iter, text, length):
        # A text was inserted in the buffer. If there are ny tags in self.tags_on,   apply them
        #if self.taglist_None or self.taglist_Italic or self.taglist_Underline or self.taglist_Bold:
        if self.taglist_on:
            # This sets the iter back N characters
            iter.backward_chars(length)
            # And this applies tag from iter to end of buffer
            if(self.check == True):
                if(self.tag_name == 'Italic'):
                    self.apply_tag_by_name('Italic', self.get_iter_position(), iter)

                if(self.tag_name == 'Bold'):
                    self.apply_tag_by_name('Bold', self.get_iter_position(), iter)

                if(self.tag_name == 'Underline'):
                    self.apply_tag_by_name('Underline', self.get_iter_position(), iter)
            
            else:
                self.apply_tag_by_name('None', self.get_iter_position(), iter)

            
  
