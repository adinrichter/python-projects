import tkinter as tk
from tkinter import *
import webbrowser, os

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title('Webpage Creator')

        self.input_text = tk.StringVar()
        self.page_text = tk.StringVar()

        self.input = Entry(self.master, textvariable = self.input_text, width = 60)
        self.input.pack(side = TOP)

        self.btn_default = Button(self.master, text = 'Default HTML Page', width = 12, height = 2, command = self.defaultHTML)
        self.btn_default.pack(side = RIGHT)

        self.btn_custom = Button(self.master, text = 'Custom HTML Page', width = 12, height = 2, command = self.customHTML)
        self.btn_custom.pack(side = RIGHT)

    # passes the preset message to the writeHTML() function
    def defaultHTML(self):
        self.writeHTML('This is an automatically generated webpage!')

    # passes the users message to the writeHTML() function
    def customHTML(self):
        self.writeHTML(self.input_text.get())

    # opens the index.html file in a web browser as long as the contents are not empty
    def writeHTML(self, htmlText):
        if htmlText.strip() != '':
            htmlFile = open('index.html', 'w')
            htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</h1>\n</body>\n</html>'
            htmlFile.write(htmlContent)
            htmlFile.close()
            webbrowser.get().open_new_tab('file:///' + os.getcwd() + '/index.html')

    


















if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
