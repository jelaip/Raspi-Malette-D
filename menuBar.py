from guizero import App, MenuBar

class MenuBarItem:
    def fctFileSave():
        print("save")
    def fctReadDoc():
        print("ReadDoc")
    def __init__(self, app):
        self.app = app
        self.createBar()
    def createBar():
        menubar = MenuBar(self.app, toplevel=["File","Doc"],
                                    options=[
                                    [["Save",fctFileSave]],
                                    [["Doc",fctReadDoc]]
                                    ])
