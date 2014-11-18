from PIL import Image, ImageDraw
import numpy
import settings

Draw = None

def use_aggdraw():
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

    return AggDraw

def use_pil():
    class PilDraw(object):
        def __init__(self):
            self.w, self.h = settings.width, settings.height
            self.im = Image.new(settings.image_color_mode, (self.w,self.h), 255)
            self.draw = ImageDraw.Draw(self.im)

        def circle(self, pt, radius):
            x,y = pt
            x1,y1 = x-radius, -(y-radius)
            x2,y2 = x+radius, -(y+radius)
            
            self.draw.ellipse((x1, y1, x2, y2), fill = 0)

        def plot(self, start, stop):
            x1, y1 = start[0], -start[1]
            x2, y2 = stop[0], -stop[1]
            self.draw.line((x1, y1, x2, y2), fill = 0, width=4)
            
        def save(self, filename):
            self.im.save(filename, 'PNG')

    return PilDraw

try:
    import aggdraw
    global Draw
    Draw = use_aggdraw()
except ImportError:
    print("You do not have aggdraw. Will use plain Python Imaging Library instead")
    global Draw
    Draw = use_pil()

    

