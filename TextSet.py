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
		self.textbuffer = self.get_buffer()
		self.tag_bold = self.textbuffer.create_tag("bold", weight = Pango.Weight.BOLD)
		self.tag_italic = self.textbuffer.create_tag("italic", style=Pango.Style.ITALIC)
		self.tag_underline = self.textbuffer.create_tag("underline", underline=Pango.Underline.SINGLE)
    
	def on_button_clicked(self, widget, tagname):
		if tagname == "Bold":
			tag= self.tag_bold
		elif tagname == "Italic":
			tag = self.tag_italic
		elif tagname == "Underline":
			tag = self.tag_underline
		name = widget.get_icon_name()
		value = widget.get_active()
		bounds = self.textbuffer.get_selection_bounds()
		#highlighting
		if(value == True and len(bounds) != 0):  
			start, end = bounds
			self.textbuffer.apply_tag(tag, start, end)
	
	def mouse_clicked(self, window, event): 
		self.button_bold.set_active(False)
		self.button_italic.set_active(False)
		self.button_underline.set_active(False)

  
