# -*- coding: utf-8 -*-

import gtk

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
    adress_box.pack_start(adress_entry)

    login_label = gtk.Label(u"login")
    login_box.pack_start(login_label)
    login_entry = gtk.Entry()
    login_box.pack_start(login_entry)
	
    password_label = gtk.Label(u"password")
    password_box.pack_start(password_label)
    password_entry = gtk.Entry()
    password_box.pack_start(password_entry)	

    convert_button = gtk.Button(u"convert")
    mainbox.pack_start(convert_button, expand=False)

    d_flabel = gtk.Label(u"Тут будет слово с ошибкой")
    mainbox.pack_start(d_flabel,expand=False)


    # sw = gtk.ScrolledWindow()
    # sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

    window.connect("destroy", lambda _: gtk.main_quit())
    convert_button.connect("clicked", on_convert_pressed, adress_entry, login_entry, password_entry)

    window.show_all()
    gtk.main()

def server_adress(adress, login, password):
	pass
	

if __name__ == "__main__":
	main()
