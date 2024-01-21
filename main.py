
from usuarios import acciones

print("""
    ¿Que deseas hacer?:
    - registrar
    - login
""")

#instanciamos la clase para poder utilizar sus metodos
hazEl = acciones.Acciones()

acciones = input("escribeme lo que quieres hacer !!:")


if acciones == "registrar":
    hazEl.registrar()
elif acciones == "login":
    hazEl.login()
else:
    print("no se puede hacer nada")

