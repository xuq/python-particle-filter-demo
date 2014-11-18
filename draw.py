from PIL import Image, ImageDraw
import aggdraw
import numpy
import settings


class AggDraw(object):
    def __init__(self):
        self.w, self.h = settings.width, settings.height
        self.im = Image.new(settings.image_color_mode, (self.w,self.h), 255)#(255, 255, 255))
        self.adraw = aggdraw.Draw(self.im)
        self.pen_black = aggdraw.Pen("black", 8)
        self.brush_red = aggdraw.Brush("red")
        self.pen_red = aggdraw.Pen("red", 2)

    def circle(self, pt, radius):
        x,y = pt
        x1,y1 = x-radius, -(y-radius)
        x2,y2 = x+radius, -(y+radius)

        self.adraw.ellipse((x1, y1, x2, y2), self.pen_red, self.brush_red)
        self.adraw.flush()

    def plot(self, start, stop):
        x1, y1 = start[0], -start[1]
        x2, y2 = stop[0], -stop[1]
        self.adraw.line((x1, y1, x2, y2), self.pen_black)
        self.adraw.flush()

    def save(self, filename):
        self.im.save(filename, 'PNG')
