import sqlite3

conexion = sqlite3.connect('ejemplo.db')

# Crear una tabla

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios con nombres, edades y emails
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios " \
    "(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()

# Inserción con INSERT

cursor = conexion.cursor()

# Insertamos un registro en la tabla de usuarios
cursor.execute("INSERT INTO usuarios VALUES " \
    "('Hector', 27, 'hector@ejemplo.com')")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()

# Lectura con SELECT


cursor = conexion.cursor()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")

# Mostrar el cursos a ver que hay ?
print(cursor)

# Recorremos el primer registro con el método fetchone, devuelve una tupla
usuario = cursor.fetchone()
print(usuario)

conexion.close()



#Inserción múltiple


cursor = conexion.cursor()

# Creamos una lista con varios usuarios
usuarios = [('Mario', 51, 'mario@ejemplo.com'),
            ('Mercedes', 38, 'mercedes@ejemplo.com'),
            ('Juan', 19, 'juan@ejemplo.com')]

# Ahora utilizamos el método executemany() para insertar varios
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()


# Lectura múltiple

cursor = conexion.cursor()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")

# Recorremos todos los registros con fetchall
# y los volcamos en una lista de usuarios
usuarios = cursor.fetchall()

# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)

conexion.close()

# Claves primarias

cursor = conexion.cursor()

# Creamos un campo dni como clave primaria
cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(100) NOT NULL, 
                    marca VARCHAR(50) NOT NULL, 
                    precio FLOAT NOT NULL)''')

productos = [('Teclado', 'Logitech', 19.95),
            ('Pantalla 19"','LG', 89.95),
            ('Altavoces 2.1','LG', 24.95),]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

conexion.commit()
conexion.close()


# Modificación con UPDATE

cursor = conexion.cursor()

# Actualizamos un registro
cursor.execute("UPDATE usuarios SET nombre='Hector Costa' " \
    "WHERE dni='11111111A'")

# Ahora lo consultamos de nuevo
cursor.execute("SELECT * FROM usuarios WHERE dni='11111111A'")
usuario = cursor.fetchone()
print(usuario)

conexion.commit()
conexion.close()


# Borrado con DELETE

cursor = conexion.cursor()

# Creamos un registro de prueba
cursor.execute("INSERT INTO usuarios VALUES " \
    "(null, '55555555E', 'Fernando', 31, 'fernando@ejemplo.com')")

# Consultamos los usuarios
for usuario in cursor.execute("SELECT * FROM usuarios"):
    print(usuario)

# Ahora lo borramos
cursor.execute("DELETE FROM usuarios WHERE dni='55555555E'")

print() # Espacio en blanco

# Consultamos de nuevo los usuarios
for usuario in cursor.execute("SELECT * FROM usuarios"):
    print(usuario)

conexion.commit()
conexion.close()