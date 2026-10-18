def cap_rate_rentado(ren_men, valor_ap):
    op_cap_rate = (ren_men / valor_ap) * 100
    return op_cap_rate


print("Inmuebles")
print("Selecciona tipo de inmueble")
print("1. Departamento")
print("2. Terreno")
print("3. Casa")
print("4. Local Comercial")

tipo_inmueble = int(input("Seleccion el numero de tu tipo de inmueble: "))

if tipo_inmueble == 1:
    # Llevar a otra pagina con html
    print("1. Propio")
    print("2. Rentado")
    tp_apartamento = int(input("Ingresa numero de opcion: "))

    if tp_apartamento == 1:
        valor_ap = float(input("Ingresa Valor Total estimado de departamento: "))
        piso_ap = int(input("Ingresa piso de departamento: "))
        hab_ap = int(input("Ingresa habitaciones de departamento: "))
        ub_ap = str(input("Ingresa ubicacion de departamento: "))
        metros_ap = float(input("m² de departamento: "))
        seguro_ap = float(input("Seguro Anual: "))
        impuestos_ap = float(input("Ingresa costo de impuestos anuales: "))
        mant_ap = float(input("Ingresa costo de mantenimiento de Departamento anual: "))

        # Calculo gasto de tenencia
        costo_total = impuestos_ap + seguro_ap + mant_ap

        print("----Tipo rendimiento:-----")
        print("1. Mensual")
        print("2. Anual")
        rendimientos_ap = int(input("Ingresa numero de opcion que deseas: "))

        if rendimientos_ap == 1:
            ren_men = float(input("Ingresa porcentaje de rendimiento mensual de tu departamento: "))
            resultado = cap_rate_rentado(ren_men, valor_ap)
            print(f"Cap rate mensual: {resultado}%")
        elif rendimientos_ap == 2:
            ren_anu = float(input("Ingresa porcentaje de rendimiento anual de tu departamento: "))
            resultado = cap_rate_rentado(ren_anu, valor_ap)
            print(f"Cap rate anual: {resultado}%")
        else:
            print("Valor no valido")

    elif tp_apartamento == 2:
        valor_ap2 = float(input("Ingresa Valor Total estimado de departamento: "))
        renta_ap2 = float(input("Ingresa Renta mensual de departamento: "))
        piso_ap2 = int(input("Ingresa piso de departamento: "))
        hab_ap2 = int(input("Ingresa habitaciones de departamento: "))
        ocupacion_ap2 = float(input("Porcentaje ocupacion de Departamento: "))
        mant_ap2 = float(input("Ingresa costo de mantenimiento de Departamento anual: "))
        ub_ap2 = str(input("Ingresa ubicacion de departamento: "))
        metros_ap2 = float(input("m² de departamento: "))
        seguro_ap2 = float(input("Seguro Anual: "))
        impuestos_ap2 = float(input("Ingresa costo de impuestos anuales: "))
        print("Datos de departamento rentado registrados.")
    else:
        print("Valor no valido")
        # Formularios para indicar Region, pais, municipio.

elif tipo_inmueble == 2:
    # Llevar a otra pagina con html
    valor_te = float(input("Ingresa Valor Total estimado de terreno: "))
    mts_te = float(input("Ingresa metros cuadrados del terreno: "))
    ub_te = str(input("Ingresa ubicacion del terreno: "))
    # Formularios para indicar Region, pais, municipio.

elif tipo_inmueble == 3:
    # Llevar a otra pagina con html
    valor_ca = float(input("Ingresa Valor Total estimado de casa: "))
    mts_ca = float(input("Ingresa metros cuadrados de casa: "))
    pisos_ca = int(input("Ingresa pisos de casa: "))
    banos_ca = int(input("Ingresa banos de casa: "))
    hab_ca = int(input("Ingresa habitaciones de casa: "))
    coc_ca = int(input("Ingresa cantidad de cocinas de casa: "))
    ub_ca = str(input("Ingresa ubicacion de casa: "))

    # Formularios para indicar Region, pais, municipio.

elif tipo_inmueble == 4:
    # Llevar a otra pagina con html
    valor_loc = float(input("Ingresa Valor Total estimado de local :"))
    mts_loc = float(input("Ingresa metros cuadrados de local :"))
    ub_loc = str(input("Ingresa ubicacion de local :"))
    # Formularios para indicar Region, pais, municipio.
else:
    print("Valor no valido")


