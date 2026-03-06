# Sistema de cálculo de envío de paquetes con recargos y descuentos fijos

def obtener_float(mensaje):
    """Función para validar que la entrada sea un número positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Error: el valor debe ser mayor o igual a 0.")
        except ValueError:
            print("Error: por favor ingresa un número válido.")

# Porcentajes predefinidos
RECARGO_URGENTE = 10.0      # 10% de recargo por envío urgente
DESCUENTO_PROMO = 5.0       # 5% de descuento promocional

# Entrada de datos
peso = obtener_float("Ingrese el peso del paquete (kg): ")
precio_base_envio = obtener_float("Ingrese el precio base por envío: ")
precio_por_kg = obtener_float("Ingrese el precio por kilogramo: ")

# Preguntar al usuario si aplica recargo o descuento
aplica_recargo = input("¿Desea envío urgente? (s/n): ").strip().lower() == 's'
aplica_descuento = input("¿Desea aplicar descuento promocional? (s/n): ").strip().lower() == 's'

# Cálculos
precio_base_total = precio_base_envio + (peso * precio_por_kg)
recargo = RECARGO_URGENTE / 100 * precio_base_total if aplica_recargo else 0
descuento = DESCUENTO_PROMO / 100 * precio_base_total if aplica_descuento else 0
precio_final = precio_base_total + recargo - descuento

# Salida de resultados
print("\n===== Detalles del envío =====")
print(f"Peso del paquete: {peso} kg")
print(f"Precio base por envío: ${precio_base_envio:.2f}")
print(f"Precio por kg: ${precio_por_kg:.2f}")
print(f"Precio base total: ${precio_base_total:.2f}")
if aplica_recargo:
    print(f"Recargo por envío urgente (10%): ${recargo:.2f}")
if aplica_descuento:
    print(f"Descuento promocional (5%): ${descuento:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")