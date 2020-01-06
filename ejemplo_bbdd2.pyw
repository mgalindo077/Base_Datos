import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute('''
	CREATE TABLE Productos (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	Description VARCHAR(50) UNIQUE, 
	Precio INTEGER, 
	Seccion VARCHAR(20))
''')

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR04','TREN',15, 'JUGUETERIA')")

variosProductos=[
  	("Camiseta", 10, "DEPORTES"),
  	("Jarron", 90, "CERAMICA"),
  	("Camion", 20, "JUGUETERIA"),
  	("Tren", 15, "JUGUETERIA")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",variosProductos)
miConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()

#print(variosProductos)

for producto in variosProductos:
	print("Nombre producto:",producto[0]," Precio:", producto[1]," Seccion: ",producto[2])

miConexion.close()