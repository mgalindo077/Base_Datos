import sqlite3

miConexion=sqlite3.connect("PrimeraBBDD")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE Productos (Description VARCHAR(50), Precio INTEGER, Seccion VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15, 'DEPORTES')")

# variosProductos=[
#  	("Camiseta", 10, "DEPORTES"),
#  	("Jarron", 90, "CERAMICA"),
#  	("Camion", 20, "JUGUETERIA")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)
#miConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()

#print(variosProductos)

for producto in variosProductos:
	print("Nombre producto:",producto[0]," Precio:", producto[1]," Seccion: ",producto[2])

miConexion.close()