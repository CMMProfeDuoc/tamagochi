"""
Tamagochi:
    nombre
    vida
    hambre
    >> sueño (pendientes)
    >> estado_animo (pendiente)
"""


def crearTamagochi (nombre:str) -> dict:
    tamagochi = {
        'nombre':nombre,
        'vida':100,
        'hambre':0,
    }

    return tamagochi

def imprimirTamagochi (tamagochi:dict) -> None:
    print('Nombre:',tamagochi['nombre'])
    print('Vida:',tamagochi['vida'])
    print('Hambre:',tamagochi['hambre'])

def guardarTamagochi (tamagochi:dict, nombre_archivo:str='*') -> None:

    if (nombre_archivo == '*'):
        nombre_archivo = 'datos_'+str(tamagochi['nombre'])+'.tmg'

    archivo = open(nombre_archivo,'w')

    for valor in tamagochi.values():
        archivo.write(str(valor) + '\n')

    archivo.close()

def cargarTamagochi (nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo,'r')

    datos_archivo = archivo.readlines()
    tamagochi = {
        'nombre': datos_archivo[0].replace('\n',''),
        'vida': datos_archivo[1].replace('\n',''),
        'hambre': datos_archivo[2].replace('\n',''),
    }

    archivo.close()

    return tamagochi
