#VARIABLES GLOBALES
historial_conceptos = []
historial_montos = []



#DEFINICIO DE FUNCIONES
def registrar_gasto(saldo_actual, historial_conceptos, historial_montos):
    que_compraste = input("¿En qué gastaste el dinero?: ")
    cuanto_costo = input("¿Cuánto costó?: ")
    monto_gasto = float(cuanto_costo)
    
    # --- ALERTA DE SALDO NEGATIVO ---
    if monto_gasto > saldo_actual:
        print(" ¡ALERTA! No tienes suficiente dinero para este gasto.")
        confirmar = input("¿Quieres registrarlo de todos modos y quedar en deuda? (si/no): ")
        if confirmar.lower() != "si":
            print(" Gasto cancelado. Tu saldo no ha cambiado.")
            return saldo_actual # Regresa el saldo sin cambios
    
    # Si el saldo es suficiente o el usuario aceptó la deuda, se procesa el gasto:
    saldo_actual -= monto_gasto
    historial_conceptos.append(que_compraste)
    historial_montos.append(monto_gasto)
    print(" Gasto anotado con éxito.")
    
    return saldo_actual


def registrar_ingreso(saldo_actual, historial_conceptos, historial_montos):
    fuente_ingreso = input("¿De dónde viene este dinero? (ej. Beca, Trabajo): ")
    cuanto_ingreso = input("¿Cuánto dinero vas a sumar?: ")
    monto_ingreso = float(cuanto_ingreso)
    
    saldo_actual += monto_ingreso # Sumamos al saldo actual
    print(f" ¡Dinero recibido! Se han sumado ${monto_ingreso:.2f} de '{fuente_ingreso}'.")
    
    return saldo_actual


def ver_gastos(historial_conceptos, historial_montos):
    print("\n TU LISTA DE GASTOS:")
    if len(historial_conceptos) == 0:
        print("No has registrado ningún gasto todavía.")
    else:
        for i in range(len(historial_conceptos)):
            print(f"- {historial_conceptos[i]}: ${historial_montos[i]:.2f}")



print("=== BIENVENIDO AL SISTEMA DE PRESUPUESTO ===")

# 1. PEDIR DATOS DE INICIO
nombre = input("¿Cuál es tu nombre?: ")
dinero_inicial = input("¿Con cuánto dinero empiezas el mes?: ")
saldo_actual = float(dinero_inicial)

while True:
    print("\n----------------------------------")
    print(f" Usuario: {nombre}")
    print(f" Saldo disponible: ${saldo_actual:.2f}")
    print("----------------------------------")
    print("1. Registrar un gasto (Restar dinero)")
    print("2. Registrar un ingreso (Sumar dinero/Beca)") # <- NUEVA OPCIÓN
    print("3. Ver lista de gastos realizados")
    print("4. Cambiar de usuario")
    print("5. Ver meta de ahorro")
    print("6. Salir del programa")
    
    opcion = input("Elige una opción (1-6): ")
    
    # OPCIÓN 1: REGISTRAR GASTO
    if opcion == "1":
        saldo_actual = registrar_gasto(saldo_actual, historial_conceptos, historial_montos)

    elif opcion == "2":
        saldo_actual = registrar_ingreso(saldo_actual, historial_conceptos, historial_montos)

    elif opcion == "3":
        ver_gastos(historial_conceptos, historial_montos)

    elif opcion == "4":
        print("\n Cambiando de usuario...")
        nombre = input("¿Cuál es el nombre del nuevo usuario?: ")
        dinero_inicial = input("¿Con cuánto dinero empieza este usuario?: ")
        saldo_actual = float(dinero_inicial)
        
        print(f" Sesión iniciada para {nombre}.")

    # OPCIÓN 5: META DE AHORRO (¡NUEVO!)
    elif opcion == "5":
        print("\n META DE AHORRO MENSUAL")
        cuanto_ahorrar = input("¿Cuánto quisieras ahorrar este mes?: ")
        meta_ahorro = float(cuanto_ahorrar)
    
     # Operaciones
        disponible_para_gastar = saldo_actual - meta_ahorro
    
        if saldo_actual > 0:
            porcentaje = (meta_ahorro / saldo_actual) * 100
            print(f"📊 Tu meta equivale al {porcentaje:.1f}% de tu saldo actual.")
    
        if disponible_para_gastar >= 0:
            gasto_diario = disponible_para_gastar / 30
            print(f"✅ ¡Meta alcanzable! Puedes gastar hasta ${disponible_para_gastar:.2f} este mes.")
            print(f"💡 Eso es un máximo de ${gasto_diario:.2f} por día (mes de 30 días).")
        else:
            faltante = abs(disponible_para_gastar)
            print(f"❌ Con tu saldo actual no alcanzas la meta.")
            print(f"   Te faltan ${faltante:.2f}. Intenta gastar menos o registrar más ingresos.")
        
    # OPCIÓN 6: SALIR
    elif opcion == "6":
        print(f" ¡Adiós {nombre}! Gracias por usar el programa.")
        break
        
    else:
        print(" Opción incorrecta. Digita un número del 1 al 6.")