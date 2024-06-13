from funcionesTamagochi import *

opciones_menu = {
    'crear' : ['crear'],
    'guardar' : ['save'],
    'modificar' : ['mod'],
    'salir' : ['salir'],
}

tamagochi = {}

while (True):

    for opcion in opciones_menu.keys():
        print(opcion, '=> ', opciones_menu[opcion])

    seleccion = input('>> ').lower()

    if (seleccion in opciones_menu['crear']):
        tamagochi = crearTamagochi(input('ingrese nombre tamagochi: '))

    if (seleccion in opciones_menu['guardar']):
        guardarTamagochi(tamagochi)

    if (seleccion in opciones_menu['modificar']):
        llave = input('ingrese llave a modificar: ')
        valor = input('ingrese valor a modificar: ')
        tamagochi[llave] = valor

    if (seleccion in opciones_menu['salir']):
        break


