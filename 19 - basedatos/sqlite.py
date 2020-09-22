import sqlite3

# conexion
conexion = sqlite3.connect('pruebas.db')

# crear cursor
cursor = conexion.cursor()

# crear tabla
cursor.execute("create table if not exists productos("+
"id integer primary key autoincrement, "+
"title varchar(255), "+
"description text, "+
"price int(255)"+
")")

# cerrar conexion
conexion.close()