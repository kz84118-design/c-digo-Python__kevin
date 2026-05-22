#kevin Andres Gañan Zapata
#codigo fuente: autoria propia

menu = [
    [ "bandeja paisa", "plato fuerte", 25000],
    [ "sancocho", "plato fuerte", 18000],
    [ "limonada se cereza", "bebida", 7500],
    [ "jugo de maracuya", "bebida", 5000],
    [ "flan de tres leches", "postre", 12000],
    [ "volcan de chocolate", "postre", 15000]
]   

def calcular_total_pedido(producto, promocion, precio):
    categoria_actual = producto[1]
    precio_base = producto[2]

    if categoria_actual == promocion and precio_base > precio:
        precio_final = precio_base * 0.85
    else:
        precio_final = precio_base

    return precio_final

categoria_objetivo = "plato fuerte"
precio_objetivo = 20000

print("---REPORTE DE PRECIOS CON PROMOCION---")

for item in menu:
    nombre = item[0]
    precio_original = item[2]
    precio_con_descuento = calcular_total_pedido(item, categoria_objetivo, precio_objetivo)

    print(f"Producto: {nombre}")
    print(f"Precio base: ${precio_original}")
    print(f"Precio final: ${precio_con_descuento:.2f}")
    print("-----------------------------")
