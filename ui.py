from Tkinter import *


class RoundedButton(Canvas):
    def __init__(self, parent, width, height, padding, color, title):
        Canvas.__init__(self, parent, borderwidth=0,
                        relief="flat", highlightthickness=0, bg='systemTransparent')

        label = Label(self, justify='center')
        label.config(font=("Helvetica", 36), background=color, foreground='white')
        label["text"] = title
        label.place(x=width / 2, y=height/2, anchor="center")
        corner_radius = height/2
        if corner_radius > 0.5 * width:
            return
        if corner_radius > 0.5 * height:
            return

        rad = 2 * corner_radius

        def shape():
            self.create_polygon((padding, height - corner_radius - padding, padding, corner_radius + padding,
                                 padding + corner_radius, padding, width - padding - corner_radius, padding,
                                 width - padding, corner_radius + padding, width - padding,
                                 height - corner_radius - padding, width - padding - corner_radius, height - padding,
                                 padding + corner_radius, height - padding), fill=color, outline=color)
            self.create_arc((padding, padding + rad, padding + rad, padding), start=90, extent=90, fill=color,
                            outline=color)
            self.create_arc((width - padding - rad, padding, width - padding, padding + rad), start=0, extent=90,
                            fill=color, outline=color)
            self.create_arc((width - padding, height - rad - padding, width - padding - rad, height - padding),
                            start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding, height - padding - rad, padding + rad, height - padding), start=180, extent=90,
                            fill=color, outline=color)

        id = shape()
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1 - x0)
        height = (y1 - y0)
        self.configure(width=width, height=height)


