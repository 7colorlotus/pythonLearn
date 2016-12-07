#Python支持多种图形界面的第三方库，包括：
#Tk
#wxWidgets
#Qt
#GTK
#等等。
#但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行GUI编程。

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	
	def createWidgets(self):
		self.helloLabel = Label(self,text='Hello,world!')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		self.quitButton.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self,text='Hello',command=self.hello)
		self.alertButton.pack()
		
	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','Hello,%s' % name)
		

app = Application()
app.master.title('Hello World')
app.mainloop()

























