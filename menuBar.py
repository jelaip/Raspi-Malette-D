from guizero import App, MenuBar

class MenuBarItem:
    def fctFileSave(self):
        print("save")
    def fctReadDoc(self):
        print("ReadDoc")
    def __init__(self, app):
        self.app = app
        self.createBar()
    def createBar(self):
        menubar = MenuBar(self.app, toplevel=["File","Doc"],
                                    options=[
                                    [["Save",self.fctFileSave]],
                                    [["Doc",self.fctReadDoc]]
                                    ])
