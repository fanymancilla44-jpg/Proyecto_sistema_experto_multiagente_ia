# Flujo del sistema

El sistema AnimeFull funcionara por pasos, para que cada parte tenga una funcion y no se haga todo en desorden.

Primero el usuario entrara al sistema y podra elegir que quiere hacer, por ejemplo revisar inventario, registrar un producto, crear un pedido o pedir una recomendacion.

Si el cliente busca un producto, el sistema revisara lo que escribio y tratara de identificar el anime, el tipo de producto y el presupuesto.

Despues el agente de inventario buscara en la base de datos los productos que coincidan con lo que pidio el cliente.

Luego el agente recomendador seleccionara una opcion tomando en cuenta el precio, el stock y la relacion con el anime solicitado.

Si el producto tiene stock disponible, el sistema podra generar un pedido o venta.

Si el producto tiene poco stock o esta agotado, el sistema mostrara una alerta para reabastecer.

Al final, el agente explicador mostrara por que se recomendo cierto producto o por que se marco como bajo stock.

El flujo general seria:

1. El usuario hace una consulta o selecciona una opcion.
2. El sistema identifica la informacion importante.
3. Se revisa la base de datos.
4. Se aplican reglas de inferencia.
5. Se muestra una recomendacion, pedido o alerta.
6. El sistema explica la decision tomada.