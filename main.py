# -*- coding: utf-8 -*-

import gtk
import mysql.connector

def on_convert_pressed(calcbutton, adress_entry, login_entry, password_entry):
    adress = adress_entry.get_text()
    login = login_entry.get_text()
    password = password.get_text()


def main():
    window = gtk.Window()
    window.set_default_size(400,400)
    window.set_title(u"sql_to_dpf")

    mainbox = gtk.VBox()
    window.add(mainbox)

    adress_box = gtk.HBox()
    mainbox.pack_start(adress_box, expand=False)
    login_box = gtk.HBox()
    mainbox.pack_start(login_box, expand=False)
    password_box = gtk.HBox()
    mainbox.pack_start(password_box, expand=False)

    adress_label = gtk.Label(u"adress")
    adress_box.pack_start(adress_label)
    adress_entry = gtk.Entry()
    adress_entry.set_text(u"127.0.0.1")
    adress_box.pack_start(adress_entry)

    login_label = gtk.Label(u"login")
    login_box.pack_start(login_label)
    login_entry = gtk.Entry()
    login_entry.set_text(u"root")
    login_box.pack_start(login_entry)
	
    password_label = gtk.Label(u"password")
    password_box.pack_start(password_label)
    password_entry = gtk.Entry()
    password_entry.set_visibility(0) # поле для пароля показывает звёздочки
    password_box.pack_start(password_entry)	

    convert_button = gtk.Button(u"convert")
    mainbox.pack_start(convert_button, expand=False)

    d_flabel = gtk.Label(u"")
    mainbox.pack_start(d_flabel,expand=False)


    #sw = gtk.ScrolledWindow()
    #sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

    window.connect("destroy", lambda _: gtk.main_quit())
    convert_button.connect("clicked", on_convert_pressed, adress_entry, login_entry, password_entry)

    window.show_all()
    gtk.main()

def connect__to_server(adress, login, password_db): #Данная функция соединяется с сервером, уведомляет об успшном соединение
	cnx = mysql.connector.connect(user=login, password=password_db, host=adress)
	
def extract_db(): #Данная функция извлекает данные из базы данных
	pass
	
def convert_to_pdf(): #данная функция превращает данные в pdf
	pass

if __name__ == "__main__":
	main()
