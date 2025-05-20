import psycopg2 as bd

# Conexión en una sola línea (alternativa comentada)
# conexion = bd.connect(user='postgres', password='1234', host='127.0.0.1', port='5433', database='test_bd', client_encoding='utf8')

# Conexión a la base de datos
conexion = bd.connect(
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5433",
    database="test_bd"
)

try:
      #conexion.autocommit = False  # No deberia estar 
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    valores = ('Maria', 'Esperanza', 'msparza@gmail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()  # hacemos el conmit manualmente
    print('Transacción completada exitosamente')
except Exception as e:
    conexion.rollback()  # Revertimos cambios en caso de error
    print(f'Ocurrió un error, se hizo un rollback : {e}')
finally:
    cursor.close()      # Cerramos el cursor
    conexion.close()    # Cerramos la conexión
