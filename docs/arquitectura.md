# Arquitectura del sistema

El sistema AnimeFull estara dividido en diferentes partes para que no todo este mezclado en un solo archivo.

La idea principal es que el proyecto funcione como un sistema de tienda de anime, donde se puedan registrar productos, revisar inventario, generar pedidos y recomendar productos a los clientes.

## Interfaz principal

La interfaz sera la parte visual del sistema. Aqui el usuario podra ver el inventario, los productos disponibles, las alertas de bajo stock y las recomendaciones.

Esta parte se hara con Streamlit, ya que permite crear una ventana mas visual con botones, tablas, tarjetas, colores e imagenes.

## Base de datos

La base de datos guardara la informacion importante del sistema.

Aqui se podran almacenar productos, clientes, pedidos, ventas y alertas de inventario.

Para esta parte se utilizara SQLite porque es una base de datos sencilla y funciona de forma local.

## Modulo de inventario

Este modulo se encargara de mostrar los productos registrados y revisar cuantos productos hay disponibles.

Tambien servira para detectar si un producto tiene poco stock o si ya esta agotado.

## Modulo de pedidos

Este modulo servira para crear pedidos o ventas dentro del sistema.

La idea es que cuando un cliente elija un producto, el sistema pueda registrar el pedido y actualizar la informacion.

## Modulo de recomendaciones

Este modulo ayudara a recomendar productos segun lo que busque el cliente.

Por ejemplo, si el cliente quiere algo de Naruto y tiene cierto presupuesto, el sistema buscara productos que coincidan con eso.

## Agentes del sistema

El sistema tendra diferentes agentes, y cada uno tendra una funcion.

El agente cliente se encargara de entender lo que quiere el usuario.

El agente inventario revisara los productos, precios y stock.

El agente recomendador buscara la mejor opcion para el cliente.

El agente pedidos se encargara de registrar pedidos o ventas.

El agente reabastecimiento revisara que productos tienen bajo stock.

El agente explicador dira por que el sistema recomendo cierto producto o por que marco un producto como bajo stock.

## Reglas de inferencia

Las reglas de inferencia serviran para que el sistema pueda tomar decisiones.

Por ejemplo:

- Si el stock es menor al minimo, entonces el producto se marca como bajo stock.
- Si el stock es igual a cero, entonces el producto se marca como agotado.
- Si el cliente pide un anime especifico, entonces se buscan productos de ese anime.
- Si el producto pasa del presupuesto, entonces se busca una opcion mas barata.
- Si un producto tiene alta demanda y poco stock, entonces se recomienda reabastecer.

Con esta organizacion el sistema no sera solo un inventario simple, sino un sistema experto con agentes, reglas, base de datos, pedidos y recomendaciones.