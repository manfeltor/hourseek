#! python3

"""Escrito por Felipe Torres para INTRALOG SA
Este sencillo programa busca horarios en una columna de excel que les contenga, siempre y cuando
los horarios esten compuestos por horario inicial, un "a" en el medio y horario final asi "XX a XX".
Funciona si son solo numeros o si es formato horario, tambien funciona si hay 2 franjas horarias generando una columna
por cada horario (para horarios de corrido serian 2 columnas, para cortados serian 4).
Nota: no toma los horarios de sabado ni domingo. Cuando encuentra prefijos como "sab" o "dom", corta la linea"""

import re  # Regex
import pyperclip
import time

print("""PROGRAMA DE SEPARACION DE HORARIOS PARA FORMATO SE CARGA TMS

Este sencillo programa busca horarios en una columna de excel que les contenga, siempre y cuando
los horarios esten compuestos por horario inicial, un "a" en el medio y horario final asi "XX a XX".
Funciona si son solo numeros o si es formato horario, tambien funciona si hay 2 franjas horarias generando una columna
por cada horario (para horarios de corrido serian 2 columnas, para cortados serian 4).
Nota: no toma los horarios de sabado ni domingo. Cuando encuentra prefijos como "sab" o "dom", corta la linea

Porfa segui todos los pasos como te va indicando el programa

Escrito por Felipe Torres para INTRALOG SA""")


print("\n", "Empecemos!!!")


prueba = re.compile(r"(\d{1,2}[.:]\d{1,2}|\d{1,4}) [AayY] (\d{1,2}[.:]\d{1,2}|\d{1,4})")  # codigo Regex

while True:
    listaFinal = []
    input("""
    Lo primero que tienes que hacer es seleccionar y copiar la columna de Excel donde se encuentran los horarios
    que quieres recortar
    luego vuelve a esta ventana y presiona ENTER""")
    ingresoExterno = pyperclip.paste().strip().split("\r\n")  # traigo portapapeles, limpio bordes y divido en una lista

    for i in ingresoExterno:
        if "sab" in i.lower():
            i = i[:i.lower().index("sab")]
        if "dom" in i.lower():
            i = i[:i.lower().index("dom")]
        try:
            matchpositivo = prueba.search(i)  # intento match Regex
            listaPositivos = list(matchpositivo.groups())  # Cambio de tupla a lista
            for j in listaPositivos:
                chn = None
                if len(j) == 3:
                    chn = f"0{j[0]}:{j[1:]}"
                elif len(j) == 4:
                    if ":" not in j:
                        chn = f"{j[:2]}:{j[2:]}"
                    else:
                        chn = f"0{j}"
                elif len(j) == 2:
                    chn = f"{j}:00"
                elif len(j) == 1:
                    chn = f"0{j}:00"
                else:
                    chn = j
                listaPositivos[listaPositivos.index(j)] = chn  # armo lista con formato
            x = ("\t".join(listaPositivos))
            matchnegativo = prueba.search(i[::-1])  # trato de encontrar match leyendo al reves p horario 2
            listaNegativos = list(matchnegativo.groups())  # Cambio de Tupla a lista
            for k in listaNegativos:
                cjn = None
                if len(k) == 3:
                    cjn = f"{k[:2]}:{k[2]}0"
                elif len(k) == 4:
                    if ":" not in k:
                        cjn = f"{k[:2]}:{k[2:]}"
                    else:
                        cjn = f"{k}0"
                elif len(k) == 2:
                    cjn = f"00:{k}"
                elif len(k) == 1:
                    cjn = f"00:{k}0"
                else:
                    cjn = k
                listaNegativos[listaNegativos.index(k)] = cjn  # armo lista con formato
            y = ("\t".join(listaNegativos)[::-1])
            if x == y:  # Valido si horario 1 y dos son el mismo
                z = [x]
                listaFinal.append(z[0])
            else:
                z = ("\t".join([x, y]))
                listaFinal.append(z)
        except:
            listaFinal.append("linea sin match")
    pyperclip.copy("\r\n".join(listaFinal))  # traigo la lista formateada como string a porta papeles
    print("\n", "Columna procesada")
    reini = input("""
    pega de vuelta en una matriz de Excel con 4 columnas libres, 
    idealmente al lado de la columna original para comprobar que sean coherentes los resultados, y limpiar a mano
    los que tengan errores.
    (Si no funciono, reinicia el proceso, algo se copio mal)
         
    luego vuelve a esta ventana y presiona x y luego enter para reiniciar, o solo enter para terminar
    
    """)
    print(listaFinal)
    if reini.lower() == "x":
        print("\n", "Reiniciemos", "\n")
        pass
    else:
        break
print("\n", "Eso es todo, el programa se ira actualizando en el tiempo para tener mas funciones")
print("\n", "ante cualquier consulta contactame a ftorres@intralog.com.ar (o manfeltor@live.com)", "\n")
print(" adios")
time.sleep(7)
exit()