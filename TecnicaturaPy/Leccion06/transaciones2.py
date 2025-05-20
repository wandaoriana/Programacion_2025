# Importación de Base de Datos - Permite la conexión con PostgreSQL
import psycopg2 as bd

# Variable de conexión
# Este código puede simplificarse en una sola línea:
# conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='Test_BD', client_encoding='utf8')
conexion = bd.connect(
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5433",
    database="test_bd"
)
# Bloque try 
try:
    conexion.autocommit = False  #inicia la transaccion
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Jorge', 'Prol', 'jprol@gmail.com')
    cursor.execute(sentencia, valores)
    
    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Perez', 'jcperez@email.com', 1)
    cursor.execute(sentencia, valores)
    
    conexion.commit()  #Hacemos commit manualmente, se cierra la transaccion
    print('Termina la transaccion')
# Excepción
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}.')
# Bloque finally
finally: 
    # Cierre de la conexión de la base de datos
    # cursor.close() -> Gracias al with, no es necesario utilizar esta línea.
    conexion.close()