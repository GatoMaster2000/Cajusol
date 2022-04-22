from PyQt5 import QtWidgets, uic
import webbrowser as wb
app = QtWidgets.QApplication([])

login = uic.loadUi("Login.ui")
menu = uic.loadUi("MenuPrincipal.ui")  
mante = uic.loadUi("MantenimientoEmpleados.ui")
sub = uic.loadUi("Sub_Menu.ui")
mante2 = uic.loadUi("MantenimientoClientes.ui")
prov = uic.loadUi("MenuProveedor.ui")
serv = uic.loadUi("MenuServicio.ui")

def gui_login():
        name = login.lineEdit.text()
        password = login.lineEdit_2.text()
        if len(name)==0 or len(password)==0:
           login.label_4.setText("Ingrese todos los datos")
        elif name == "Gato" and password == "1234":
           gui_menu()

def gui_menu():
        login.hide()
        login.lineEdit.setText("")
        login.lineEdit_2.setText("")
        menu.show()

def gui_mante():
    menu.hide()
    mante.show()

def gui_sub():
    menu.hide()
    sub.show()

def volver_menu():
    sub.hide()
    menu.show()

def volver_menu_mante():
    mante.hide()
    menu.show()

def cerrar_sesion():
    menu.hide()
    login.label_4.setText("")
    login.show()

def gui_mante2():
    menu.hide()
    mante2.show()

def volver_mante2():
    mante2.hide()
    menu.show()

def gui_prov():
    sub.hide()
    prov.show()

def volver_prov():
    prov.hide()
    sub.show()

def gui_serv():
    sub.hide()
    serv.show()

def volver_serv():
    serv.hide()
    sub.show()






def app_movil():
    chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chromepath).open_new_tab("https://carloscesarbandach.wixsite.com/website-1")
    
    
login.pushButton.clicked.connect(gui_login)
menu.pushButton_6.clicked.connect(gui_mante)
menu.pushButton.clicked.connect(gui_sub)
sub.pushButton_6.clicked.connect(volver_menu)
mante.pushButton_6.clicked.connect(volver_menu_mante)
menu.pushButton_8.clicked.connect(cerrar_sesion)
menu.pushButton_7.clicked.connect(gui_mante2)
mante2.pushButton.clicked.connect(volver_mante2)
menu.pushButton_9.clicked.connect(app_movil)
sub.pushButton_5.clicked.connect(gui_prov)
prov.pushButton.clicked.connect(volver_prov)
sub.pushButton_3.clicked.connect(gui_serv)
serv.pushButton.clicked.connect(volver_serv)

login.show()
app.exec()


