# Base de datos

El sistema AnimeFull utilizara una base de datos para guardar la informacion principal de la tienda.

La base de datos ayudara a tener ordenados los productos, clientes, pedidos, ventas y alertas de inventario.

Por el momento se tiene pensado utilizar SQLite porque es una base de datos local, sencilla y no necesita instalar un servidor externo.

Algunas tablas que podria tener el sistema son:

## Productos

Aqui se guardaran datos como nombre del producto, anime, categoria, precio, stock y stock minimo.

## Clientes

Aqui se podran guardar datos basicos del cliente, como nombre, gustos o historial de compras.

## Pedidos

Aqui se registraran los pedidos generados dentro del sistema.

## Ventas

Aqui se guardara la informacion de las ventas realizadas.

## Alertas

Aqui se podran guardar los productos que tengan bajo stock o que esten agotados.