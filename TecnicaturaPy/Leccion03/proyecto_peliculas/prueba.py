class Persona:
    def __init__(self, nombre, edad, apellido):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido 

persona1 = Persona("Ana", 30, 'Simich')
persona2 = Persona("fer", 30, 'Simich')


# Podés acceder así:
print(persona2.nombre)  # Ana
print(persona1.edad)    # 30
print(persona1.apellido) 