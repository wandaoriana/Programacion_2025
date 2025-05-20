import psycopg2
conexion = psycopg2.connect(
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5433",
    database="test_bd"
    )

print("Conexion exitosa a la base de datos")
print(conexion)

cursor = conexion.cursor()

sentencia = "SELECT * FROM persona"
cursor.execute(sentencia) # Ejecutamos la sentencia
registros = cursor.fetchall() # Obtenemos todos los registros que seran una lista de tuplas
if registros:
    print(f"Persona encontrada: {registros}")
else:
    print("No se encontró la persona con el id proporcionado.")
# Cerramos cursor y conexión
cursor.close()
conexion.close()
print("Conexion cerrada")
print("Fin del programa")