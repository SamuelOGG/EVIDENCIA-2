from collections import namedtuple
import pandas as pd
import csv 
import datetime

#PARTE AGREGADA POR ANGEL SAUL DAVALOS FRAUSTRO
Registros = {} #Diccionario que gauradara todos los registros donde la llave sea el folio
#PARTE AGREGADA POR ANGEL SAUL DAVALOS FRAUSTRO
Servicio= namedtuple("Detalle", ("nombre", "descripcion", "descripcion_servicio", "precio"))#Tupla nominada que le dara un orden a los datos que guardamos
#PARTE AGREGADA POR ANGEL SAUL DAVALOS FRAUSTRO
Clave_servicio = namedtuple("Clave_servicio", "folio fecha")#Tupla nominada que le dara un orden a los datos de fecha y folio

#PARTE AGRAGADA POR SAMUEL OBED GARCIA GOMEZ
Nombre = [] #Lista que guarda los datos de la variable nombre del csv
#PARTE AGRAGADA POR SAMUEL OBED GARCIA GOMEZ
Fecha= [] #Lista que guarda lo datos de la variable fecha del csv
#PARTE AGRAGADA POR SAMUEL OBED GARCIA GOMEZ
Folio = [] #Lista que guarda los datos de la variable folio del csv

separador = ('-'*80+'\n') #Variable que nos ayudara para separar las opciones y darle mejor formato de presentacion

#Un try que nos ayuda a validad los datos guardados en un archivo CSV en dado caso que se tenga un archivo CSV con datos
try: #(ESTE APARTADO FUE PROGRAMADO POR SAMUEL OBED GARCIA GOMEZ)
    with open("Reporte.csv", "r", newline="") as archivo: #comando que nos ayuda a seleccionar el archivo a abrir
        lector = csv.reader(archivo)#comando para que lea el archivo csv
        lista_claves = [] # lista que almacena los datos de fecha y folio del archivo csv
        lista_registros = [] # lista que almacena los registros del csv
        #for que valida los datos registrados en el csv 
        for folio, fecha, nombre, descripcion, descripcion_servicio, precio in lector:
            clave = (Clave_servicio(int(folio), fecha))
            if clave not in lista_claves:
                lista_claves.append(clave)
            lista_registros.append((Clave_servicio(int(folio), fecha), Servicio(nombre, descripcion, descripcion_servicio, float(precio))))
            # Aqui se guardan los datos de nombre, folio, fecha en las listas de Nombre, Fecha, Flio 
            # para que funcione correctamente la opcion de consulta por rango de fecha
            Nombre.append(nombre)
            Folio.append(folio)
            Fecha.append(fecha)
        #for que hace que no se reptian los registros de un mismo folio del csv
        for clave in lista_claves:
            articulos = []
            for articulo in lista_registros:
                if clave == articulo[0]:
                    articulos.append(articulo[1])
            Registros[clave] = articulos
except Exception:
    print(separador)
    print("No se encontro ningun archivo CSV....")
else: 
    print(separador)
    print("Se encontro el archivo CSV....")#(ESTE APARTADO PROGRAMADO POR SAMUEL OBED GARCIA GOMEZ TERMINA AQUI)


    
#while True principal que maneja las opciones del menu principal
while True:  #(ESTE APARTADO FUE PROGRAMADO POR ANGEL SAUL DAVALOS FRAUSTRO)
    print(separador)
    print("******** MENU PRINCIPAL ********")
    print("[1] Registrar un servicio")
    print("[2] Consultar registros por folio")
    print("[3] Consultar registros po fecha")
    print("[4] Consultar registros por rango de fecha")
    print("[5] Guardar datos en archivo CSV")
    print("[6] Salir")
    
    print(separador)
    OpcionMenu = int(input("Selecciona una opcion:")) #variable que tomara el valor de la opcion que quieres usar
    print(separador)#(ESTE APARTADO PROGRAMADO POR ANGEL SAUL DAVALOS FRAUSTRO TERMINA AQUI)
    
    # if de opcion 1 en la cual capturan los datos de nombre, descripcion, descripcion_servicio, precio, fecha y folio
    if OpcionMenu == 1: #(ESTE IF DE LA OPCION 1 FUE INICIADO Y PROGRAMADO POR ANGEL SAUL DAVALOS FRAUSTRO)
        #try que valida que la fecha este escrita correctamente
        try:
            fecha_capturada = input("Ingresa la fecha de tu servicio en formato (DD/MM/YYYY): ")
            fecha = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
        except ValueError:
            print("\n**El fromato de fecha no es valido**")
            continue
        # while true que valida que el folio no se repite
        while True:
            folio = int(input("Ingrese el numero de folio: "))
            for clave in Registros.keys(): 
                if folio == clave.folio:
                    print("***Este folio ya esta registrado intenta uno nuevo***\n")
                    break
            else:
                break

        clave_servicio = Clave_servicio(folio, fecha) #variable en donde se gurdan los datos de folio y fecha
        comprobante = [] #lista que almacena los datos de nombre, descripcion, descripcion_servicio, precio
        nombre = input("Ingresa tu nombre: ") #variable que te pide que escribas tu nombre
        #(ESTE APARTADO PROGRAMADO POR ANGEL SAUL DAVALOS FRAUSTRO TERMINA AQUI)

        Nombre.append(nombre) #apartado que guarda el nombre (PARTE AGRAGADA POR SAMUEL OBED GARCIA GOMEZ)
        Folio.append(folio) #apartado que guarda el folio (PARTE AGRAGADA POR SAMUEL OBED GARCIA GOMEZ)
        Fecha.append(fecha) #apartado que guarda la fecha(PARTE AGRAGADA POR SAMUEL OBED GARCIA GOMEZ)

        # whil true que nos pide los artidulos y servicios a agregar ademas del precio
        while True: #(ESTE WHILE TRUE COMPLETO FUE PROGRAMADO POR RUBEN ALEXIS CRUZ QUIÑONES) 
            descripcion = input("Ingresa el articulo al que le haremos el servicio: ")
            if descripcion == "":
                print("***No me has dado ningun articulo***")
            else:
                descripcion_servicio = input("Ingresa el servicio que necesitara tu articulo: ")
                precio = float(input("Precio del articulo: "))
            articulo_en_turno = Servicio(nombre, descripcion, descripcion_servicio, precio)
            comprobante.append(articulo_en_turno)
            
            print(separador)
            # sub menu con pregunta si quieres agregar algun articulo o servicio mas
            seguir_registrando = int(input("¿Desas agregar mas articulos? AGREGAR[0] | VOLVER AL MENU[1]:"))
            print(separador)
            
            # if y elif que nos dara a elegir si volvemos al menu o agregamos algun articulo y servicio mas
            if seguir_registrando == 0:
                continue
            elif seguir_registrando == 1:
                total_venta = 0
                Registros[clave_servicio] = comprobante
                for articulo in Registros[clave_servicio]:
                    total_articulo =  articulo.precio
                    total_venta = total_venta + total_articulo
                # comandos que nos calcula el IVA y que nos da el total mas el IVA a pagar
                IVA = total_venta * .16
                total_mas_iva = total_venta + IVA
                print(f"El total a pagar es: {total_mas_iva}")
                print(f"El IVA a pagar es de: {IVA}")
                break #(ESTE WHILE TRUE PROGRAMADO POR RUBEN ALEXIS CRUZ QUIÑONES TERMINA AQUI)
    

    #if opcion 2 aqui se hace la consulta por folio de un cliente y sus articulos a dar servicio
    elif OpcionMenu == 2: #(ESTE ELIF FUE PROGRAMADO POR ANGEL SAUL DAVALOS FRAUSTRO)
        # variable que pide el folio de la consulta
        folio_a_cosultar = int(input("Ingresa el folio que se desa consultar: "))
        #variable que valida el folio en los registros
        lista_claves = list(Registros.keys())
        # for con las consulta si el folio a consultar es igual al folio entonces imprime lo que esta dentro del mismo
        for clave in lista_claves:
            if folio_a_cosultar == clave.folio:
                total = 0
                print(f"\nEl folio del servicio es: {clave.folio}")
                print(f"La fecha del servicio es: {clave.fecha}")
                print(f'{"Nombre":<15} | {"Descripcion":<15} | {"Servicio":<15} | {"Precio servicio":<15} \n') 
                for venta in Registros[clave]:
                    print(f"{venta.nombre:<15} | {venta.descripcion:<15} | {venta.descripcion_servicio:<15} |${venta.precio:<15}")
                    total_por_articulo = venta.precio
                    total = total + total_por_articulo
                # procedimientos para sacar el iva y total con el iva
                iva = total * .16
                total_mas_iva = total + iva
                print(f"IVA (16%): {iva}")
                print(f"Total a pagar: {total_mas_iva}")#(ESTE APARTADO PROGRAMADO POR ANGEL SAUL DAVALOS FRAUSTRO TERMINA AQUI)


    # opcion 3 que nos da la consulta por fecha de los registros que ya tenemos
    elif OpcionMenu == 3: #(ESTE ELIF COMPLETO FUE PROGRAMADO POR RUEBEN ALEXIS CRUZ QUIÑONES) 
        # try en donde agregamos la variables que piden la fecha al usario y validan de una que sea de un formato correcto
        try:
            convercion_fecha = input("Ingresa la fecha a consultar en el formato (DD/MM/YYYY): ")
            fecha_a_buscar = datetime.datetime.strptime(convercion_fecha , "%d/%m/%Y").date()
        except ValueError:
            print("\n**El fromato de fecha no es valido**")
            continue
        # for y variable que valida los datos que se imprimiran en pantalla que estan almacenadas en listas y tuplas nominadas
        lista_claves = list(Registros.keys())
        for clave in lista_claves:
            if fecha_a_buscar == clave.fecha:
                total = 0
                print(f"\nEl folio del servicio es: {clave.folio}")
                print(f"La fecha del servicio es: {clave.fecha}")
                print(f'{"Nombre":<15} | {"Descripcion":<15} | {"Servicio":<15} | {"Precio servicio":<15} \n')
                for venta in Registros[clave]:
                    print(f"{venta.nombre:<15} | {venta.descripcion:<15} | {venta.descripcion_servicio:<15} |${venta.precio:<15}")
                    total_por_articulo = venta.precio
                    total = total + total_por_articulo
                # se vuelve a realizar la operacion de el iva a cobrar y el total mas iva de cada cosnulta de datos
                iva = total * .16
                total_mas_iva = total + iva
                print(f"IVA (16%): {iva}")
                print(f'Total a pagar: {total_mas_iva}')#(ESTE ELIF PROGRAMADO POR RUEBEN ALEXIS CRUZ QUIÑONES TERMINA AQUI)

    # opcion 4 que nos consulta los registros en un rango de fechas que el usario ingrese
    elif OpcionMenu == 4:#(ESTE APARTADO FUE PROGRAMADO POR RUBEN ALEXIS CRUZ QUIÑONES)
        print("--Ingresa el rango de fechas que quieres consultar--")
        #validacion de las fechas que el usario quiere consultar con el formato datetime
        try:
            fecha_inicio = input("\nIngresa la fecha de inicio en el formato (DD/MM/YYYY): ")
            fecha_1 = datetime.datetime.strptime(fecha_inicio , "%d/%m/%Y").date()

            fecha_final = input("\nIngresa la fecha final en el formato (DD/MM/YYYY): ")
            fecha_2 = datetime.datetime.strptime(fecha_final , "%d/%m/%Y").date()
        except ValueError:
            print("\n**El fromato de fecha no es valido**")
            continue
        
        # en este apartado se uso pandas para darle formato a los datoa que se veran por el usario

        #variable que nos traera los datos que queremos ver en el rango de fechas
        df = pd.DataFrame({"Nombre": Nombre , 'Fechas': pd.to_datetime(Fecha),"Folio": Folio}) 
        df = df.set_index(['Fechas']) #este sera el indice que tiene nuestra tabla hecha con pandas
        
        filtered_df=df.loc[fecha_1 : fecha_2] #esta variable busca ente las fechas que registro el usario 
        print("\n", filtered_df)#(ESTE APARTADO PROGRAMADO POR RUBEN ALEXIS CRUZ QUIÑONES TERMINA AQUI)

    # opcion 5 que nos permite guradar y registrar los datos en un archivo CSV
    elif OpcionMenu == 5:#(ESTE APARTADO FUE PROGRAMADO POR SAMUEL OBED GARCIA GOMEZ)
        print("Quieres guardar los datos en un archivo CSV y salir?\n")
        Opcion = int(input("GUARDAR Y SALIR[0]  |   VOLVER AL MENU[1]   |   GUARDAR[2]: "))
        # si la opcion es 0 entonces guardaremos y saldremos del programa
        if Opcion == 0:
            # aqui este el nombre que le dimos al archivo y que almacenara los datos que tenemos el apartado de registros
            with open ("Reporte.csv" , "w", newline="") as archivo:
                grabador = csv.writer(archivo)
                for clave, detalle in Registros.items():
                    for articulo in detalle:
                        grabador.writerow((clave.folio, clave.fecha, articulo.nombre, articulo.descripcion, articulo.descripcion_servicio, articulo.precio))
                print("El arvhivo CSV se creo correctamente con el nombre de: 'Reporte.csv'\n")
            break

        #Si la opcion es 1 entonces se volvera al menu principal
        elif Opcion == 1:
            continue

        # si la opcion es 2 entonces se guardaran solo los datos y vovlera al menu principal
        elif Opcion == 2:
            # esto es lo mismo que la opcion 0 solo que aqui no sales totalmente del programa
            with open ("Reporte.csv" , "w", newline="") as archivo:
                grabador = csv.writer(archivo)
                for clave, detalle in Registros.items():
                    for articulo in detalle:
                        grabador.writerow((clave.folio, clave.fecha, articulo.nombre, articulo.descripcion, articulo.descripcion_servicio, articulo.precio))
                print("\nEL guardado se ha completado exitosamente con el nombre: 'Reporte.csv'...\n")
            continue#(ESTE APARTADO PROGRAMADO POR SAMUEL OBED GARCIA GOMEZ TERMINA AQUI)
        
    # opcion 6 nos permite salir sin guardar los datos registrados o de lo contrario volver al menu principal 
    elif OpcionMenu == 6:#(ESTE APARTADO FUE PROGRAMADO POR ANGEL SAUL DAVALOS FRAUSTRO)
        print("¿Estas seguro que quieres salir?\n")
        print("**NO SE GUARDARAN TUS DATOS REGISTADOS**\n")
        confirmacion = int(input("SALIR[0] | VOLVER AL MENU[1]: "))
        print(separador)
        if confirmacion == 0:
            break
        elif confirmacion == 1:
            continue#(ESTE APARTADO PROGRAMADO POR ANGEL SAUL DAVALOS FRAUSTRO TERMINA AQUI)