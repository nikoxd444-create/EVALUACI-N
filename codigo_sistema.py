# Sistema de cálculo de envío de paquetes con recargos y descuentos fijos

# Función para pedir un número decimal al usuario y validar que sea correcto
def obtener_float(mensaje):
    """Función para validar que la entrada sea un número positivo."""
    
    while True:  # Bucle infinito que se repite hasta que el usuario ingrese un valor válido
        try:
            # input() pide el dato al usuario
            # float() intenta convertir el texto ingresado a número decimal
            valor = float(input(mensaje))
            
            # Se verifica que el número sea mayor o igual a 0
            if valor >= 0:
                return valor  # Si es válido, se devuelve el número y se termina la función
            else:
                # Si el número es negativo se muestra un error
                print("Error: el valor debe ser mayor o igual a 0.")
        
        except ValueError:
            # Si el usuario escribe letras o algo que no se pueda convertir a número
            print("Error: por favor ingresa un número válido.")


# Función para validar respuestas de tipo SI o NO
def obtener_si_no(mensaje):
    
    while True:  # Bucle que se repetirá hasta que el usuario escriba una respuesta válida
        
        # input() pide la respuesta
        # strip() elimina espacios al inicio y al final
        # lower() convierte el texto a minúsculas para evitar problemas con SI, Si, etc.
        respuesta = input(mensaje).strip().lower()

        # Si el usuario no escribe nada
        if respuesta == "":
            print("Error: no puedes dejar el campo vacío.")
        
        # Si la respuesta está dentro de las opciones permitidas
        elif respuesta in ["si", "no"]:
            
            # Si escribe "si" devuelve True
            # Si escribe "no" devuelve False
            return respuesta == "si"
        
        else:
            # Si escribe cualquier otra cosa se muestra error
            print("Error: ingresa solo 'si' o 'no'.")            


# Porcentajes predefinidos del sistema
RECARGO_URGENTE = 10.0      # Porcentaje de recargo si el envío es urgente
DESCUENTO_PROMO = 5.0       # Porcentaje de descuento promocional


# -----------------------------
# ENTRADA DE DATOS
# -----------------------------

# Se pide el peso del paquete en kilogramos usando la función de validación
peso = obtener_float("Ingrese el peso del paquete (kg): ")

# Se pide el precio base del envío
precio_base_envio = obtener_float("Ingrese el precio base por envío: ")

# Se pide el precio adicional por cada kilogramo
precio_por_kg = obtener_float("Ingrese el precio por kilogramo: ")


# -----------------------------
# PREGUNTAS AL USUARIO
# -----------------------------

# Se pregunta si el cliente desea envío urgente
# La función devuelve True si responde "si" y False si responde "no"
aplica_recargo = obtener_si_no("¿Desea envío urgente? (si/no): ")

# Se pregunta si el cliente desea aplicar descuento promocional
aplica_descuento = obtener_si_no("¿Desea aplicar descuento promocional? (si/no): ")


# -----------------------------
# CÁLCULOS DEL ENVÍO
# -----------------------------

# Se calcula el precio base total del envío
# precio base + (peso del paquete * precio por kilogramo)
precio_base_total = precio_base_envio + (peso * precio_por_kg)

# Se calcula el recargo
# Si aplica_recargo es True se calcula el 10%
# Si es False el recargo será 0
recargo = RECARGO_URGENTE / 100 * precio_base_total if aplica_recargo else 0

# Se calcula el descuento
# Si aplica_descuento es True se calcula el 5%
# Si es False el descuento será 0
descuento = DESCUENTO_PROMO / 100 * precio_base_total if aplica_descuento else 0

# Se calcula el precio final del envío
# precio base + recargo - descuento
precio_final = precio_base_total + recargo - descuento


# -----------------------------
# FACTURA / RESULTADOS
# -----------------------------

# Se imprime un título para mostrar los resultados
print("\n===== Detalles del envío =====")

# Se muestra el peso del paquete
print(f"Peso del paquete: {peso} kg")

# Se muestra el precio base del envío
print(f"Precio base por envío: ${precio_base_envio:.2f}")

# Se muestra el precio por kilogramo
print(f"Precio por kg: ${precio_por_kg:.2f}")

# Se muestra el precio base total calculado
print(f"Precio base total: ${precio_base_total:.2f}")


# Si el usuario eligió envío urgente
if aplica_recargo:
    
    # Se muestra el porcentaje de recargo aplicado
    print(f"Envío urgente seleccionado: {RECARGO_URGENTE}% de recargo")
    
    # Se muestra el valor del recargo en dinero
    print(f"Valor del recargo: ${recargo:.2f}")


# Si el usuario eligió descuento promocional
if aplica_descuento:
    
    # Se muestra el porcentaje de descuento aplicado
    print(f"Descuento promocional aplicado: {DESCUENTO_PROMO}%")
    
    # Se muestra el valor que se descuenta
    print(f"Valor descontado: ${descuento:.2f}")


# Finalmente se muestra el precio total que el cliente debe pagar
print(f"Precio final a pagar: ${precio_final:.2f}")