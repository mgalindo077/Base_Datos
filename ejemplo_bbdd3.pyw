import sqlite3

def agregar(cursor, articulo):
	cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", articulo)

def lectura(cursor):
	cursor.execute("SELECT * FROM PRODUCTOS")
	variosProductos=miCursor.fetchall()
	for producto in variosProductos:
		print(producto)

def actualizar(cursor, criterio):
	print(criterio)
	cursor.execute("UPDATE PRODUCTOS SET PRECIO=25 " + criterio )

def borrar(cursor, criterio):
	cursor.execute("DELETE FROM PRODUCTOS " + criterio)

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

borrar(miCursor,"WHERE DESCRIPTION='Balon'")
lectura(miCursor)
articulo=("Balon",90,"DEPORTES")
agregar(miCursor,articulo)
lectura(miCursor)
actualizar(miCursor,"WHERE DESCRIPTION='Camiseta'")
lectura(miCursor)

miConexion.commit()
miConexion.close()