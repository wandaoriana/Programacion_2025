# Importación de Base de Datos
import psycopg2


conexion = psycopg2.connect(
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5433",
    database="test_bd"
    )
# print(conexion)

# Bloque try 
try:
    # Bloque With
    with conexion:
        with conexion.cursor() as cursor:
            # Actualizar o modificar un registro
            # Sentencia UPDATE
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            # Tupla de valores
            valores = ('Illa', 'Garín', 'igarin@gmail.com', 4)
            # Función .execute
            cursor.execute(sentencia, valores)
            # Función .rowcount
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')
# Excepción
except Exception as e:
    print(f'Ocurrió un error: {e}.')
# Bloque finally
finally: 
    conexion.close()
