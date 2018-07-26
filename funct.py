import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango


class funct(Gtk.TextView):
    def __init__(self):
        Gtk.TextView.__init__(self)
        self.set_vexpand(True)
        self.set_indent(10)
        self.set_top_margin(90)
        self.set_left_margin(20)
        self.textbuffer = self.get_buffer()
        tag_bold = self.textbuffer.create_tag("bold", weight = Pango.Weight.BOLD)
        tag_italic = self.textbuffer.create_tag("italic", style=Pango.Style.ITALIC)
        tag_underline = self.textbuffer.create_tag("underline", underline=Pango.Underline.SINGLE)

    def on_button_clicked(window, widget, tag):
        name = widget.get_icon_name()
        value = widget.get_active()
        bounds = self.textbuffer.get_selection_bounds()
        if len(bounds) != 0:
            start, end = bounds
            self.textbuffer.apply_tag(tag, start, end)
