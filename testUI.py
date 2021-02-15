from guizero import *

name = "d"
mdp = "d"
#login
app = App(title = "Manager")
title= Text(app, text="Manager D system", size = 40, font="Times New Roman", color="black")
nameTxt= Text(app, text="name", size = 20, font="Times New Roman", color="black")
boxName = TextBox(app, width = 30, text= "")
mdpTxt= Text(app, text="password", size = 20, font="Times New Roman", color="black")
boxMdp = TextBox(app, width = 30, text= "")
#verif login
def VerifMdp():
    if boxName.value == name  :
        title.value = "ok"
    else:
        title.value = "off"
btVerifMdp = PushButton(app, command=VerifMdp, text="verif password")



app.display()
