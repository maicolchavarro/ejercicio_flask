# Precios base por persona para cada paquete
PRECIOS = {
    "Cartagena Colonial": 1200000,
    "Medellín Moderno": 980000,
    "San Andres Islas": 1500000
}

def calcular_precio(paquete, personas):
    """
    Calcula el precio total de un paquete turístico
    """
    if paquete not in PRECIOS:
        raise ValueError("Paquete no válido")
    
    if personas <= 0:
        raise ValueError("Número de personas debe ser positivo")
    
    precio_base = PRECIOS[paquete]
    
    # Aplicar descuentos por grupo
    if personas > 10:
        return precio_base * personas * 0.85  # 15% descuento
    elif personas > 5:
        return precio_base * personas * 0.90  # 10% descuento
    else:
        return precio_base * personas