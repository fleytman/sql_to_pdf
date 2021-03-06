# -*- coding: utf-8 -*-

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

import gtk
import mysql.connector
#~ import os
import sys
import locale


def on_convert_pressed(calcbutton, adress_entry, login_entry, password_entry,db_entry,query_entry):
    adress = adress_entry.get_text()
    login = login_entry.get_text()
    password = password_entry.get_text()
    db = db_entry.get_text()
    query = query_entry.get_text()
    
    data = connect__to_server(adress, login, password,db,query)
    convert_to_pdf(data)
    #~ os.system('converted.pdf')
    print "do"
def main():
    window = gtk.Window()
    window.set_default_size(300,200)
    window.set_title(u"sql_to_dpf")


    mainbox = gtk.VBox()
    window.add(mainbox)

    adress_box = gtk.HBox()
    mainbox.pack_start(adress_box, expand=False)
    login_box = gtk.HBox()
    mainbox.pack_start(login_box, expand=False)
    password_box = gtk.HBox()
    mainbox.pack_start(password_box, expand=False)
    db_box = gtk.HBox()
    mainbox.pack_start(db_box,expand=False)
    query_box = gtk.VBox()
    mainbox.pack_start(query_box,expand=False)

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
    password_entry.set_text(u"root")
    password_entry.set_visibility(0) # поле для пароля показывает звёздочки
    password_box.pack_start(password_entry)
    
    db_label = gtk.Label(u"database")
    db_box.pack_start(db_label)
    db_entry = gtk.Entry()
    db_entry.set_text(u"test")
    db_box.pack_start(db_entry)

    query_label = gtk.Label(u"query sql")   	
    query_box.pack_start(query_label)
    query_entry = gtk.Entry()
    query_entry.set_text(u"SELECT * FROM `city` ORDER BY `name` DESC")
    query_box.pack_start(query_entry)


    convert_button = gtk.Button(u"convert")
    mainbox.pack_start(convert_button, expand=False)

    d_flabel = gtk.Label(u"")
    mainbox.pack_start(d_flabel,expand=False)


    #sw = gtk.ScrolledWindow()
    #sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

    window.connect("destroy", lambda _: gtk.main_quit())
    convert_button.connect("clicked", on_convert_pressed, adress_entry, login_entry, password_entry,db_entry,query_entry)

    window.show_all()
    gtk.main()

def connect__to_server(adress, login, password_db,db,query): #Данная функция соединяется с сервером, уведомляет об успешном соединение
	from mysql.connector import errorcode
	if sys.stdin.encoding: encoding = sys.stdin.encoding
	else: encoding = locale.getdefaultlocale()[1]
	try:
		cnx = mysql.connector.connect(user=login, password=password_db, host=adress, database=db)
		cursor = cnx.cursor()
		#~ query = ('SELECT * FROM `city` ORDER BY `name` DESC')
		cursor.execute(query)
		data = []
		for name in cursor:
			
			i =0
			k = len(name)
			#~ string=""
			
			spisok=[]
			while i < k:
				#~ string+= unicode(name[i])
				spisok.append(name[i])
				i+=1
				
			#~ print string	
			data.append(spisok)
			print data
			print "\n"
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exists")
		else:
			print(err)
	else:
		cursor.close()
		cnx.close()
	return data
	
def convert_to_pdf(data): #данная функция превращает данные в pdf
	doc = SimpleDocTemplate("converted.pdf", pagesize=letter)
	# container for the 'Flowable' objects
	elements = []
	t=Table(data)
	t.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))
	elements.append(t)
	# write the document to disk
	doc.build(elements)


if __name__ == "__main__":
	main()
