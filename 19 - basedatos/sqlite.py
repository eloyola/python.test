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
conexion.commit()

# insert
cursor.execute("insert into productos values(NULL, 'item1','description',200);")
conexion.commit()

# borrar

# cursor.execute("""
# DELETE FROM productos;
# """)

# insertar multiples registros
productos = [
    ('phone', 'good phone', 200),
    ('laptop', 'good laptop', 1200),
]
cursor.executemany("""
INSERT INTO productos values (null,?,?,?)
""", productos)
conexion.commit()
# listar
cursor.execute("Select * from productos;")
print(cursor)

productos = cursor.fetchall()
print(productos)
# cerrar conexion
conexion.close()