'''
carrito = {}
​
​
def agregar_articulo(articulo, precio):
    carrito[articulo] = precio
​
​
def sacar_articulo(articulo):
    del carrito[articulo]
​
​
def calcular_total():
    total = 0
    for articulo in carrito:
        total = total + carrito[articulo]
    return total
​
​
def sacar_articulos(articulos):
    for articulo in articulos:
        del carrito[articulo]
​
​
def aplicar_descuento(descuento, articulos):
    for articulo in articulos:
        carrito[articulo] = carrito[articulo] - (carrito[articulo] * (descuento / 100))
​
​
agregar_articulo("jabon", 10.78)
agregar_articulo("servilletas", 8.65)
agregar_articulo("champu", 20.12)
agregar_articulo("arroz", 18.94)
agregar_articulo("pan", 25.35)
print(carrito)
​
sacar_articulos(["jabon", "champu"])
print(carrito)
​
print(calcular_total())
​
aplicar_descuento(10, ["arroz", "pan"])
print(carrito)
​
print(calcular_total())
'''

carrito = {}
def agregar_articulo(articulo, precio):
   carrito[articulo] = precio
def cambiar_precio(articulo,precio):
   carrito[articulo]=precio
   print(carrito)
def sacar_articulo(articulo):
   del carrito[articulo]
def calcular_total():
   total = 0
   for articulo in carrito:
       total = total + carrito[articulo]
   return total
def sacar_articulos(articulos):
   for articulo in articulos:
       del carrito[articulo]
def aplicar_descuento(descuento, articulos):
   for articulo in articulos:
       carrito[articulo] = carrito[articulo] - (carrito[articulo] * (descuento / 100))
agregar_articulo("jabon", 10.78)
agregar_articulo("servilletas", 8.65)
agregar_articulo("champu", 20.12)
agregar_articulo("arroz", 18.94)
agregar_articulo("pan", 25.35)
print(carrito)
cambiar_precio("jabon",12.8)
sacar_articulos(["jabon", "champu"])
print(carrito)
print(calcular_total())
descuento = int(input(f"ingrese el porcentaje a hacer el descuento:"))
aplicar_descuento(descuento, ["arroz", "pan"])
print(carrito)
print(calcular_total())