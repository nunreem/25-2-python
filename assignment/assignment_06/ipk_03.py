import tkinter as tk
import math
class Shape:
    def __init__(self,x,y): self.x,self.y=x,y
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError
    def draw(self,canvas): raise NotImplementedError

class Rectangle (Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y); self.w, self.h=w,h
    def area(self): return self.w*self.h
    def perimeter(self): return 2* (self.w+self.h)
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="tomato")