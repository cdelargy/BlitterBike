from Tkinter import *
import random
from math import *

class App:
   	def __init__(self, t):
   		global time
   		c = Canvas(t, width=maxCol*2, height=maxRow*2)
   		c.pack()
   		def task():
	   		global time, z_mode, p_mode, pal
	   		self.i = PhotoImage(width=maxCol,height=maxRow)
   			row = 0; col = 0
   			while (row < maxRow):
   				z = plasma(row,col,z_mode);
				color = (pal[z][0],pal[z][1],pal[z][2])
   				self.i.put(rgb2Hex(color),(row,col))
   				col += 1
   				if col == maxCol:
   					row +=1; col = 0
   			time += 1
   			if (time > 64):
   				z_mode = random.randint(0,2)
   				p_mode = random.randint(0,2)
				pal = palette(p_mode)
   				time = 1
   			c.delete(ALL)
   			c.create_image(maxRow/2, maxCol/2, image = self.i, anchor=NW)
   			t.after(2,task)  # reschedule event in 1 seconds
		t.after(2,task)

def plasma(x, y, z_mode):
	if z_mode == 0:
		return int((128.0 + (128.0 * sin(x / (time%31 + 1))) + 128.0 + (128.0 * sin(y / (time%15 + 1))) + 128.0 + (128.0 * sin((x + y) / (time%31 +1))) + 128.0 + (128.0 * sin(sqrt(x * x + y * y) / (time%15 + 1)))) / 4)
	elif z_mode == 1:
		return int((128.0 + (128.0 * sin(x / 16.0)) + 128.0 + (128.0 * sin(y / (time%7+1))) + 128.0 + ((128-time%127) * sin((x + y) / (time%31 +1))) + 128.0 + (128.0 * sin(sqrt(x * y + y * y) / 8))) / 4)
	else:
		return int((128.0 + (128.0 * sin(x*(time%33) / 16.0)) + 128.0 + (128.0 * sin(y*(time%17) / 8.0)) + 128.0 + (128.0 * sin((x + y) / (time%31 +1))) + 128.0 + (128.0 * sin(sqrt(x * x + y * y) / (time%15 + 1)))) / 4)

def rgb2Hex(rgb):
	return '#%02x%02x%02x' % tuple(rgb)

def palette(p_mode):
		map = [None]*256
		i=0
		if (p_mode==0):
			for i in range(0,64):
				map[i]=([255, i * 4, 255 - (i * 4)])
				map[i+64]=([255 - (i * 4), 255, i * 4])
				map[i+128]=([0, 255 - (i * 4), 255])
				map[i+192]=([i * 4, 0, 255])
			return map
		elif(p_mode==1):
			for i in range(0,32):
				map[i]=([255, i * 8, 255 - (i * 8)])
				map[i+32]=([255 - (i * 8), 255, i * 8])
				map[i+64]=([0, 255 - (i * 8), 255])
				map[i+96]=([i * 8, 0, 255])
				map[i+128]=([255, i * 8, 255 - (i * 8)])
				map[i+160]=([255 - (i * 8), 255, i * 8])
				map[i+192]=([0, 255 - (i * 8), 255])
				map[i+224]=([i * 8, 0, 255])
			return map
		else:
			for i in range(0,64):
				map[i]=([255, 0, 255 - (i * 4)])
				map[i+64]=([255 - (i * 4), i*4, 0])
				map[i+128]=([0, 255 - (i * 4), 0])
				map[i+192]=([i*4, 0, i*4])
			return map
maxRow = 64
maxCol = 64
time = 1
z_mode = 1
p_mode = 1
pal = palette(p_mode)
t = Tk()
a = App(t)    
t.mainloop()